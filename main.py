
from util import print_multi_table
import pandas
import streamlit as st
print_multi_table(5,20)

data= pandas.read_csv("products.csv")

st.title("Dashboard")

st.header("Product Data")
st.write("This application is a simple dashboard to show data")
st.subheader("This is product data from products")
st.write(data)

coll1, col2, col3 = st.columns(3)
with coll1:
    st.metric("Sales", "1200", "12%")
with col2:
    st.metric("Revenue", "56000", "5%")
with col3:
    st.metric("Profit", "32000", "3%")
st.line_chart(data["sales"]) 

