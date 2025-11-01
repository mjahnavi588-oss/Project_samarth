import sqlite3
import pandas as pd

DB_PATH = "data/samarth.db"

def get_top_crops():
    conn = sqlite3.connect(DB_PATH)
    query = """
        SELECT 
            [Crops] AS crop_name, 
            SUM([Production (MT)]) AS production
        FROM crop_production
        GROUP BY [Crops]
        ORDER BY production DESC
        LIMIT 5;
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def get_average_rainfall():
    conn = sqlite3.connect(DB_PATH)
    query = """
        SELECT 
            [SUBDIVISION] AS region, 
            AVG([ANNUAL]) AS avg_rainfall
        FROM rainfall_data
        GROUP BY [SUBDIVISION]
        ORDER BY avg_rainfall DESC
        LIMIT 5;
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df

if __name__ == "__main__":
    print("🌾 Top crops by production:")
    print(get_top_crops())
    print("\n🌧️ Top rainfall regions:")
    print(get_average_rainfall())
