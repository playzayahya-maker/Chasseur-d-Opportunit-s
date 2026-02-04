import streamlit as st
from groq import Groq
import hunter

st.set_page_config(page_title="IKON PRO", layout="wide")

# CSS dyal l-Menu w l-Interface
st.markdown("""
    <style>
    .stApp { background-color: #F8F9FA; }
    .stSidebar { background-color: #111827 !important; }
    .stButton>button { 
        background: linear-gradient(90deg, #4F46E5 0%, #7C3AED 100%); 
        color: white; border-radius: 8px; font-weight: bold; width: 100%; border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 📍 API KEY (Baddelha hna!)
MY_API_KEY = "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"

with st.sidebar:
    st.markdown("<h2 style='color: #7C3AED;'>🚀 IKON PRO</h2>", unsafe_allow_html=True)
    st.write("---")
    choice = st.radio("SÉLECTIONNER AGENT:", ["📄 CV BOOSTER", "🕵️ OPPORTUNITY HUNTER"])
    st.write("---")
    st.caption("AI Market Intelligence v3.0")

if choice == "📄 CV BOOSTER":
    st.title("📄 AI CV Optimization")
    cv_input = st.text_area("Coller votre CV ici:", height=200)
    job_title = st.text_input("Poste Visé:")
    if st.button("OPTIMISER CV"):
        client = Groq(api_key=MY_API_KEY)
        res = client.chat.completions.create(model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": f"Optimize CV for {job_title}: {cv_input}"}])
        st.markdown(res.choices[0].message.content)

elif choice == "🕵️ OPPORTUNITY HUNTER":
    hunter.run_hunter_agent(MY_API_KEY)
