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

# Sanitize special missing codes
df["MOCATOTS"] = df["MOCATOTS"].replace([88, 88.0, 99, 99.0], np.nan)
df["MOCATOTS"] = pd.to_numeric(df["MOCATOTS"], errors="coerce")

# Target quantitative variables for Expected Value and Variance analysis
target_vars = [
    "NACCAGE",
    "MOCATOTS",
    "LH_ENTORHINAL_AVGTH",
    "RH_ENTORHINAL_AVGTH",
]

results = []
for var in target_vars:
    if var in df.columns:
        s = df[var].dropna()
        mean_val = s.mean()  # Empirical Expected Value E[X]
        var_val = s.var(ddof=1)  # Sample Variance (n-1 degrees of freedom)
        std_val = s.std(ddof=1)  # Sample Standard Deviation

        results.append(
            {
                "Variable": var,
                "Sample Mean (E[X])": round(mean_val, 4),
                "Sample Variance (Var)": round(var_val, 4),
                "Standard Deviation (Std)": round(std_val, 4),
            }
        )

df_results = pd.DataFrame(results)
print("=== PHASE 2: TASK 7 EXPECTED VALUE & VARIANCE ===")
print(df_results.to_string(index=False))