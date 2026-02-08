import streamlit as st
from groq import Groq
import pandas as pd
import io

# 1. Page Configuration
st.set_page_config(page_title="OPPS HUNTER PRO - L'MOKHBIRE", layout="wide", page_icon="🕵️")

# 2. Custom CSS (Cyber-Professional Design)
st.markdown("""
    <style>
    .stApp { background-color: #020617; color: #00FF9D; font-family: 'Inter', sans-serif; }
    
    /* Card Professional Design */
    .hunter-card { 
        background: linear-gradient(145deg, #0F172A, #1E293B); 
        border: 1px solid #334155; 
        padding: 30px; border-radius: 20px; margin-bottom: 30px; 
        border-left: 10px solid #00FF9D;
        box-shadow: 0 15px 35px rgba(0,0,0,0.4);
    }
    
    /* Email Section Layout */
    .contact-container { 
        display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); 
        gap: 20px; margin-top: 20px; 
    }
    
    .email-box { 
        background: rgba(15, 23, 42, 0.8); 
        padding: 15px; border-radius: 12px; border: 1px solid #00FF9D22;
        transition: 0.3s;
    }
    .email-box:hover { border-color: #00FF9D; background: rgba(0, 255, 157, 0.05); }
    
    .tag-rec { color: #38BDF8; font-size: 11px; font-weight: 800; letter-spacing: 1px; }
    .tag-dir { color: #F87171; font-size: 11px; font-weight: 800; letter-spacing: 1px; }
    .email-val { color: #F1F5F9; font-family: 'JetBrains Mono', monospace; font-size: 17px; display: block; margin-top: 5px; }

    /* Buttons & Inputs */
    .stButton>button { 
        background: linear-gradient(90deg, #00FF9D 0%, #059669 100%); 
        color: #000 !important; font-weight: bold; border: none; height: 3.5em; 
        border-radius: 12px; width: 100%; font-size: 16px;
    }
    input { background-color: #0F172A !important; border: 1px solid #334155 !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# 📍 3. API KEY LOGIC (Total Fix)
raw_key = st.secrets.get("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", "")
# Had l-ster houwa l-boss: i-7iyed spaces o sstora bach t-khdem l-key 100%
MY_API_KEY = "".join(raw_key.split())

# Sidebar for Stats/Help
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1055/1055644.png", width=100)
    st.title("Mokhbaire Console")
    st.info("Scanner i7tirafi bach tjbed les emails direct d les décideurs.")
    if not MY_API_KEY:
        st.error("⚠️ API Key machi m-linkya!")

# Header
st.markdown("<h1 style='text-align: center; color: #00FF9D; margin-bottom:0;'>🕵️ L'MOKHBIRE PRO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94A3B8;'>Intelligence Artificielle pour le Headhunting International</p>", unsafe_allow_html=True)
st.write("---")

# 4. Search Form
c1, c2 = st.columns([2, 1])
with c1:
    job = st.text_input("🎯 Métier (Ex: Cloud Architect, Truck Driver...)", placeholder="Kteb smit l-khidma hna...")
with c2:
    loc = st.selectbox("🌍 Zone de Recherche", ["Germany", "France", "Spain", "Canada", "USA", "UK", "Italy", "Gulf"])

if st.button("Lancer le Scan Stratégique 🔍"):
    if not MY_API_KEY:
        st.error("❌ Mouchkil f l-API Key! Check your Streamlit Secrets.")
    elif not job:
        st.warning("⚠️ 3emmer l-metier li kat-qelleb 3lih.")
    else:
        try:
            client = Groq(api_key=MY_API_KEY)
            with st.status("📡 Scan en cours dans les bases de données...", expanded=True) as status:
                st.write("Recherche des entreprises actives...")
                
                # Prompt PRO bach i-khrej l-format m9ad
                prompt = f"""
                Act as a Senior Headhunter. Find 3 REAL companies hiring for {job} in {loc}. 
                For each company, extract:
                1. General Email (Reception/HR Dept).
                2. Direct VIP Email (HR Director, CEO, or Hiring Manager).
                
                Return ONLY this HTML format for each:
                <div class='hunter-card'>
                    <h2 style='color: white; margin-bottom:5px;'>🏢 COMPANY NAME</h2>
                    <p style='color: #00FF9D;'>📍 Location: {loc} | Recruiting Status: Priority</p>
                    <div class='contact-container'>
                        <div class='email-box'>
                            <span class='tag-rec'>📩 RÉCEPTION / RH GENERAL:</span>
                            <span class='email-val'>contact@company.com</span>
                        </div>
                        <div class='email-box' style='border-left: 4px solid #F87171;'>
                            <span class='tag-dir'>🎯 DÉCIDEUR / DIRECTEUR:</span>
                            <span class='email-val'>directeur.rh@company.com</span>
                        </div>
                    </div>
                </div>
                """
                
                res = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.5
                )
                
                st.session_state['hunt_res'] = res.choices[0].message.content
                status.update(label="✅ Scan terminé avec succès!", state="complete")
                
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# 5. Display & Export
if 'hunt_res' in st.session_state:
    st.markdown("### 🏢 Entreprises Identifiées")
    st.markdown(st.session_state['hunt_res'], unsafe_allow_html=True)
    
    # Optional: Download Button (Simple Version)
    st.download_button(
        label="📥 Télécharger l'Audit (Text)",
        data=st.session_state['hunt_res'],
        file_name=f"audit_{job}_{loc}.html",
        mime="text/html"
    )
