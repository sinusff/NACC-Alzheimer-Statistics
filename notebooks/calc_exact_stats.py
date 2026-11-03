import os
import pandas as pd

data_dir = "data"
if not os.path.exists(data_dir):
    data_dir = "../data"

df_mri = pd.read_csv(os.path.join(data_dir, "mriscanclean.csv"))
df_uds = pd.read_csv(os.path.join(data_dir, "udslong_imputed.csv"))

print("=== 1. EXACT FREQUENCY TABLE: NACCUDSD ===")
counts = df_uds["NACCUDSD"].value_counts().sort_index()
percent = (df_uds["NACCUDSD"].value_counts(normalize=True) * 100).sort_index()
for cat, cnt, pct in zip(counts.index, counts, percent):
    print(f"Category {cat}: Count = {cnt}, Percentage = {pct:.2f}%")

print("\n=== 2. EXACT FREQUENCY TABLE: SEX ===")
counts_sex = df_uds["SEX"].value_counts().sort_index()
percent_sex = (df_uds["SEX"].value_counts(normalize=True) * 100).sort_index()
for s, cnt, pct in zip(counts_sex.index, counts_sex, percent_sex):
    print(f"Sex {s}: Count = {cnt}, Percentage = {pct:.2f}%")

print("\n=== 3. EXACT UDS NUMERIC STATS ===")
for col in ["NACCAGE", "EDUC", "MOCATOTS"]:
    s = df_uds[col].dropna()
    q25, q75 = s.quantile(0.25), s.quantile(0.75)
    print(
        f"{col} -> Mean: {s.mean():.2f}, Std: {s.std():.2f}, Median: {s.median():.2f}, Q1: {q25:.2f}, Q3: {q75:.2f}, IQR: {q75-q25:.2f}, Min: {s.min():.2f}, Max: {s.max():.2f}, Skew: {s.skew():.2f}"
    )

print("\n=== 4. EXACT MRI NUMERIC STATS ===")
for col in [
    "LH_ENTORHINAL_GVOL",
    "RH_ENTORHINAL_GVOL",
    "LH_ENTORHINAL_AVGTH",
    "RH_ENTORHINAL_AVGTH",
]:
    s = df_mri[col].dropna()
    q25, q75 = s.quantile(0.25), s.quantile(0.75)
    print(
        f"{col} -> Mean: {s.mean():.2f}, Std: {s.std():.2f}, Median: {s.median():.2f}, Q1: {q25:.2f}, Q3: {q75:.2f}, IQR: {q75-q25:.2f}, Min: {s.min():.2f}, Max: {s.max():.2f}, Skew: {s.skew():.2f}"
    )