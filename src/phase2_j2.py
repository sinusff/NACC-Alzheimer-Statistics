import os
import numpy as np
import pandas as pd

# Load dataset paths
data_dir = "data"
if not os.path.exists(data_dir):
    data_dir = "../data"

# Read CSV files and merge on NACCID
df_mri = pd.read_csv(os.path.join(data_dir, "mriscanclean.csv"))
df_uds = pd.read_csv(os.path.join(data_dir, "udslong_imputed.csv"))
df = pd.merge(df_uds, df_mri, on="NACCID", suffixes=("_uds", "_mri"))

# Sanitize MoCA scores
df["MOCATOTS"] = df["MOCATOTS"].replace([88, 88.0, 99, 99.0], np.nan)
df["MOCATOTS"] = pd.to_numeric(df["MOCATOTS"], errors="coerce")

# Select variables for Path C requirement J.2:
# 1. UDS Quantitative Cognitive Score: MOCATOTS
# 2. MRI Quantitative Variable: LH_ENTORHINAL_GVOL
target_vars = ["MOCATOTS", "LH_ENTORHINAL_GVOL"]

audit_results = []
for var in target_vars:
    s = df[var].dropna()
    mean_val = s.mean()
    var_val = s.var(ddof=1)
    std_val = s.std(ddof=1)
    skew_val = s.skew()
    
    # Outlier detection using the IQR method (Q1 - 1.5*IQR, Q3 + 1.5*IQR)
    q1 = s.quantile(0.25)
    q3 = s.quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = s[(s < lower_bound) | (s > upper_bound)]
    
    audit_results.append({
        "Variable": var,
        "Mean": round(mean_val, 4),
        "Variance": round(var_val, 4),
        "StdDev": round(std_val, 4),
        "Skewness": round(skew_val, 4),
        "IQR": round(iqr, 4),
        "Outliers_Count": len(outliers),
        "Min": round(s.min(), 4),
        "Max": round(s.max(), 4)
    })

res_df = pd.DataFrame(audit_results)
print("=== PHASE 2: PATH C - C.2 DISTRIBUTIONAL & OUTLIER AUDIT ===")
print(res_df.to_string(index=False))