import streamlit as st
from groq import Groq

# 1. Config dyal l-page
st.set_page_config(page_title="IKON PRO - AI Suite", layout="wide", page_icon="🚀")

# 2. CSS Style (Professional Blue/Purple)
st.markdown("""
    <style>
    .stApp { background-color: #F8F9FA; }
    .doc-container {
        background-color: white; padding: 40px; border-radius: 4px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        border-top: 20px solid #3149A1; margin-top: 20px;
    }
    .stButton>button { background-color: #7C3AED; color: white; border-radius: 8px; font-weight: bold; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Navigation
with st.sidebar:
    st.markdown("<h1 style='color: #7C3AED;'>IKON PRO</h1>", unsafe_allow_html=True)
    st.write("---")
    choice = st.radio("Select Service:", ["📄 CV Booster", "🕵️ Opportunity Hunter"])
    st.write("---")
    st.info("Status: Online 🟢")

# 📍 API KEY (Fetch from Secrets for security)
MY_API_KEY = st.secrets.get("GROQ_API_KEY", "YOUR_KEY_HERE")

# 4. Routing Logic
if choice == "📄 CV Booster":
    st.title("Build Your Pro Package")
    col_l, col_r = st.columns([1.2, 1], gap="large")
    
    with col_l:
        uploaded_file = st.file_uploader("📤 Upload CV (PDF, PNG, JPG)", type=["pdf", "png", "jpg", "jpeg"])
        cv_manual = st.text_area("Or paste CV details manually", height=250)
    
    with col_r:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        job_target = st.text_input("Target Job Title")
        region = st.selectbox("Target Region", ["Canada", "Europe", "USA", "Gulf"])
        
        if st.button("Generate Pro CV & Letter ✨"):
            if (cv_manual or uploaded_file) and job_target:
                client = Groq(api_key=MY_API_KEY)
                with st.spinner("AI is styling your documents..."):
                    # Agent 1: CV Optimization
                    res_cv = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[{"role": "user", "content": f"Optimize this CV for {job_target} in {region}. Use Markdown. Content: {cv_manual}"}]
                    )
                    st.session_state['cv_final'] = res_cv.choices[0].message.content
                    
                    # Agent 1: Cover Letter
                    res_cl = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[{"role": "user", "content": f"Write a professional cover letter for {job_target}. Extract the name from: {cv_manual}"}]
                    )
                    st.session_state['cl_final'] = res_cl.choices[0].message.content

    if 'cv_final' in st.session_state:
        tab1, tab2 = st.tabs(["📄 Styled CV", "✉️ Cover Letter"])
        with tab1:
            st.markdown(f'<div class="doc-container">{st.session_state["cv_final"]}</div>', unsafe_allow_html=True)
        with tab2:
            st.markdown(f'<div class="doc-container">{st.session_state["cl_final"]}</div>', unsafe_allow_html=True)

elif choice == "🕵️ Opportunity Hunter":
    # 5. Routing to Hunter Agent
    import hunter
    hunter.run_hunter_agent(MY_API_KEY)
