import os
import pandas as pd

# Load dataset paths
data_dir = "data"
if not os.path.exists(data_dir):
    data_dir = "../data"

# Read CSV files and merge on NACCID
df_mri = pd.read_csv(os.path.join(data_dir, "mriscanclean.csv"))
df_uds = pd.read_csv(os.path.join(data_dir, "udslong_imputed.csv"))
df = pd.merge(df_uds, df_mri, on="NACCID", suffixes=("_uds", "_mri"))

# Sanitize MoCA scores (remove special missing codes like 88 and 99)
df["MOCATOTS"] = df["MOCATOTS"].replace([88, 88.0, 99, 99.0], pd.NA)
df["MOCATOTS"] = pd.to_numeric(df["MOCATOTS"], errors="coerce")

# Total sample size (Sample Space S)
sample_size = len(df)

# Define Event A: Cognitive Impairment (NACCUDSD_uds >= 3)
# Note: Using 'NACCUDSD_uds' because the column exists in both tables
event_a_count = df[df["NACCUDSD_uds"] >= 3].shape[0]

# Define Event B: Presence of Hypertension (HYPERTEN == 1)
event_b_count = df[df["HYPERTEN"] == 1].shape[0]

# Print empirical probabilities for Task 1 validation
print("=== PHASE 2: TASK 1 VALIDATION ===")
print(f"Total Sample Size (|S|): {sample_size}")
print(f"Event A Count (Cognitive Impairment >= MCI): {event_a_count}")
print(
    f"Empirical Probability P(A): {event_a_count / sample_size:.4f} "
    f"({(event_a_count / sample_size)*100:.2f}%)"
)
print(f"Event B Count (Hypertension == 1): {event_b_count}")
print(
    f"Empirical Probability P(B): {event_b_count / sample_size:.4f} "
    f"({(event_b_count / sample_size)*100:.2f}%)"
)

# Random Variable X summary (MoCA Total Score)
moca_stats = df["MOCATOTS"].describe()
print("\n=== RANDOM VARIABLE X (MOCATOTS) SUMMARY ===")
print(moca_stats)