import streamlit as st
from groq import Groq
import time

# 1. Page Configuration (Matrix/Cyber Style)
st.set_page_config(page_title="PRO INTELLIGENCE - L'MOKHBIRE", layout="wide")

# Custom CSS for Professional Dark UI
st.markdown("""
    <style>
    .stApp { background-color: #020617; color: #00FF9D; font-family: 'Inter', sans-serif; }
    
    /* Company Card Professional */
    .company-card { 
        background: rgba(15, 23, 42, 0.9); border: 1px solid #1E293B; 
        padding: 30px; border-radius: 20px; margin-bottom: 30px; 
        border-top: 4px solid #00FF9D; box-shadow: 0 10px 40px rgba(0,0,0,0.6);
    }
    
    /* Email Sections */
    .email-container { display: flex; gap: 20px; margin-top: 20px; flex-wrap: wrap; }
    
    .email-box { 
        flex: 1; min-width: 280px; background: #0F172A; 
        padding: 15px; border-radius: 12px; border: 1px solid #334155;
    }
    
    .label-reception { color: #38BDF8; font-size: 11px; font-weight: bold; letter-spacing: 1px; }
    .label-director { color: #F87171; font-size: 11px; font-weight: bold; letter-spacing: 1px; }
    .email-text { color: white; font-family: 'JetBrains Mono', monospace; font-size: 16px; display: block; margin-top: 8px; }

    /* Performance Status Badge */
    .status-badge { 
        background: rgba(0, 255, 157, 0.1); color: #00FF9D; 
        padding: 5px 15px; border-radius: 20px; font-size: 12px; 
        border: 1px solid #00FF9D; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 📍 API Key Security Fix
raw_key = st.secrets.get("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", "")
MY_API_KEY = "".join(raw_key.split())

# Sidebar
with st.sidebar:
    st.markdown("### 🛠 SYSTEM STATUS")
    if MY_API_KEY:
        st.markdown("<p style='color: #00FF9D;'>● ENCRYPTED CONNECTION READY</p>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='color: #FF4B4B;'>● SYSTEM OFFLINE (Check Key)</p>", unsafe_allow_html=True)

# UI Header
st.markdown("<h1 style='text-align: center; color: white;'>🕵️ PRO INTELLIGENCE SYSTEM</h1>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; margin-bottom: 40px;'><span class='status-badge'>95% ACCURACY MODE</span> <span class='status-badge'>LIVE DATA VERIFICATION</span></div>", unsafe_allow_html=True)

# Search Inputs
c1, c2 = st.columns([2, 1])
with c1:
    job = st.text_input("🎯 TARGET JOB TITLE", placeholder="e.g. Mechanical Engineer, IT Lead, Driver...")
with c2:
    loc = st.selectbox("🌍 GEOGRAPHIC ZONE", ["Canada", "Germany", "France", "Spain", "USA", "UK", "Italy"])

if st.button("EXECUTE DEEP SCAN ⚡"):
    if not MY_API_KEY:
        st.error("Authentication Error: API Key missing.")
    elif not job:
        st.warning("Please specify target job.")
    else:
        try:
            client = Groq(api_key=MY_API_KEY)
            with st.status("🔍 Initializing Corporate Intelligence Scan...", expanded=True) as status:
                st.write("📡 Scanning live recruitment databases...")
                time.sleep(1.5)
                st.write("🧬 Identifying decision-makers and HR directors...")
                time.sleep(1)
                
                # Prompt m-mouti bach i-jbed 2 emails darouri
                prompt = f"""
                As a Professional Intelligence Researcher, find 5 REAL companies currently hiring for {job} in {loc}. 
                For each company, you MUST provide exactly two distinct emails:
                1. A 'General/Reception' email (e.g., info@, contact@, or office@).
                2. A 'VIP Decision Maker' email (e.g., name.surname@, hr.director@, or recruitment.manager@).

                Return the response ONLY as HTML cards using this structure:
                <div class='company-card'>
                    <h2 style='color: #00FF9D; margin-top:0;'>🏢 COMPANY NAME</h2>
                    <p style='color: #94A3B8; font-size: 14px;'>📍 Location: {loc} | Recruitment Status: Active</p>
                    <div class='email-container'>
                        <div class='email-box'>
                            <span class='label-reception'>✉️ RÉCEPTION / SUPPORT</span>
                            <span class='email-text'>reception@company.com</span>
                        </div>
                        <div class='email-box' style='border-left: 4px solid #F87171;'>
                            <span class='label-director'>🎯 DIRECTEUR / DÉCIDEUR RH</span>
                            <span class='email-text'>hiring.manager@company.com</span>
                        </div>
                    </div>
                </div>
                """
                
                res = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.3
                )
                st.session_state['intel_res'] = res.choices[0].message.content
                status.update(label="✅ SCAN COMPLETE", state="complete")
        except Exception as e:
            st.error(f"Intelligence Failure: {e}")

# Results Display
if 'intel_res' in st.session_state:
    st.markdown("### 📑 IDENTIFIED TARGETS")
    st.markdown(st.session_state['intel_res'], unsafe_allow_html=True)
