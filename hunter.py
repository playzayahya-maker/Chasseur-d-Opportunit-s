import streamlit as st
from groq import Groq

def run_hunter_agent(api_key):
    # CSS Cyberpunk Design (Hsen mn Screenshot 236)
    st.markdown("""
        <style>
        .stApp { background-color: #0A0F14; color: #00FF9D; }
        .cyber-card { background: #111827; border: 1px solid #00FF9D; padding: 25px; border-radius: 10px; border-left: 6px solid #00FF9D; margin-bottom: 20px; }
        .email-box { background: rgba(239, 68, 68, 0.1); border: 1px solid #EF4444; padding: 15px; border-radius: 6px; margin-top: 15px; }
        .stTextInput>div>div>input { background-color: #1F2937 !important; color: white !important; border: 1px solid #00FF9D !important; }
        </style>
        """, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center; color: #00FF9D;'>🕵️ OPPORTUNITY HUNTER PRO</h1>", unsafe_allow_html=True)
    
    c1, c2 = st.columns([3, 1])
    with c1:
        job = st.text_input("🔍 SCAN JOB TITLE", placeholder="e.g. Truck Driver, Nurse...")
    with c2:
        loc = st.selectbox("REGION", ["Canada", "Germany", "France", "Spain"])

    if st.button("INITIALIZE DEEP SCAN ⚡"):
        if job:
            client = Groq(api_key=api_key)
            with st.status("Accessing Global Databases...", expanded=True):
                # Prompt bach i-jbed l-email dyal l-Directeur s7i7
                prompt = f"""
                Act as a Headhunter. Find 3 companies for {job} in {loc}. 
                For each, provide: Company, Location, and the professional email format for the HR DIRECTOR (Decision Maker).
                Format as HTML:
                <div class='cyber-card'>
                    <h2 style='color: white;'>🏢 COMPANY_NAME</h2>
                    <p>📍 Location: {loc}</p>
                    <div class='email-box'>
                        <b style='color: #EF4444;'>🎯 DIRECT DIRECTOR EMAIL:</b><br>
                        <code style='color: white; font-size: 18px;'>first.last@company.com</code>
                    </div>
                </div>
                """
                res = client.chat.completions.create(model="llama-3.3-70b-versatile", messages=[{"role": "user", "content": prompt}])
                st.session_state['hunter_data'] = res.choices[0].message.content

    if 'hunter_data' in st.session_state:
        st.markdown(st.session_state['hunter_data'], unsafe_allow_html=True)
