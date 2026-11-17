import os
import pandas as pd

# Load dataset paths dynamically
data_dir = "data"
if not os.path.exists(data_dir):
    data_dir = "../data"

# Read CSV files and merge on NACCID
df_mri = pd.read_csv(os.path.join(data_dir, "mriscanclean.csv"))
df_uds = pd.read_csv(os.path.join(data_dir, "udslong_imputed.csv"))
df_merged = pd.merge(df_uds, df_mri, on="NACCID", suffixes=("_uds", "_mri"))

# 1. Audit participant-level uniqueness (Independence Verification)
uds_rows, uds_unique = len(df_uds), df_uds["NACCID"].nunique()
mri_rows, mri_unique = len(df_mri), df_mri["NACCID"].nunique()
merged_rows, merged_unique = len(df_merged), df_merged["NACCID"].nunique()

# Distribution of visit/scan counts per unique participant
uds_counts = df_uds["NACCID"].value_counts()
mri_counts = df_mri["NACCID"].value_counts()

# 2. Scan column names for explicit longitudinal/visit metadata fields
visit_keywords = ["VISIT", "DATE", "TIME", "NACCV", "SCAN", "YEAR"]
uds_meta_cols = [c for c in df_uds.columns if any(k in c.upper() for k in visit_keywords)]
mri_meta_cols = [c for c in df_mri.columns if any(k in c.upper() for k in visit_keywords)]

print("=== PHASE 2: PATH C - C.5 REPEATED VISITS & INDEPENDENCE AUDIT ===")
print(f"UDS Dataset    -> Total Rows: {uds_rows}, Unique NACCIDs: {uds_unique}, Min/Max Visits per ID: {uds_counts.min()}/{uds_counts.max()}")
print(f"MRI Dataset    -> Total Rows: {mri_rows}, Unique NACCIDs: {mri_unique}, Min/Max Scans per ID : {mri_counts.min()}/{mri_counts.max()}")
print(f"Merged Dataset -> Total Rows: {merged_rows}, Unique NACCIDs: {merged_unique}")

print(f"\nDuplicate Subject Records in Analysis Cohort : {merged_rows - merged_unique}")
print(f"Independence Assumption (1 Obs/Subject) Met  : {merged_rows == merged_unique}")

print(f"\nLongitudinal/Visit Metadata Columns in UDS   : {uds_meta_cols}")
print(f"Longitudinal/Visit Metadata Columns in MRI   : {mri_meta_cols}")