import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")
plt.rcParams["font.sans-serif"] = "DejaVu Sans"

data_dir = "data"
if not os.path.exists(data_dir):
    data_dir = "../data"
fig_dir = "figures"
if not os.path.exists(fig_dir):
    fig_dir = "../figures"
os.makedirs(fig_dir, exist_ok=True)

df_mri = pd.read_csv(os.path.join(data_dir, "mriscanclean.csv"))
df_uds = pd.read_csv(os.path.join(data_dir, "udslong_imputed.csv"))

df = pd.merge(df_uds, df_mri, on="NACCID", suffixes=("_uds", "_mri"))

df['MOCATOTS'] = df['MOCATOTS'].replace([88, 88.0, 99, 99.0], pd.NA)
df['EDUC'] = df['EDUC'].replace([99, 99.0], pd.NA)

diag_map = {1: "Normal", 2: "Impaired (Not MCI)", 3: "MCI", 4: "Dementia"}
df["Diagnosis"] = df["NACCUDSD_uds"].map(diag_map)

plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="Diagnosis", order=["Normal", "Impaired (Not MCI)", "MCI", "Dementia"], palette="viridis")
plt.title("Figure 1: Distribution of Cognitive Diagnosis")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "fig1_diagnosis_dist.png"), dpi=300)
plt.close()

plt.figure(figsize=(7, 5))
sns.histplot(df["MOCATOTS"].dropna(), bins=20, kde=True, color="coral")
plt.title("Figure 2: Distribution of MoCA Score")
plt.xlabel("MoCA Total Score")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "fig2_moca_dist.png"), dpi=300)
plt.close()

plt.figure(figsize=(7, 5))
sns.histplot(df["LH_ENTORHINAL_GVOL"].dropna(), bins=30, kde=True, color="teal")
plt.title("Figure 3: Left Entorhinal Volume Distribution")
plt.xlabel("Volume (mm^3)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "fig3_volume_dist.png"), dpi=300)
plt.close()

plt.figure(figsize=(7, 5))
sns.scatterplot(data=df, x="LH_ENTORHINAL_GVOL", y="MOCATOTS", hue="Diagnosis", palette="Set1", alpha=0.7)
plt.title("Figure 4: Entorhinal Volume vs. MoCA Score")
plt.xlabel("Left Entorhinal Volume (mm^3)")
plt.ylabel("MoCA Score")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "fig4_vol_vs_moca.png"), dpi=300, bbox_inches='tight')
plt.close()

print("Figures successfully generated in the 'figures/' folder!")