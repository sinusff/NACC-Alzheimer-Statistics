import os
import numpy as np
import pandas as pd

data_dir = "data"
if not os.path.exists(data_dir):
    data_dir = "../data"

df_mri = pd.read_csv(os.path.join(data_dir, "mriscanclean.csv"))
df_uds = pd.read_csv(os.path.join(data_dir, "udslong_imputed.csv"))
df = pd.merge(df_uds, df_mri, on="NACCID", suffixes=("_uds", "_mri"))

df["MOCATOTS"] = df["MOCATOTS"].replace([88, 88.0, 99, 99.0], pd.NA)
df["EDUC"] = df["EDUC"].replace([99, 99.0], pd.NA)

quant_vars = [
    "NACCAGE",
    "EDUC",
    "MOCATOTS",
    "LH_ENTORHINAL_GVOL",
    "RH_ENTORHINAL_GVOL",
    "LH_ENTORHINAL_AVGTH",
    "RH_ENTORHINAL_AVGTH",
]

results = []
for var in quant_vars:
    if var in df.columns:
        s = pd.to_numeric(df[var]).dropna()
        mean_val = s.mean()
        std_val = s.std()
        median_val = s.median()
        q1 = s.quantile(0.25)
        q3 = s.quantile(0.75)
        iqr_val = q3 - q1
        skew_val = s.skew()

        results.append(
            {
                "Variable": var,
                "Mean": round(mean_val, 2),
                "Std": round(std_val, 2),
                "Median": round(median_val, 2),
                "Q1 (25%)": round(q1, 2),
                "Q3 (75%)": round(q3, 2),
                "IQR": round(iqr_val, 2),
                "Skewness": round(skew_val, 2),
            }
        )

df_results = pd.DataFrame(results)
print("=== EXACT CENTER & SPREAD METRICS ===")
print(df_results.to_string(index=False))