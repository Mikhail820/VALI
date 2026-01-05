import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# 1. Настройка стиля VALI (Премиальный темный интерфейс)
st.set_page_config(
    page_title="VALI Smart Audit",
    page_icon="💎",
    layout="centered"
)

st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #D4AF37; }
    .stMarkdown h1, h2, h3 { color: #D4AF37 !important; text-align: center; }
    .stButton>button {
        width: 100%;
        background-color: #D4AF37;
        color: black;
        border-radius: 12px;
        font-weight: bold;
        height: 3em;
        border: none;
    }
    .stRadio > label { color: #D4AF37 !important; font-weight: bold; }
    div[data-testid="stExpander"] { border: 1px solid #D4AF37; }
    </style>
    """, unsafe_allow_html=True)

# 2. Логика выбора моделей Gemini 2.5
# Подключаем API ключ из секретов
try:
    API_KEY = st.secrets["GEMINI_KEY"]
    genai.configure(api_key=API_KEY)
except:
    st.error("Критическая ошибка: GEMINI_KEY не найден в Secrets.")

# Интерфейс выбора тарифа
st.title("💎 VALI | SMART AUDIT")
st.markdown("### Выберите уровень интеллекта для проверки")

# Маппинг моделей на основе актуальной линейки 2026 года
tier = st.radio(
    "Режим аудита:",
    ["Стандарт (2.5 Flash-Lite)", "Профи (2.5 Flash)", "Сенсей (2.5 Pro)"],
    index=1,
    help="Lite — быстро и дешево, Pro — максимальная точность для сложных документов."
)

model_map = {
    "Стандарт (2.5 Flash-Lite)": "gemini-2.5-flash-lite",
    "Профи (2.5 Flash)": "gemini-2.5-flash",
    "Сенсей (2.5 Pro)": "gemini-2.5-pro"
}

selected_model_id = model_map[tier]

# 3. Загрузка и анализ
uploaded_file = st.file_uploader("Загрузите фото инвойса (JPG, PNG)", type=['png', 'jpg', 'jpeg'])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Документ готов к анализу', use_container_width=True)
    
    if st.button(f"ЗАПУСТИТЬ АУДИТ ({tier})"):
        with st.spinner(f'Модель {selected_model_id} анализирует данные...'):
            try:
                # Инициализация выбранной модели
                model = genai.GenerativeModel(selected_model_id)
                
                # Промпт для профессионального аудита
                prompt = """
                Ты — VALI, ведущий AI-аудитор по закупкам. 
                Проанализируй этот документ:
                1. Перепроверь математику (Цена x Кол-во).
                2. Оцени адекватность цен для оптового рынка.
                3. Найди скрытые наценки или странные позиции.
                
                Ответь в стиле:
                ✅ ИТОГ МАТЕМАТИКИ: 
                💰 АНАЛИЗ ЦЕН: 
                ⚠️ РИСКИ: 
                💡 СОВЕТ:
                Отвечай на русском языке.
                """
                
                response = model.generate_content([prompt, image])
                
                st.write("---")
                st.markdown(f"### Вердикт от {selected_model_id}:")
                st.success(response.text)
                
            except Exception as e:
                st.error(f"Ошибка модели: {e}")

st.write("---")
st.caption("VALI v2.5 | Работает на базе Google Gemini 2.5 Next-Gen")