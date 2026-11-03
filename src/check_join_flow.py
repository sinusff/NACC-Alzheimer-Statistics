import os
import pandas as pd

data_dir = "data"
if not os.path.exists(data_dir):
    data_dir = "../data"

mri_path = os.path.join(data_dir, "mriscanclean.csv")
uds_path = os.path.join(data_dir, "udslong_imputed.csv")

df_mri = pd.read_csv(mri_path)
df_uds = pd.read_csv(uds_path)

mri_ids = set(df_mri["NACCID"])
uds_ids = set(df_uds["NACCID"])

common_ids = mri_ids.intersection(uds_ids)
mri_only = mri_ids - uds_ids
uds_only = uds_ids - mri_ids

merged_df = pd.merge(df_uds, df_mri, on="NACCID", how="inner")

print("=== NACC MULTIMODAL JOIN & DATA FLOW AUDIT ===")
print(f"Total UDS Records: {len(df_uds):,}")
print(f"Total MRI Records: {len(df_mri):,}")
print(f"Overlapping Participants (Common IDs): {len(common_ids):,}")
print(f"Unmatched UDS Cases (Only in UDS): {len(uds_only):,}")
print(f"Unmatched MRI Cases (Only in MRI): {len(mri_only):,}")
print(f"Final Multimodal Merged Sample Size: {len(merged_df):,}")

if len(uds_only) == 0 and len(mri_only) == 0:
    print(
        "\nStatus: Perfect 1-to-1 match. Zero sample loss during integration."
    )
else:
    print(
        "\nStatus: Mismatched cases detected. Check data exclusion logs."
    )