import streamlit as st
import sqlite3
import pandas as pd

from aggrid_style import show_streamlit_style_grid

st.set_page_config(page_title="Inventory Dashboard", layout="wide")
st.title("Editable Inventory Dashboard")


# 🔹 Paths
EXCEL_OUTPUT_PATH = r"C:\Users\OWNER\Desktop\Python\My_Inventory\Updated_Inventory.xlsx"

# 🔹 Database connection
conn = sqlite3.connect("inventory.db", check_same_thread=False)

# 🔹 Load data from DB
df = pd.read_sql("SELECT * FROM inventory", conn)

# 🔹 Editable dashboard
edited_df = show_streamlit_style_grid(df)

# 🔹 Save button (DB + Excel)
if st.button("💾 Save Changes"):
    # 1️⃣ Save to SQLite (MASTER)
    edited_df.to_sql("inventory", conn, if_exists="replace", index=False)

    # 2️⃣ ALSO save to Excel
    edited_df.to_excel(EXCEL_OUTPUT_PATH, index=False)

    st.success("Dashboard, Database & Excel updated successfully")
