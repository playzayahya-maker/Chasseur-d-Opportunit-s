import streamlit as st

# 1. Configuration dyal l-Hub
st.set_page_config(page_title="IKON PRO - AI Suite", layout="wide", page_icon="🚀")

# 2. Sidebar Navigation (Kima Screenshot 233)
with st.sidebar:
    st.markdown("<h1 style='color: #7C3AED;'>IKON PRO</h1>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("### 🧭 NAVIGATION")
    
    # Menu bach t-khetar l-Agent
    choice = st.radio("Select Service:", ["📄 CV Booster", "🕵️ Opportunity Hunter"])
    
    st.write("---")
    st.info("Agentic AI System v2.0\nStatus: Online 🟢")
    st.caption("by Darcot")

# 3. Routing Logic
if choice == "📄 CV Booster":
    # --- Hna kiy-ji l-code dyal Agent 1 (CV & Letter) ---
    st.title("Build Your Pro Package")
    st.write("Optimize your CV and generate a personalized cover letter.")
    
    # Hna tqder t-kopi l-logic dyal CV booster li qaddina qbila
    # (Uploader, Text Area, Generate Button, etc.)
    import cv_logic # Ila knti dayrha f fichi m3zoul
    st.warning("Agent 1 is active. Upload your document to start.")

elif choice == "🕵️ Opportunity Hunter":
    # --- Hna kiy-ji l-code dyal Agent 2 (The Hunter) ---
    # Bach t-khelli l-hunter i-bqa f dak l-style l-kħal, ghadi n-3ayto 3lih
    import hunter # Hada ghadi i-khdem l-fichie li yallah qaddina
