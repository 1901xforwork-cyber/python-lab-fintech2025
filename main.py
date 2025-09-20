
from util import print_multi_table
import pandas as pd
import streamlit as st
print_multi_table(5,20)

if 'username' in st.session_state:
        st.write(f"Hello {st.session_state['username']}")
else:   
       st.info("Please set your name in Setting page")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is None:
    st.write("Please upload a file")
else:
    data = pd.read_csv(uploaded_file)

    st.title("Dashboard")



    st.header("Product Data")
    st.write("This application is a simple dashboard to show data")
    st.subheader("This is product data from products")
    if st.button("Show table"):
        st.line_chart(data["sales"]) 
        st.write(data)

    coll1, col2, col3 = st.columns(3)
    with coll1:
        st.metric("Sales", "1200", "12%")
    with col2:
        st.metric("Revenue", "56000", "5%")
    with col3:
        st.metric("Profit", "32000", "3%")
    name = st.text_input("Enter your name")
    st.write(name)
