import streamlit as st

def apply_clean_style():
    st.set_page_config(page_title="VALI AUDIT", page_icon="💎", layout="centered")
    
    st.markdown("""
        <style>
        /* Полная зачистка элементов Streamlit */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .viewerBadge_container__1QS13 {display: none !important;}
        button[title="View source"] {display: none;}
        
        /* Фон и отступы */
        .stApp { background-color: #0E1117; }
        .block-container { padding-top: 1rem; padding-bottom: 0rem; }
        
        /* Кнопка */
        .stButton>button {
            width: 100%; background-color: #D4AF37; color: black;
            border-radius: 12px; font-weight: bold; height: 3.8em; border: none;
        }
        
        /* Слайдер и текст */
        div[data-testid="stWidgetLabel"] { color: #D4AF37 !important; font-weight: bold; }
        </style>
        """, unsafe_allow_html=True)
