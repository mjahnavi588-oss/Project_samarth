import sqlite3
import pandas as pd

conn = sqlite3.connect("data/samarth.db")

print("🧾 Preview of crop_production table:")
df = pd.read_sql("SELECT * FROM crop_production LIMIT 10;", conn)
print(df)

print("\n🔍 Checking data types:")
print(df.dtypes)

conn.close()
