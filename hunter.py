import streamlit as st
from groq import Groq
import os

# 1. Configuration dyal l-page
st.set_page_config(page_title="OPPS HUNTER - L'MOKHBIRE", layout="wide", page_icon="🕵️")

# 2. Design "Cyber Pro Max" (Custom CSS)
st.markdown("""
    <style>
    /* Background Matrix Dark */
    .stApp { background-color: #020617; color: #00FF9D; font-family: 'Segoe UI', sans-serif; }
    
    /* Hunter Card */
    .hunter-card { 
        background: linear-gradient(145deg, #0F172A, #1E293B); 
        border: 1px solid #334155; 
        padding: 30px; border-radius: 20px; margin-bottom: 25px; 
        border-left: 10px solid #00FF9D;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    
    /* Contact Box Styling */
    .contact-container { 
        display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); 
        gap: 15px; margin-top: 20px; 
    }
    
    .email-box { 
        background: rgba(15, 23, 42, 0.8); padding: 15px; border-radius: 12px; 
        border: 1px solid #00FF9D22; transition: 0.3s;
    }
    
    .tag-rec { color: #38BDF8; font-size: 11px; font-weight: 800; text-transform: uppercase; }
    .tag-dir { color: #F87171; font-size: 11px; font-weight: 800; text-transform: uppercase; }
    .email-val { color: #F1F5F9; font-family: 'Courier New', monospace; font-size: 16px; display: block; margin-top: 5px; }

    /* Button Style */
    .stButton>button { 
        background: linear-gradient(90deg, #00FF9D 0%, #059669 100%); 
        color: black !important; font-weight: bold; border: none; height: 3.8em; 
        border-radius: 12px; transition: 0.3s; text-transform: uppercase;
    }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(0, 255, 157, 0.4); }
    
    input { background-color: #111827 !important; color: white !important; border: 1px solid #334155 !important; }
    </style>
    """, unsafe_allow_html=True)

# 📍 3. API KEY MANAGEMENT (L-Fix l-Niha'i)
# Kat-jbedha mn Secrets (Streamlit Cloud) wlla mn Env Variables
raw_key = st.secrets.get("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", os.environ.get("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", ""))

# Had l-ster darouri bach i-lssaq l-key s7i7a wakha t-koun m9tou3a f sstora f Secrets
MY_API_KEY = "".join(raw_key.split())

# Sidebar bach n-verify-o l-connection
with st.sidebar:
    st.title("🕵️ Mokhbaire Status")
    if MY_API_KEY:
        st.success("✅ API Connected")
    else:
        st.error("❌ API Missing in Secrets")
    st.write("---")
    st.info("Had l-app kadi scan l-database d l-recrutement bach tjbed les emails d les RH.")

# Header
st.markdown("<h1 style='text-align: center; color: #00FF9D;'>🕵️ L'MOKHBIRE : OPPORTUNITY HUNTER</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>Deep Scan: USA, UK, Canada, France, Germany, Spain...</p>", unsafe_allow_html=True)
st.write("---")

# 4. Search Form
col1, col2 = st.columns([2, 1])
with col1:
    job = st.text_input("🎯 Quel métier ?", placeholder="ex: Truck Driver, Software Engineer, Nurse...")
with col2:
    loc = st.selectbox("🌍 Choisir le Pays", ["Germany", "France", "Spain", "Italy", "Canada", "USA", "UK"])

if st.button("LANCER LE DEEP SCAN 🔍"):
    if not MY_API_KEY:
        st.error("❌ Mouchkil f l-API Key! T-akked mn Settings > Secrets f Streamlit.")
    elif not job:
        st.warning("⚠️ Kteb l-metier lli kat-qelleb 3lih.")
    else:
        try:
            client = Groq(api_key=MY_API_KEY)
            with st.status("📡 Scan stratégique en cours...", expanded=True):
                # Prompt iħtirafi bach i-jbed l-emails dyal l-Directeurs o l-General
                prompt = f"""
                Act as a Professional Headhunter. Find 3 REAL companies currently hiring for {job} in {loc}. 
                Identify: 
                1. General/Reception email.
                2. Direct email for the HR Manager or Hiring Director.
                
                Return ONLY this HTML format:
                <div class='hunter-card'>
                    <h2 style='color: white; margin-bottom:5px;'>🏢 COMPANY NAME</h2>
                    <p style='color: #00FF9D;'>📍 Location: {loc} | Recruitment: ACTIVE</p>
                    <div class='contact-container'>
                        <div class='email-box'>
                            <span class='tag-rec'>📩 RÉCEPTION / SUPPORT:</span>
                            <span class='email-val'>contact@company.com</span>
                        </div>
                        <div class='email-box' style='border-left: 4px solid #F87171;'>
                            <span class='tag-dir'>🎯 DÉCIDEUR (HR DIRECTOR):</span>
                            <span class='email-val'>hr.director@company.com</span>
                        </div>
                    </div>
                </div>
                """
                res = client.chat.completions.create(
                    model="llama-3.3-70b-versatile", 
                    messages=[{"role": "user", "content": prompt}]
                )
                st.session_state['hunt_res'] = res.choices[0].message.content
        except Exception as e:
            st.error(f"❌ Error during scan: {str(e)}")

# 5. Display Results
if 'hunt_res' in st.session_state:
    st.markdown("### 🔍 RÉSULTATS DU SCAN MOKHBARE")
    st.markdown(st.session_state['hunt_res'], unsafe_allow_html=True)
    
    # Button bach t-download-i l-audit
    st.download_button(
        label="📥 Télécharger l'Audit",
        data=st.session_state['hunt_res'],
        file_name=f"audit_{job}.html",
        mime="text/html"
    )
