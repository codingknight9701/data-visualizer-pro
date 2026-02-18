import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Data Visualizer", layout="wide")
st.title("Interactive Data Visualizer Dashboard")

# 2. Upload Data
uploaded_file = st.file_uploader("Upload your CSV dataset", type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview")
    st.dataframe(df.head())

    # 3. Sidebar Filters
    st.sidebar.header("Visualization Settings")
    columns = df.columns.tolist()
    
    x_axis = st.sidebar.selectbox("Select X-Axis", columns)
    y_axis = st.sidebar.selectbox("Select Y-Axis", columns)

    # 4. Generate Charts
    st.write("### Interactive Bar Chart")
    st.plotly_chart(px.bar(df, x=x_axis, y=y_axis), use_container_width=True)

    st.write("### Interactive Scatter Plot")
    st.plotly_chart(px.scatter(df, x=x_axis, y=y_axis), use_container_width=True)
else:
    st.info("Please upload a CSV file to generate visualizations.")