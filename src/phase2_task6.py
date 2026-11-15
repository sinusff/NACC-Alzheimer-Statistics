import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import seaborn as sns

# Configure plot visual style
sns.set_theme(style="whitegrid")
plt.rcParams["font.sans-serif"] = "DejaVu Sans"

# Load dataset paths
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

# Select continuous MRI variable: Left Entorhinal Cortical Thickness (mm)
target_col = "LH_ENTORHINAL_AVGTH"
series = pd.to_numeric(df[target_col], errors="coerce").dropna()

# 1. Compute summary statistics
n = len(series)
mean_val = series.mean()
std_val = series.std(ddof=1)
median_val = series.median()
skew_val = series.skew()
kurt_val = series.kurtosis()

# 2. Check Empirical Rule (68-95-99.7% rule)
within_1sd = np.mean((series >= mean_val - std_val) & (series <= mean_val + std_val)) * 100
within_2sd = np.mean((series >= mean_val - 2 * std_val) & (series <= mean_val + 2 * std_val)) * 100
within_3sd = np.mean((series >= mean_val - 3 * std_val) & (series <= mean_val + 3 * std_val)) * 100

# 3. Statistical Normality Tests (Shapiro-Wilk and D'Agostino-Pearson)
shapiro_stat, shapiro_p = stats.shapiro(series)
dagostino_stat, dagostino_p = stats.normaltest(series)

print("=== PHASE 2: TASK 6 NORMALITY ASSESSMENT ===")
print(f"Target Variable: {target_col}")
print(f"Sample Size (N): {n}")
print(f"Mean: {mean_val:.4f} mm, Std: {std_val:.4f} mm")
print(f"Median: {median_val:.4f} mm")
print(f"Sample Skewness: {skew_val:.4f} (Ideal Normal: 0.0)")
print(f"Excess Kurtosis: {kurt_val:.4f} (Ideal Normal: 0.0)")

print("\n--- Empirical Rule vs. Theoretical Normal ---")
print(f"Within +/- 1 SD: {within_1sd:.2f}% (Theoretical: 68.27%)")
print(f"Within +/- 2 SD: {within_2sd:.2f}% (Theoretical: 95.45%)")
print(f"Within +/- 3 SD: {within_3sd:.2f}% (Theoretical: 99.73%)")

print("\n--- Formal Statistical Tests ---")
print(f"Shapiro-Wilk Test   : Statistic = {shapiro_stat:.4f}, p-value = {shapiro_p:.4e}")
print(f"D'Agostino-Pearson  : Statistic = {dagostino_stat:.4f}, p-value = {dagostino_p:.4e}")

# 4. Generate Visual Diagnostics: Histogram with Normal Fit + Q-Q Plot
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Subplot 1: Histogram with fitted theoretical normal curve
sns.histplot(
    series,
    bins=30,
    stat="density",
    color="steelblue",
    alpha=0.6,
    edgecolor="white",
    ax=axes[0],
    label="Empirical Density",
)
x_axis = np.linspace(series.min(), series.max(), 300)
pdf_fitted = stats.norm.pdf(x_axis, mean_val, std_val)
axes[0].plot(x_axis, pdf_fitted, "r-", linewidth=2.5, label=f"Normal Fit (μ={mean_val:.2f}, σ={std_val:.2f})")
axes[0].set_title("Histogram with Fitted Normal Curve", fontsize=12, fontweight="bold")
axes[0].set_xlabel("Cortical Thickness (mm)", fontsize=11)
axes[0].set_ylabel("Probability Density", fontsize=11)
axes[0].legend(loc="upper left")

# Subplot 2: Normal Q-Q Plot
stats.probplot(series, dist="norm", plot=axes[1])
axes[1].get_lines()[0].set_markerfacecolor("navy")
axes[1].get_lines()[0].set_markersize(4.0)
axes[1].get_lines()[1].set_color("red")
axes[1].get_lines()[1].set_linewidth(2.0)
axes[1].set_title("Normal Q-Q Plot", fontsize=12, fontweight="bold")
axes[1].set_xlabel("Theoretical Quantiles", fontsize=11)
axes[1].set_ylabel("Sample Quantiles (mm)", fontsize=11)

plt.tight_layout()
fig_output_path = os.path.join(fig_dir, "fig6_normality_check.png")
plt.savefig(fig_output_path, dpi=300)
plt.close()

print(f"\nFigure saved successfully to: {fig_output_path}")