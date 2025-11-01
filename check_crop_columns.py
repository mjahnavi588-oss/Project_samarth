import sqlite3

conn = sqlite3.connect("data/samarth.db")
cursor = conn.cursor()

print("🌾 Columns in crop_production table:")
cursor.execute("PRAGMA table_info(crop_production);")
for col in cursor.fetchall():
    print(col[1])

conn.close()

