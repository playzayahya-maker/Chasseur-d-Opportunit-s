import streamlit as st
from groq import Groq
import hunter  # Ghadi n-3aytou l-Agent Hunter hna

# 1. Config dyal Page
st.set_page_config(page_title="IKON PRO AI", layout="wide", page_icon="🚀")

# 2. API KEY SETUP
# Kat-jibha men Secrets dyal Streamlit Cloud (Smiytha: GROQ_API_KEY)
MY_API_KEY = st.secrets.get("GROQ_API_KEY", "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")

# 3. Sidebar Design (Professional Dark)
with st.sidebar:
    st.markdown("<h1 style='color: #7C3AED;'>IKON PRO</h1>", unsafe_allow_html=True)
    st.write("---")
    choice = st.radio("SELECT AGENT:", ["🕵️ OPPORTUNITY HUNTER", "📄 CV BOOSTER"])
    st.write("---")
    st.success("System: Operational 🟢")
    st.caption("v3.0 - OSINT Intelligence")

# 4. Logic dyal Navigation
if choice == "🕵️ OPPORTUNITY HUNTER":
    hunter.run_hunter_agent(MY_API_KEY)
else:
    st.title("📄 CV Booster")
    st.info("Agent CV Booster ghadi i-koun kheddam hna. D-aba rkkéz m3aya 3la l-Hunter.")
