import pandas as pd
import sqlite3
import os

# Paths
RAW_DIR = "data/raw"
DB_PATH = "data/samarth.db"

# Load Crop Data
print("📥 Loading crop production data...")
crop_path = os.path.join(RAW_DIR, "area_and_production_of_crop_2017_18.csv")
crop_df = pd.read_csv(crop_path)

# Clean column names
crop_df.columns = crop_df.columns.str.strip()

# Clean and convert production column
crop_df["Production (MT)"] = (
    crop_df["Production (MT)"]
    .astype(str)
    .str.strip()
    .replace(["", " ", "NA", "NaN", "nan", "-", "--", "None"], "0", regex=True)
    .str.replace(",", "", regex=False)
)

crop_df["Production (MT)"] = pd.to_numeric(crop_df["Production (MT)"], errors="coerce").fillna(0)
print("✅ Crop data loaded:", crop_df.shape)

# Load Rainfall Data
print("🌧️ Loading rainfall data...")
rain_path = os.path.join(RAW_DIR, "Sub_Division_IMD_2017.csv")
rain_df = pd.read_csv(rain_path)
rain_df.columns = rain_df.columns.str.strip()
print("✅ Rainfall data loaded:", rain_df.shape)

# Save to SQLite
print("💾 Writing to SQLite database...")
conn = sqlite3.connect(DB_PATH)
crop_df.to_sql("crop_production", conn, if_exists="replace", index=False)
rain_df.to_sql("rainfall_data", conn, if_exists="replace", index=False)
conn.close()

print("✅ ETL complete! Database updated.")
