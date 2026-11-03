import os
import pandas as pd

mri_path = os.path.join("..", "data", "mriscanclean.csv")
uds_path = os.path.join("..", "data", "udslong_imputed.csv")

if not os.path.exists(mri_path):
    mri_path = os.path.join("data", "mriscanclean.csv")
    uds_path = os.path.join("data", "udslong_imputed.csv")

df_mri = pd.read_csv(mri_path)
df_uds = pd.read_csv(uds_path)

print("=== MRI Dataset Information ===")
print(f"Number of rows and columns: {df_mri.shape}")
print(f"Number of unique patients (NACCID): {df_mri['NACCID'].nunique()}")

print("\n=== UDS Dataset Information ===")
print(f"Number of rows and columns: {df_uds.shape}")

if "NACCID" in df_uds.columns:
    print(f"Number of unique patients (NACCID): {df_uds['NACCID'].nunique()}")

print(f"UDS column names:\n{list(df_uds.columns)}")

if "NACCID" in df_uds.columns and "NACCID" in df_mri.columns:
    common_ids = set(df_mri["NACCID"]).intersection(set(df_uds["NACCID"]))
    print(f"\nNumber of patients present in both datasets: {len(common_ids)}")