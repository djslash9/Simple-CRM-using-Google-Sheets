# Contents of ~/my_app/main_page.py
import streamlit as st

st.markdown("# Login Page 🎈")
st.sidebar.markdown("# Main page 🎈")

title = st.text_input('User Name', 'User')
title = st.text_input('Password', 'Password')