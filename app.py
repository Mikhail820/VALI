import streamlit as st
from PIL import Image
from engine import get_vali_response
from styles import apply_clean_style

apply_clean_style()

# Хедер (Логотип в углу)
col_l, col_r = st.columns([1, 4])
with col_l:
    try: st.image("logo.png", width=60)
    except: st.write("💎")
with col_r:
    st.markdown("<h2 style='margin-top: 5px;'>VALI AUDIT</h2>", unsafe_allow_html=True)

# Интерфейс
quality = st.select_slider("Качество:", options=["Молния", "Профи", "Сенсей"], value="Профи")
file = st.file_uploader("Загрузить", type=['png', 'jpg', 'jpeg'], label_visibility="collapsed")

if file and st.button("ЗАПУСТИТЬ АУДИТ"):
    with st.spinner('VALI анализирует...'):
        img = Image.open(file)
        text, model_used = get_vali_response(img, quality)
        st.success(text)
        st.caption(f"Использована модель: {model_used}")
