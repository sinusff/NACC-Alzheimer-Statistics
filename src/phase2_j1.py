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

# Define Target Event: Cognitive Impairment (NACCUDSD_uds >= 3 for MCI or Dementia)
df["Cognitive_Impairment"] = df["NACCUDSD_uds"] >= 3

# Define MRI Grouping: Split by sample median of Left Entorhinal Volume
median_vol = df["LH_ENTORHINAL_GVOL"].median()
df["MRI_Group"] = np.where(
    df["LH_ENTORHINAL_GVOL"] < median_vol,
    "Low Volume (Atrophy)",
    "Normal/High Volume",
)

# Compute conditional probabilities of cognitive impairment across MRI groups
prob_table = (
    df.groupby("MRI_Group")["Cognitive_Impairment"]
    .agg(Total_Patients="count", Impaired_Patients="sum")
    .reset_index()
)
prob_table["Probability_Impairment"] = (
    prob_table["Impaired_Patients"] / prob_table["Total_Patients"]
)

print("=== PHASE 2: PATH C - C.1 CONDITIONAL PROBABILITY ===")
print(f"Entorhinal Volume Sample Median: {median_vol:.2f} mm^3\n")
print(prob_table.to_string(index=False))