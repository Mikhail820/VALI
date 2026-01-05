import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# 1. Настройка стиля VALI (Золото на темном)
st.set_page_config(
    page_title="VALI Smart Audit",
    page_icon="💎",
    layout="centered"
)

st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: #D4AF37;
    }
    .stMarkdown h1, h2, h3 {
        color: #D4AF37 !important;
        text-align: center;
    }
    .stButton>button {
        width: 100%;
        background-color: #D4AF37;
        color: black;
        border-radius: 12px;
        border: none;
        height: 3em;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #B8962E;
        color: white;
    }
    /* Стилизация загрузчика файлов */
    .stFileUploader {
        border: 1px dashed #D4AF37;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Подключение ИИ (Ключ берем из секретов Streamlit)
try:
    genai.configure(api_key=st.secrets["GEMINI_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("Ошибка конфигурации. Проверьте GEMINI_KEY в Secrets.")

# 3. Интерфейс приложения
st.title("💎 VALI | SMART AUDIT")
st.markdown("### Искусственный интеллект для проверки ваших инвойсов")
st.write("---")

uploaded_file = st.file_uploader("Загрузите фото инвойса или накладной", type=['png', 'jpg', 'jpeg'])

if uploaded_file:
    # Показываем превью
    image = Image.open(uploaded_file)
    st.image(image, caption='Документ загружен', use_container_width=True)
    
    # Кнопка запуска анализа
    if st.button("ЗАПУСТИТЬ АУДИТ СЕНСЕЕМ"):
        with st.spinner('Сенсей анализирует данные...'):
            try:
                # Промпт-инструкция для ИИ
                prompt = """
                Ты — VALI, профессиональный AI-аудитор закупок из Китая. 
                Твоя задача:
                1. Проверить корректность математических вычислений (цена * количество = итог).
                2. Оценить адекватность цен. Если цена кажется завышенной для опта из Китая, укажи на это.
                3. Проверить логистические данные, если они есть.
                
                Выдай ответ в формате:
                ✅ МАТЕМАТИКА: (ОК или Найдена ошибка)
                💰 ЦЕНЫ: (Рыночные или Завышены)
                🛠 ВЕРДИКТ: (Краткий совет пользователю)
                
                Отвечай строго на русском языке, вежливо, но профессионально.
                """
                
                response = model.generate_content([prompt, image])
                
                st.write("---")
                st.markdown("### РЕЗУЛЬТАТ ПРОВЕРКИ:")
                st.success(response.text)
                
            except Exception as e:
                st.error(f"Произошла ошибка при анализе: {e}")

else:
    st.info("Ожидаю файл для анализа...")

st.markdown("---")
st.caption("VALI v1.0 | Защищено технологиями ИИ")
