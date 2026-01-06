import streamlit as st
from PIL import Image
import time
from styles import apply_styles, render_header
from engine import run_smart_audit

# 1. Инициализация защиты и памяти
if 'last_request' not in st.session_state:
    st.session_state.last_request = 0

# 2. Применяем наш премиальный дизайн
apply_styles()

# 3. Отрисовываем Логотип и "Плюшку" (Верни 14%)
render_header()

# 4. Выбор режима (под капотом модели 2026 года)
# Используем пустую строку для label, так как дизайн минималистичный
quality = st.select_slider(
    "",
    options=["Молния", "Профи", "Сенсей"],
    value="Профи",
    help="Выберите глубину анализа"
)

# 5. Зона загрузки
uploaded_file = st.file_uploader("", type=['png', 'jpg', 'jpeg'], label_visibility="collapsed")

if uploaded_file:
    # Отображаем превью (адаптировано под Mini App)
    img = Image.open(uploaded_file)
    with st.expander("📄 Посмотреть загруженный документ"):
        st.image(img, use_container_width=True)

    if st.button("РАСКРЫТЬ ПЕРЕПЛАТУ"):
        # ПРОВЕРКА RATE LIMIT (Защита от спама и траты токенов)
        current_time = time.time()
        cooldown = 15 # секунд
        
        if current_time - st.session_state.last_request < cooldown:
            wait_time = int(cooldown - (current_time - st.session_state.last_request))
            st.error(f"🛡️ Защита VALI: Подождите {wait_time} сек. перед следующим анализом.")
        else:
            with st.spinner('СВЕРЯЕМ ЦЕНЫ С БАЗОЙ 2026...'):
                st.session_state.last_request = current_time
                
                # Запуск ИИ-логики
                res_text, qr_code, ref_url = run_smart_audit(img, quality)
                
                st.markdown("---")
                # Вывод результата (Тизер)
                if "ОШИБКА" in res_text:
                    st.warning(res_text)
                else:
                    st.success(res_text)
                    
                    # Блок рефералки и перехода в бота
                    st.markdown(f"""
                        <div style="border: 1px solid #D4AF37; padding: 20px; border-radius: 20px; text-align: center; background: rgba(212,175,55,0.05);">
                            <p style="color: #D4AF37; font-weight: bold; margin-bottom: 10px;">📊 ПОЛНЫЙ ОТЧЕТ И PDF ГОТОВЫ</p>
                            <img src="{qr_code}" width="150" style="border-radius: 10px; margin-bottom: 10px;"><br>
                            <a href="{ref_url}" target="_blank">
                                <button style="width: 100%; background: #D4AF37; color: black; border: none; padding: 10px; border-radius: 10px; font-weight: bold; cursor: pointer;">
                                    ОТКРЫТЬ В TELEGRAM
                                </button>
                            </a>
                            <p style="font-size: 0.8rem; margin-top: 10px; opacity: 0.6;">Сканируй QR коллегой, чтобы получить +3 аудита "Сенсей"</p>
                        </div>
                    """, unsafe_allow_html=True)

# 6. Футер (максимально незаметный)
st.caption("VALI v3.0 | Protected by Gemini 2.5 Security")
