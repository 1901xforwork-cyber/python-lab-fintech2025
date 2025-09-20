import streamlit as st

st.set_page_config(
    page_title="Rectangle page",
    layout="wide"
)
st.title("Rectangle Area Calculator")
width = st.number_input("Enter width")
height = st.number_input("Enter height")
if st.button("Calculate Area"):
     st.write(f'area = {width * height}')