import streamlit as st
import sqlite3
import pandas as pd

# --- Title ---
st.title("🌾 Samarth Q&A Assistant")
st.write("Ask questions about crop production or rainfall patterns in India (2017–18).")

# --- Connect to DB ---
conn = sqlite3.connect("data/samarth.db")

# --- Helper Functions ---
def get_top_crops(state=None):
    if state:
        query = f"""
        SELECT [Crops] AS crop_name, SUM([Production (MT)]) AS production
        FROM crop_production
        WHERE lower([Types of Crops]) LIKE '%{state.lower()}%'
        GROUP BY [Crops]
        ORDER BY production DESC
        LIMIT 5;
        """
    else:
        query = """
        SELECT [Crops] AS crop_name, SUM([Production (MT)]) AS production
        FROM crop_production
        GROUP BY [Crops]
        ORDER BY production DESC
        LIMIT 5;
        """
    return pd.read_sql(query, conn)

def get_top_rainfall_regions():
    query = """
    SELECT SUBDIVISION AS region, AVG(ANNUAL) AS avg_rainfall
    FROM rainfall_data
    GROUP BY SUBDIVISION
    ORDER BY avg_rainfall DESC
    LIMIT 5;
    """
    return pd.read_sql(query, conn)

# --- Input box ---
user_question = st.text_input("💬 Ask your question:")

if st.button("Ask"):
    if not user_question.strip():
        st.warning("Please type a question.")
    else:
        q = user_question.lower()

        # --- Crop-related questions ---
        if "crop" in q or "production" in q:
            st.subheader("🌾 Top crops by production")
            df = get_top_crops()
            st.dataframe(df)

        # --- Rainfall-related questions ---
        elif "rain" in q or "region" in q:
            st.subheader("🌧️ Top rainfall regions")
            df = get_top_rainfall_regions()
            st.dataframe(df)

        # --- Fallback ---
        else:
            st.info("I can answer questions about crop production or rainfall patterns!")

conn.close()
