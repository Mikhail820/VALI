import streamlit as st

def apply_clean_style():
    st.markdown("""
        <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .viewerBadge_container__1QS13 {display: none !important;}
        button[title="View source"] {display: none;}
        .stApp { background-color: #0E1117; color: #D4AF37; }
        .block-container { padding-top: 1.5rem; }
        .stButton>button {
            width: 100%; background-color: #D4AF37; color: black;
            border-radius: 12px; font-weight: bold; border: none;
        }
        </style>
        """, unsafe_allow_html=True)
