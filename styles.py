import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        /* 1. ПОЛНАЯ ЗАЧИСТКА ИНТЕРФЕЙСА */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .viewerBadge_container__1QS13 {display: none !important;}
        button[title="View source"] {display: none;}
        
        /* 2. ПРЕМИАЛЬНЫЙ ТЕМНЫЙ ФОН */
        .stApp {
            background-color: #0E1117;
            color: #FFFFFF;
            font-family: 'Inter', sans-serif;
        }

        /* 3. ЦЕНТРИРОВАННЫЙ ЛОГОТИП */
        .logo-container {
            display: flex;
            justify-content: center;
            padding-top: 40px;
            margin-bottom: 10px;
        }

        /* 4. "ПЛЮШКА" (THE HOOK) С АНИМАЦИЕЙ */
        .magic-box {
            background: linear-gradient(145deg, rgba(212,175,55,0.1) 0%, rgba(0,0,0,0) 100%);
            border: 1px solid rgba(212,175,55,0.4);
            padding: 25px 20px;
            border-radius: 24px;
            text-align: center;
            margin: 20px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.4);
            animation: pulse-border 3s infinite;
        }

        @keyframes pulse-border {
            0% { border-color: rgba(212,175,55,0.4); }
            50% { border-color: rgba(212,175,55,1); }
            100% { border-color: rgba(212,175,55,0.4); }
        }

        .highlight-title {
            color: #D4AF37;
            font-size: 1.8rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 2px;
            display: block;
            margin-bottom: 8px;
        }

        .promo-desc {
            font-size: 1rem;
            line-height: 1.4;
            opacity: 0.9;
        }

        /* 5. КНОПКИ И СЛАЙДЕРЫ */
        .stButton>button {
            width: 100%;
            background: linear-gradient(90deg, #D4AF37 0%, #B8860B 100%);
            color: #000000 !important;
            border-radius: 14px;
            font-weight: 700;
            height: 3.8em;
            border: none;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: all 0.3s;
        }
        
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(212,175,55,0.4);
        }

        /* Прячем стандартный заголовок uploader */
        .stFileUploader section {
            background-color: rgba(255,255,255,0.03);
            border: 1px dashed rgba(212,175,55,0.3);
            border-radius: 14px;
        }
        </style>
    """, unsafe_allow_html=True)

def render_header():
    # Логотип (замени на свой файл logo.png в корне)
    st.markdown('<div class="logo-container">', unsafe_allow_html=True)
    try:
        st.image("logo.png", width=140)
    except:
        st.markdown("<h1 style='color:#D4AF37; text-align:center;'>💎 VALI</h1>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Визуальный оффер
    st.markdown("""
        <div class="magic-box">
            <span class="highlight-title">Верни свои 14%</span>
            <p class="promo-desc">
                По статистике, 8 из 10 поставщиков завышают счета.<br>
                <b>VALI</b> найдет скрытые наценки за 15 секунд.
            </p>
        </div>
    """, unsafe_allow_html=True)
