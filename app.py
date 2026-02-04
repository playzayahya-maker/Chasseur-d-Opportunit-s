import streamlit as st
from groq import Groq
import hunter # Import dyal Agent 2

# 1. Configuration
st.set_page_config(page_title="IKON PRO AI", layout="wide", page_icon="🚀")

# 2. Design CSS Pro
st.markdown("""
    <style>
    .stApp { background-color: #F4F7F9; }
    .main-card { background: white; padding: 30px; border-radius: 12px; border-top: 10px solid #6366F1; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
    .stButton>button { background: linear-gradient(90deg, #6366F1 0%, #A855F7 100%); color: white; border: none; border-radius: 8px; font-weight: bold; height: 3.5em; width: 100%; }
    .stSidebar { background-color: #FFFFFF !important; border-right: 1px solid #E5E7EB; }
    </style>
    """, unsafe_allow_html=True)

# 📍 API KEY SETUP (HNA FIN T-7ET L-KEY DYALK)
MY_API_KEY = st.secrets.get("GROQ_API_KEY", "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")

# 3. Sidebar Menu
with st.sidebar:
    st.markdown("<h1 style='color: #6366F1;'>IKON PRO</h1>", unsafe_allow_html=True)
    st.write("---")
    choice = st.radio("SERVICE SELECTOR:", ["📄 AI CV BOOSTER", "🕵️ OPPORTUNITY HUNTER"])
    st.write("---")
    st.success("System: Active 🟢")

# 4. Routing
if choice == "📄 AI CV BOOSTER":
    st.markdown("<h1 style='color: #1F2937;'>CV Optimization Engine</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns([1.2, 1], gap="large")
    
    with col1:
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        uploaded = st.file_uploader("Upload Document (PDF/Image)", type=["pdf", "png", "jpg"])
        cv_text = st.text_area("Or Paste CV Content", height=300)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        target = st.text_input("Job Title", placeholder="e.g. Sales Manager")
        region = st.selectbox("Market", ["Canada", "Europe", "USA", "Gulf"])
        if st.button("REWRITE & DESIGN ✨"):
            if (cv_text or uploaded) and target:
                client = Groq(api_key=MY_API_KEY)
                with st.spinner("AI Magic in progress..."):
                    res = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[{"role": "user", "content": f"Optimize CV and write Cover Letter for {target} in {region}: {cv_text}"}]
                    )
                    st.session_state['cv_res'] = res.choices[0].message.content
                    st.balloons()

    if 'cv_res' in st.session_state:
        st.markdown("### ✨ GENERATED ASSETS")
        st.markdown(f'<div class="main-card">{st.session_state["cv_res"]}</div>', unsafe_allow_html=True)

elif choice == "🕵️ OPPORTUNITY HUNTER":
    # 5. Launch Agent 2
    hunter.run_hunter_agent(MY_API_KEY)
