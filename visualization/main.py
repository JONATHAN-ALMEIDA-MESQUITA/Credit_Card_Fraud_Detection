"""
Main application file for the Credit Card Fraud Detection visualization dashboard.
This module serves as the entry point for the Streamlit application, handling the
main menu and navigation between different sections.
"""

import streamlit as st
from about import render_about
from relatorio import render_relatorio
from notebook import render_notebook

# Constants
MENU_OPTIONS = {
    "About 🔍": render_about,
    "Report 📊": render_relatorio,
    "Notebook 📓": render_notebook
}

# Page configuration
st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="auto"
)

# Add title to the sidebar
st.sidebar.title("Navigation")

# Menu selection
selected_menu = st.sidebar.radio(
    'Menu', 
    options=list(MENU_OPTIONS.keys())
)

# Main content rendering with error handling
try:
    MENU_OPTIONS[selected_menu]()
except Exception as e:
    st.error(f"An error occurred while rendering the {selected_menu} page: {str(e)}")
    st.error("Please try refreshing the page or contact support if the problem persists.")