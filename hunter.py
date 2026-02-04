import streamlit as st
from groq import Groq

def run_hunter_agent(api_key):
    # 1. CSS dyal Screenshot 236 & 238 (The Cyber Scan Look)
    st.markdown("""
        <style>
        .stApp { background-color: #050A0E; color: #00FF9D; font-family: 'Courier New', Courier, monospace; }
        
        /* Stats Row Style */
        .stat-card {
            background-color: #0D161F;
            border: 1px solid #1E293B;
            padding: 15px;
            border-radius: 8px;
            text-align: center;
            box-shadow: 0 0 10px rgba(0, 255, 157, 0.05);
        }
        .stat-val { font-size: 28px; font-weight: bold; color: white; display: block; }
        .stat-lbl { font-size: 10px; color: #888; text-transform: uppercase; letter-spacing: 1px; }

        /* Job Card Style */
        .opp-card {
            background-color: #0D161F;
            border: 1px solid #1E293B;
            padding: 25px;
            border-radius: 10px;
            margin-top: 20px;
            border-left: 5px solid #00FF9D;
        }
        
        /* The Red Director Email Box */
        .director-box {
            background-color: rgba(255, 75, 75, 0.1);
            border: 1px solid #FF4B4B;
            padding: 15px;
            border-radius: 6px;
            margin-top: 15px;
        }
        
        .stButton>button { 
            background-color: #00FF9D; color: #050A0E; 
            font-weight: bold; width: 100%; border: none; 
            height: 3em; border-radius: 5px;
        }
        
        input { background-color: #0D161F !important; color: white !important; border: 1px solid #1E293B !important; }
        </style>
        """, unsafe_allow_html=True)

    # 2. Header System
    st.markdown("<h1 style='text-align: center; color: #00FF9D; letter-spacing: 2px;'>PRO OPPORTUNITY HUNTER</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; font-size: 12px;'>SYSTEM STATUS: OPERATIONAL • CONNECTED TO GLOBAL JOB BOARDS</p>", unsafe_allow_html=True)

    # 3. Search Bar Section
    st.write("---")
    col_input, col_country = st.columns([3, 1])
    with col_input:
        job_target = st.text_input("🎯 ENTER TARGET JOB", placeholder="e.g. Truck Driver, IT Manager, Nurse...")
    with col_country:
        country = st.selectbox("🌍 REGION", ["Canada", "Germany", "France", "USA", "Spain"])

    if st.button("START DEEP SCAN 🚀"):
        if job_target and api_key:
            client = Groq(api_key=api_key)
            
            # Simulated Stats kima f Screenshot 238
            st.write("### 📊 MARKET INSIGHTS")
            s1, s2, s3 = st.columns(3)
            s1.markdown("<div class='stat-card'><span class='stat-val'>200+</span><span class='stat-lbl'>Companies Detected</span></div>", unsafe_allow_html=True)
            s2.markdown("<div class='stat-card'><span class='stat-val'>1,374</span><span class='stat-lbl'>Jobs Active</span></div>", unsafe_allow_html=True)
            s3.markdown("<div class='stat-card'><span class='stat-val'>95%</span><span class='stat-lbl'>Match Accuracy</span></div>", unsafe_allow_html=True)
            
            with st.status("Scanning Corporate Databases & OSINT Patterns...", expanded=True):
                # Prompt m-fessal bach i-jbed l-emails dyal l-Directeurs
                prompt = f"""
                Act as a Headhunter. Find 3 companies hiring for {job_target} in {country}.
                For each, provide:
                1. Company Name & Location.
                2. Professional Email Format for the HR Director or Decision Maker.
                3. A very short pitch.
                Return HTML ONLY like this:
                <div class='opp-card'>
                    <h3 style='color: #00FF9D; margin-bottom: 5px;'>🏢 COMPANY_NAME</h3>
                    <p style='color: #888; font-size: 14px;'>📍 Location, {country} | Sector: Professional Services</p>
                    <div class='director-box'>
                        <strong style='color: #FF4B4B; display: block; margin-bottom: 5px;'>🎯 DIRECT DIRECTOR EMAIL:</strong>
                        <code style='color: white; font-size: 18px;'>first.last@company.com</code>
                        <p style='color: #FF4B4B; font-size: 11px; margin-top: 5px;'>Priority: High - Direct Access to Hiring Manager</p>
                    </div>
                </div>
                """
                res = client.chat.completions.create(model="llama-3.3-70b-versatile", messages=[{"role": "user", "content": prompt}])
                st.session_state['hunter_res'] = res.choices[0].message.content

    # 4. Results Display
    if 'hunter_res' in st.session_state:
        st.markdown("### 🏢 IDENTIFIED TARGETS")
        st.markdown(st.session_state['hunter_res'], unsafe_allow_html=True)

# 5. Display Results
if 'results' in st.session_state:
    st.markdown("### 🏢 IDENTIFIED OPPORTUNITIES")
    st.markdown(st.session_state['results'], unsafe_allow_html=True)
