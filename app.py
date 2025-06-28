import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px
import time

from insights import generate_insight

# --- Page Config ---
st.set_page_config(page_title="MySQL Sales Dashboard", layout="wide")
st.title("📊 Real-Time MySQL Sales Dashboard")
st.write("⏱️ Auto-refresh every 60 seconds. Click the button below to refresh manually.")

# --- Manual Refresh Button ---
if st.button("🔄 Refresh Now"):
    st.rerun()

# --- MySQL Connection ---
def get_data():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Replace if you have a MySQL password
        database="sales_dashboard_mysql"
    )
    query = "SELECT * FROM sales_data ORDER BY sale_time DESC LIMIT 100"
    return pd.read_sql(query, con=connection)

# --- Load and Display Data ---
df = get_data()

# --- Show AI-powered Insight ---
st.subheader("🧠 Auto-Generated Sales Insight")
st.markdown(generate_insight(df))

st.subheader("🧾 Recent Sales Records")
st.dataframe(df)

# --- Sales by Product ---
st.subheader("📦 Sales by Product")
fig1 = px.bar(df, x='product', y='total_sales', color='region', title="Total Sales by Product")
st.plotly_chart(fig1, use_container_width=True)

# --- Sales by Region ---
st.subheader("🌎 Sales by Region")
region_data = df.groupby("region")["total_sales"].sum().reset_index()
fig2 = px.pie(region_data, names="region", values="total_sales", title="Sales Distribution by Region")
st.plotly_chart(fig2, use_container_width=True)

# --- Auto Refresh Delay ---
time.sleep(60)
st.rerun()
