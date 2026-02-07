import streamlit as st
from groq import Groq

# 1. Configuration dyal l-page
st.set_page_config(page_title="OPPS HUNTER - L'MOKHBIRE", layout="wide", page_icon="🕵️")

# 2. Design "Cyber Pro Max" (Custom CSS)
st.markdown("""
    <style>
    /* Background Matrix Dark */
    .stApp { background-color: #020617; color: #00FF9D; font-family: 'Segoe UI', sans-serif; }
    
    /* Card dyal l-Offre */
    .hunter-card { 
        background: #0F172A; border: 1px solid #1E293B; 
        padding: 25px; border-radius: 15px; margin-bottom: 25px; 
        border-left: 6px solid #00FF9D; box-shadow: 0 4px 20px rgba(0, 255, 157, 0.1);
    }
    
    /* L-Kadr l-7mer dyal l-Email (Direct Access) */
    .director-box { 
        background: rgba(239, 68, 68, 0.1); border: 2px dashed #EF4444; 
        padding: 20px; border-radius: 10px; margin-top: 15px; text-align: center;
    }
    .email-text { color: #FF4B4B; font-weight: bold; font-size: 22px; font-family: 'Courier New', monospace; }
    .label-red { color: white; font-size: 13px; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 5px; display: block; }

    /* Button Style */
    .stButton>button { 
        background: linear-gradient(90deg, #00FF9D 0%, #008F58 100%); 
        color: black; font-weight: bold; border: none; width: 100%; height: 3.8em; border-radius: 8px;
    }
    input { background-color: #111827 !important; color: white !important; border: 1px solid #00FF9D !important; }
    </style>
    """, unsafe_allow_html=True)

# 📍 API KEY SETUP
# Ghadi i-jbedha mn Secrets dyal Streamlit Cloud
MY_API_KEY = st.secrets.get("GROQ_API_KEY", "AIzaSyBUpOZ7lUxX6kLTkfHvAIG4Etll6LTj-_k")

# Header
st.markdown("<h1 style='text-align: center; color: #00FF9D;'>🕵️ L'MOKHBIRE : OPPORTUNITY HUNTER</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>Deep Search: Germany, France, Spain, Canada, USA, UK, Italy...</p>", unsafe_allow_html=True)
st.write("---")

# 3. Search Inputs
col1, col2 = st.columns([2, 1])
with col1:
    job = st.text_input("🎯 Quel métier ?", placeholder="ex: Truck Driver, IT Manager, Nurse...")
with col2:
    loc = st.selectbox("🌍 Choisir le Pays", ["Germany", "France", "Spain", "Italy", "Canada", "USA", "UK"])

if st.button("LANCER LE DEEP SCAN 🔍"):
    if job and MY_API_KEY != "YOUR_KEY_HERE":
        client = Groq(api_key=MY_API_KEY)
        with st.status("📡 Scan en cours dans les bases de données RH...", expanded=True):
            # Prompt iħtirafi bach i-jbed l-emails dyal l-Directeurs
            prompt = f"""
            Act as a Professional Headhunter. Find 3 REAL companies currently hiring for {job} in {loc}. 
            For each company, identify the most likely direct email format for the HR DIRECTOR or HIRING MANAGER.
            Return ONLY this HTML format:
            <div class='hunter-card'>
                <h2 style='color: white; margin-bottom:5px;'>🏢 COMPANY NAME</h2>
                <p style='color: #94A3B8;'>📍 Location: {loc} | Status: Recrutement Ouvert</p>
                <div class='director-box'>
                    <span class='label-red'>🎯 DIRECT ACCESS (DÉCIDEUR RH):</span>
                    <span class='email-text'>name.surname@company.com</span>
                </div>
                <p style='color: #888; font-size: 11px; margin-top: 10px;'>Note: Envoyez votre CV directement à ce contact pour maximiser vos chances.</p>
            </div>
            """
            res = client.chat.completions.create(model="llama-3.3-70b-versatile", messages=[{"role": "user", "content": prompt}])
            st.session_state['hunt_res'] = res.choices[0].message.content
    else:
        st.warning("⚠️ 3emmer l-metier w t-7eqqeq men l-API Key f Secrets.")

# 4. Results
if 'hunt_res' in st.session_state:
    st.markdown("### 🏢 RÉSULTATS DU SCAN MOKHBARE")
    st.markdown(st.session_state['hunt_res'], unsafe_allow_html=True)
