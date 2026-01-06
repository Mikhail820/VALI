import streamlit as st
from PIL import Image
import time
import os
from styles import apply_styles, render_header, render_disclaimer
from engine import run_smart_audit
from database import init_db, is_user_subscribed

# 1. Настройка страницы и SEO
st.set_page_config(
    page_title="VALI | Smart Audit",
    page_icon="💎",
    layout="centered"
)

# Мета-теги для SEO
st.markdown("""
    <head>
        <meta name="description" content="VALI - автономный аудит инвойсов.">
        <meta name="keywords" content="аудит, инвойс, Китай, Gemini">
    </head>
""", unsafe_allow_html=True)

# 2. Инициализация базы и стилей
init_db()
apply_styles()
render_header()

# 3. Получение user_id из URL (передается ботом)
query_params = st.query_params
user_id = query_params.get("user_id")

# Вспомогательная переменная в сессии для тестов (если зашли без Telegram)
if 'test_mode' not in st.session_state:
    st.session_state.test_mode = False

# 4. Интерфейс загрузки
uploaded_file = st.file_uploader("", type=['png', 'jpg', 'jpeg'], label_visibility="collapsed")

if uploaded_file:
    img = Image.open(uploaded_file)
    with st.expander("📄 Посмотреть документ"):
        st.image(img, use_container_width=True)

    # ГЛАВНАЯ КНОПКА (Нейтральное название)
    if st.button("ПРОВЕРИТЬ ИНВОЙС"):
        
        # ШАГ 1: Проверка на вшивость (есть ли user_id)
        if not user_id and not st.session_state.test_mode:
            st.error("⚠️ Ошибка авторизации. Пожалуйста, запустите приложение через Telegram-бота.")
        else:
            # ШАГ 2: Проверка подписки в базе данных
            # (Функция is_user_subscribed должна реально проверять статус в vali_users.db)
            subscribed = is_user_subscribed(user_id) if user_id else st.session_state.test_mode
            
            if not subscribed:
                # БЛОКИРОВКА: ИИ не вызывается, токены не тратятся
                st.warning("📊 ОТЧЕТ СФОРМИРОВАН, НО ЗАБЛОКИРОВАН")
                st.markdown("""
                    <div style="background: rgba(212,175,55,0.05); padding: 20px; border-radius: 15px; border: 1px solid #D4AF37; text-align: center;">
                        <p style="margin-bottom: 15px;">Для получения доступа к результатам анализа необходимо подписаться на наш официальный канал.</p>
                        <a href="https://t.me/твой_канал" target="_blank" style="text-decoration: none;">
                            <div style="background: #D4AF37; color: black; padding: 12px; border-radius: 10px; font-weight: bold; cursor: pointer;">
                                🔗 ПОДПИСАТЬСЯ И ПОЛУЧИТЬ ДОСТУП
                            </div>
                        </a>
                    </div>
                """, unsafe_allow_html=True)
                
                # Кнопка для ручной проверки (для отладки)
                if st.button("Я подписался, обновить"):
                    st.rerun()
            else:
                # ШАГ 3: Запуск ИИ только для «своих»
                current_time = time.time()
                if 'last_req' not in st.session_state: st.session_state.last_req = 0
                
                if current_time - st.session_state.last_req < 15:
                    st.toast("🛡️ Подождите 15 секунд...")
                else:
                    with st.spinner('СИНХРОНИЗАЦИЯ С БАЗОЙ...'):
                        st.session_state.last_req = current_time
                        res_text, bot_url = run_smart_audit(img)
                        
                        st.markdown("---")
                        st.success(res_text)
                        
                        # Вместо некликабельного QR — кнопка возврата в бот за PDF/подробностями
                        st.link_button("ПОЛУЧИТЬ ПОЛНЫЙ ОТЧЕТ В TG", bot_url)

# 5. Футер с дисклеймером
render_disclaimer()
