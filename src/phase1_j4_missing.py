import os
import pandas as pd

data_dir = "data"
if not os.path.exists(data_dir):
    data_dir = "../data"

df_mri = pd.read_csv(os.path.join(data_dir, "mriscanclean.csv"))
df_uds = pd.read_csv(os.path.join(data_dir, "udslong_imputed.csv"))

key_uds_vars = ["NACCAGE", "EDUC", "MOCATOTS", "NACCUDSD"]
key_mri_vars = ["LH_ENTORHINAL_GVOL", "RH_ENTORHINAL_GVOL", "LH_ENTORHINAL_AVGTH"]

print("=== 1. MISSINGNESS PERCENTAGE AUDIT ===")
print("\n--- UDS Variables ---")
print(df_uds[key_uds_vars].isnull().mean() * 100)

print("\n--- MRI Variables ---")
print(df_mri[key_mri_vars].isnull().mean() * 100)

print("\n=== 2. MULTIMODAL SAMPLE SELECTION AUDIT ===")
total_n = len(df_uds)
mri_holders = len(df_mri)
print(f"Total Participants: {total_n}")
print(f"Participants with MRI: {mri_holders}")
print(f"Percentage of sample that is multimodal: {(mri_holders/total_n)*100:.2f}%")

print("\n--- Checking for MRI outliers in the multimodal sample ---")
print(df_mri[key_mri_vars].describe().loc[['min', 'max', 'mean']])