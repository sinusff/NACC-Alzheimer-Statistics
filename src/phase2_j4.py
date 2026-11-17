import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Set publication-quality plot theme
sns.set_theme(style="whitegrid")
plt.rcParams["font.sans-serif"] = "DejaVu Sans"

# Load dataset paths dynamically
data_dir = "data"
if not os.path.exists(data_dir):
    data_dir = "../data"

fig_dir = "figures"
if not os.path.exists(fig_dir):
    fig_dir = "../figures"
os.makedirs(fig_dir, exist_ok=True)

# Read CSV files and merge on NACCID
df_mri = pd.read_csv(os.path.join(data_dir, "mriscanclean.csv"))
df_uds = pd.read_csv(os.path.join(data_dir, "udslong_imputed.csv"))
df = pd.merge(df_uds, df_mri, on="NACCID", suffixes=("_uds", "_mri"))

# Sanitize MoCA scores (remove special missing codes like 88 and 99)
df["MOCATOTS"] = df["MOCATOTS"].replace([88, 88.0, 99, 99.0], np.nan)
df["MOCATOTS"] = pd.to_numeric(df["MOCATOTS"], errors="coerce")

# Map diagnostic codes to readable clinical labels
diag_map = {1: "Normal", 2: "Impaired (Not MCI)", 3: "MCI", 4: "Dementia"}
diag_col = "NACCUDSD_uds" if "NACCUDSD_uds" in df.columns else "NACCUDSD"
df["Diagnosis"] = df[diag_col].map(diag_map)

# Select UDS cognitive score (Y) and MRI volumetric biomarker (X)
sub_df = df[["LH_ENTORHINAL_GVOL", "MOCATOTS", "Diagnosis"]].dropna()

x_vol = sub_df["LH_ENTORHINAL_GVOL"]
y_moca = sub_df["MOCATOTS"]

# 1. Compute Sample Covariance and Correlations
cov_matrix = np.cov(x_vol, y_moca, ddof=1)
cov_val = cov_matrix[0, 1]
pearson_r = x_vol.corr(y_moca, method="pearson")
spearman_rho = x_vol.corr(y_moca, method="spearman")

print("=== PHASE 2: PATH C - C.4 COGNITIVE & MRI COVARIANCE ===")
print(f"Sample Size (Complete Pairs)                 : {len(sub_df)}")
print(f"Sample Covariance Cov(Volume, MoCA)          : {cov_val:.4f}")
print(f"Pearson Correlation Coefficient (r)          : {pearson_r:.4f}")
print(f"Spearman Rank Correlation (rho)              : {spearman_rho:.4f}")

# 2. Generate Scatter Plot with Diagnostic Hue and Linear Trend Line
plt.figure(figsize=(9, 6))
sns.scatterplot(
    data=sub_df,
    x="LH_ENTORHINAL_GVOL",
    y="MOCATOTS",
    hue="Diagnosis",
    palette="Set1",
    alpha=0.75,
    s=55,
)

# Overlay overall linear regression trend line
sns.regplot(
    data=sub_df,
    x="LH_ENTORHINAL_GVOL",
    y="MOCATOTS",
    scatter=False,
    color="black",
    line_kws={"linestyle": "--", "linewidth": 1.5, "alpha": 0.8},
)

plt.title(
    "Figure C.4: Scatter Plot - Left Entorhinal Volume vs. MoCA Score",
    fontsize=13,
    fontweight="bold",
    pad=12,
)
plt.xlabel("Left Entorhinal Gray Matter Volume (mm^3)", fontsize=11)
plt.ylabel("MoCA Total Score (0-30)", fontsize=11)
plt.legend(title="Diagnostic Status", bbox_to_anchor=(1.02, 1), loc="upper left")
plt.tight_layout()

# Save figure at 300 DPI
output_path = os.path.join(fig_dir, "fig_c4_vol_vs_moca_cov.png")
plt.savefig(output_path, dpi=300, bbox_inches="tight")
plt.close()

print(f"\nFigure successfully generated and saved to: {output_path}")