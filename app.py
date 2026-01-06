import streamlit as st
from PIL import Image
import time
from styles import apply_styles, render_header
from engine import run_smart_audit

# SEO Конфигурация
st.set_page_config(page_title="VALI | Аудит 16.8%", page_icon="💎", layout="centered")

st.markdown("""
    <head>
        <meta name="description" content="VALI - умный ИИ-аудит инвойсов. Верни свои 16.8% переплат.">
        <meta name="keywords" content="аудит, китай, инвойс, карго, Gemini 2.5">
    </head>
""", unsafe_allow_html=True)

if 'last_request' not in st.session_state:
    st.session_state.last_request = 0

apply_styles()
render_header()

quality = st.select_slider("", options=["Молния", "Профи", "Сенсей"], value="Профи") #
uploaded_file = st.file_uploader("", type=['png', 'jpg', 'jpeg'], label_visibility="collapsed")

if uploaded_file:
    img = Image.open(uploaded_file)
    if st.button("РАСКРЫТЬ ПЕРЕПЛАТУ"):
        current_time = time.time()
        if current_time - st.session_state.last_request < 15:
            st.error(f"🛡️ Защита: Подождите {int(15 - (current_time - st.session_state.last_request))} сек.")
        else:
            with st.spinner('АНАЛИЗ ПО СТАНДАРТУ 16.8%...'):
                st.session_state.last_request = current_time
                res_text, qr_code, ref_url = run_smart_audit(img, quality)
                
                if "🛡️" in res_text:
                    st.warning(res_text)
                else:
                    st.success(res_text)
                    st.image(qr_code, width=150, caption="Сканируй для полного отчета")
