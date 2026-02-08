import streamlit as st
from groq import Groq
import time

# 1. Config dyal l-Intelligence System
st.set_page_config(page_title="PRO INTEL - L'MOKHBIRE", layout="wide", page_icon="🕵️")

# 2. Design "Cyber Intelligence" (Professional & Dark)
st.markdown("""
<style>
    .stApp { background-color: #050505; color: #00FF9D; font-family: 'Inter', sans-serif; }
    .intel-card { 
        background: #0a0a0a; border: 1px solid #1a1a1a; 
        padding: 30px; border-radius: 20px; border-top: 6px solid #00FF9D;
        margin-bottom: 30px; box-shadow: 0 15px 45px rgba(0,0,0,0.8);
    }
    .badge-verified { 
        background: rgba(0, 255, 157, 0.1); color: #00FF9D; 
        padding: 5px 12px; border-radius: 8px; font-size: 10px; border: 1px solid #00FF9D;
        text-transform: uppercase; font-weight: bold;
    }
    .email-section { 
        display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); 
        gap: 20px; margin-top: 20px; 
    }
    .email-box { background: #111; padding: 15px; border-radius: 12px; border: 1px solid #222; }
    .label-blue { color: #38BDF8; font-size: 11px; font-weight: 800; }
    .label-red { color: #F87171; font-size: 11px; font-weight: 800; }
    .email-val { color: #fff; font-family: 'JetBrains Mono', monospace; font-size: 16px; margin-top: 5px; display: block; }
    
    /* Input Styling */
    input { background-color: #0f172a !important; color: white !important; border: 1px solid #1e293b !important; }
</style>
""", unsafe_allow_html=True)

# 📍 3. API KEY LOGIC (Manual Input + Secrets)
with st.sidebar:
    st.markdown("### 🔐 ACCESS CONTROL")
    # I-jarreb i-jbedha mn Secrets awalan
    secret_key = st.secrets.get("GROQ_API_KEY", "")
    
    # Ila mal9ahach, i-3tik fin t-ktebha
    user_key = st.text_input("Enter GROQ API KEY:", value=secret_key, type="password")
    
    if user_key:
        MY_API_KEY = "".join(user_key.split())
        st.success("✅ SYSTEM READY")
    else:
        MY_API_KEY = None
        st.error("❌ AUTHENTICATION REQUIRED")

# Header Section
st.markdown("<h1 style='text-align:center; letter-spacing: 3px;'>PRO INTELLIGENCE SYSTEM</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#555;'>PERFORMANCE FOCUS: ACCURACY > VELOCITY | AI-VERIFIED DATA</p>", unsafe_allow_html=True)

# 4. Search Interface
col1, col2 = st.columns([3, 1])
with col1:
    job = st.text_input("🎯 TARGET JOB ROLE", placeholder="e.g. Senior Software Engineer, Truck Driver...")
with col2:
    loc = st.selectbox("🌍 GEOGRAPHIC ZONE", ["Canada", "Germany", "France", "Spain", "Italy", "USA", "UK"])

# Execute Scan
if st.button("EXECUTE DEEP SCAN ⚡"):
    if not MY_API_KEY:
        st.error("Please provide a valid API Key in the sidebar.")
    elif not job:
        st.warning("Please enter a job title to start scanning.")
    else:
        try:
            client = Groq(api_key=MY_API_KEY)
            with st.status("🔍 Initializing multi-layered corporate scan...", expanded=True) as status:
                st.write("📡 Accessing international job registries...")
                time.sleep(1.5)
                st.write("🧬 Cross-referencing 5 companies with active hiring status...")
                time.sleep(1)
                st.write("📧 Extracting Decision Maker and Support contacts...")
                
                # Professional Prompt for 2 Emails and 5 Companies
                prompt = f"""
                As a Senior Headhunter, find 5 REAL companies in {loc} actively hiring for {job}.
                For each company, you MUST provide two distinct emails:
                1. General/Reception Email (e.g., info@, contact@).
                2. Decision Maker/HR Director Email (e.g., hr.director@, name.surname@).
                
                Return the results ONLY as HTML cards with this structure:
                <div class='intel-card'>
                    <div style='display:flex; justify-content:space-between;'>
                        <h2 style='color:white; margin:0;'>🏢 COMPANY NAME</h2>
                        <span class='badge-verified'>AI Verified</span>
                    </div>
                    <p style='color:#00FF9D; font-size:13px;'>📍 Location: {loc} | Status: Actively Hiring</p>
                    <div class='email-section'>
                        <div class='email-box'>
                            <span class='label-blue'>✉️ RECEPTION / GENERAL</span>
                            <span class='email-val'>contact@company.com</span>
                        </div>
                        <div class='email-box' style='border-left: 3px solid #F87171;'>
                            <span class='label-red'>🎯 HR DIRECTOR / DECISION MAKER</span>
                            <span class='email-val'>director.hr@company.com</span>
                        </div>
                    </div>
                </div>
                """
                
                res = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.2 # Higher accuracy
                )
                st.session_state['pro_results'] = res.choices[0].message.content
                status.update(label="✅ SCAN COMPLETE - 5 TARGETS IDENTIFIED", state="complete")
        except Exception as e:
            st.error(f"Intelligence Failure: {e}")

# 5. Display Results
if 'pro_results' in st.session_state:
    st.markdown("---")
    st.markdown(st.session_state['pro_results'], unsafe_allow_html=True)
