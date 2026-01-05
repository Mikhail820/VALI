import google.generativeai as genai
import streamlit as st

def get_vali_response(image, quality_mode):
    # Карта моделей 2026 года
    models = {
        "Молния": "gemini-2.5-flash-lite", # Скорость и дешевые токены
        "Профи": "gemini-2.0-flash",       # Баланс и точность таблиц
        "Сенсей": "gemini-2.5-pro"         # Максимальный интеллект
    }
    
    selected_model = models.get(quality_mode, "gemini-2.0-flash")
    
    genai.configure(api_key=st.secrets["GEMINI_KEY"])
    model = genai.GenerativeModel(selected_model)
    
    prompt = f"Ты — VALI AUDIT. Проведи анализ инвойса в режиме {quality_mode}. Найди ошибки. Ответь на русском."
    
    response = model.generate_content([prompt, image])
    return response.text, selected_model
