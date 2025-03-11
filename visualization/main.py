import streamlit as st
from about import render_about
from relatorio import render_relatorio
from notebook import render_notebook

st.set_page_config(layout='wide', page_title='Fraud_detect')



menu = st.sidebar.radio(
    'Menu', 
    options=["About 🔍", "Relatorio 📊", "Notebook 📓"]
)

menu_functions= {
    "About 🔍": render_about,
    "Relatorio 📊": render_relatorio,
    "Notebook 📓": render_notebook
}

menu_functions[menu]()