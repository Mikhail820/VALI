import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        #MainMenu {visibility: hidden;} header {visibility: hidden;} footer {visibility: hidden;}
        .stApp { background-color: #0E1117; color: #FFFFFF; font-family: 'Inter', sans-serif; }
        .magic-box {
            background: linear-gradient(145deg, rgba(212,175,55,0.1) 0%, rgba(0,0,0,0) 100%);
            border: 1px solid rgba(212,175,55,0.4);
            padding: 25px 20px;
            border-radius: 24px;
            text-align: center;
            margin: 20px;
            animation: pulse-border 3s infinite;
        }
        @keyframes pulse-border {
            0% { border-color: rgba(212,175,55,0.4); }
            50% { border-color: rgba(212,175,55,1); }
            100% { border-color: rgba(212,175,55,0.4); }
        }
        .highlight-title { color: #D4AF37; font-size: 1.8rem; font-weight: 800; text-transform: uppercase; }
        </style>
    """, unsafe_allow_html=True)

def render_header():
    st.markdown('<div style="text-align:center; padding: 40px 0 10px 0;">', unsafe_allow_html=True)
    st.markdown("<h1 style='color:#D4AF37;'>💎 VALI</h1>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
        <div class="magic-box">
            <span class="highlight-title">Верни свои 16.8%</span>
            <p style="opacity: 0.9;">VALI найдет скрытые наценки в инвойсах за 15 секунд.</p>
        </div>
    """, unsafe_allow_html=True)
