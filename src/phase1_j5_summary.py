import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

df['MOCATOTS'] = df['MOCATOTS'].replace([88, 88.0, 99, 99.0], np.nan)
df['MOCATOTS'] = pd.to_numeric(df['MOCATOTS'], errors='coerce')
df['LH_ENTORHINAL_AVGTH'] = pd.to_numeric(df['LH_ENTORHINAL_AVGTH'], errors='coerce')

summary_vars = ['MOCATOTS', 'LH_ENTORHINAL_AVGTH']
stats = df[summary_vars].describe().T[['mean', 'std', '50%', 'min', 'max']]
q75 = df[summary_vars].quantile(0.75)
q25 = df[summary_vars].quantile(0.25)
stats['IQR'] = q75 - q25
print("=== DESCRIPTIVE SUMMARY TABLE ===")
print(stats.round(2))

plot_df = df[['LH_ENTORHINAL_AVGTH', 'MOCATOTS']].dropna()

g = sns.jointplot(
    data=plot_df, 
    x="LH_ENTORHINAL_AVGTH", 
    y="MOCATOTS", 
    kind="reg", 
    color="purple", 
    height=7,
    marginal_kws=dict(bins=20, fill=True)
)
g.fig.suptitle("Figure 5: Common Summary - MoCA Score vs. Entorhinal Thickness", y=1.02)
plt.savefig(os.path.join(fig_dir, "fig5_joint_summary.png"), dpi=300, bbox_inches='tight')
plt.close()

print("\nFigure 5 successfully saved to 'figures/' directory.")