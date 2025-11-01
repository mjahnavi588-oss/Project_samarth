import sqlite3
conn = sqlite3.connect("data/samarth.db")
cursor = conn.cursor()
cursor.execute("PRAGMA table_info(rainfall_data);")
print("?? Columns in rainfall_data:")
for col in cursor.fetchall():
    print(col[1])
conn.close()
