import streamlit as st
from groq import Groq

def run_hunter_agent(api_key):
    # CSS Cyberpunk Pro Max
    st.markdown("""
        <style>
        .stApp { background-color: #020617; color: #00FF9D; }
        
        /* Card dyal l-Offre */
        .opp-card {
            background: #0F172A; border: 1px solid #1E293B;
            padding: 25px; border-radius: 16px; margin-bottom: 25px;
            border-left: 6px solid #00FF9D; box-shadow: 0 10px 30px rgba(0,255,157,0.1);
        }
        
        /* L-Email f Kadr 7mer (Highlight) */
        .director-box {
            background: rgba(239, 68, 68, 0.1); border: 2px dashed #EF4444;
            padding: 20px; border-radius: 12px; margin-top: 15px; text-align: center;
        }
        .email-text {
            color: #EF4444; font-weight: bold; font-size: 22px;
            font-family: 'Courier New', monospace; text-shadow: 0 0 10px rgba(239, 68, 68, 0.3);
        }
        
        /* Buttons */
        .stButton>button {
            background: linear-gradient(90deg, #00FF9D 0%, #008F58 100%);
            color: #020617; font-weight: bold; border-radius: 10px; height: 3.5em; width: 100%; border: none;
        }
        input { background-color: #1E293B !important; color: white !important; border: 1px solid #334155 !important; }
        </style>
        """, unsafe_allow_html=True)

    st.markdown("<h1 style='color: #00FF9D;'>🕵️ L'CHASSEUR D'OPPORTUNITÉS</h1>", unsafe_allow_html=True)
    st.write("Deep Search Agent: Extraction des offres et emails des décideurs RH.")

    # Input Section
    st.markdown("---")
    c1, c2 = st.columns([2, 1])
    with c1:
        job = st.text_input("🎯 Métier Cible", placeholder="ex: Truck Driver, IT Manager...")
    with c2:
        loc = st.selectbox("🌍 Zone Géographique", ["Canada", "Germany", "France", "Spain", "Italy", "USA", "UK"])

    if st.button("LANCER LE SCAN DES DÉCIDEURS 🔍"):
        if job and api_key != "YOUR_GSK_KEY_HERE":
            client = Groq(api_key=api_key)
            with st.status("📡 Scan Deep-Web en cours...", expanded=True):
                prompt = f"""Find 3 real companies hiring for {job} in {loc}. 
                Provide the direct email format for the HR DIRECTOR.
                Return HTML strictly:
                <div class='opp-card'>
                    <h2 style='color: white; margin:0;'>🏢 COMPANY_NAME</h2>
                    <p style='color: #00FF9D;'>📍 Status: Recrutement Actif | {loc}</p>
                    <div class='director-box'>
                        <span style='color: white; font-size: 12px; letter-spacing: 2px;'>🎯 CONTACT DIRECT (DÉCIDEUR RH):</span><br>
                        <span class='email-text'>first.last@company.com</span>
                    </div>
                </div>"""
                res = client.chat.completions.create(model="llama-3.3-70b-versatile", messages=[{"role": "user", "content": prompt}])
                st.session_state['hunt_res'] = res.choices[0].message.content
        else:
            st.error("⚠️ Check Job Title or API Key in Secrets!")

    if 'hunt_res' in st.session_state:
        st.markdown(st.session_state['hunt_res'], unsafe_allow_html=True)
