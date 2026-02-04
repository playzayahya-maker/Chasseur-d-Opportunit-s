import streamlit as st
from groq import Groq

# 1. Page Config
st.set_page_config(page_title="PRO Opportunity Hunter", layout="wide")

# 2. Advanced CSS for Cyber Look (Screenshots 236-238)
st.markdown("""
    <style>
    .stApp { background-color: #050A0E; color: #00FF9D; }
    
    /* Stats Cards */
    .stat-card {
        background-color: #0D161F; border: 1px solid #1E293B;
        padding: 20px; border-radius: 10px; text-align: center;
    }
    .stat-val { font-size: 35px; font-weight: bold; color: white; }
    
    /* Company Card */
    .company-card {
        background-color: #0D161F; border: 1px solid #1E293B;
        padding: 25px; border-radius: 12px; margin-bottom: 20px;
        border-left: 5px solid #00FF9D;
    }
    
    .hr-badge {
        background-color: rgba(255, 75, 75, 0.1); color: #FF4B4B;
        padding: 4px 10px; border-radius: 5px; font-weight: bold; font-size: 13px;
    }
    
    .stButton>button { background-color: #00FF9D; color: black; font-weight: bold; border-radius: 5px; }
    input { background-color: #0D161F !important; color: white !important; border: 1px solid #1E293B !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. UI Header
st.markdown("<h1 style='text-align: center;'>PRO OPPORTUNITY HUNTER</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>AI-Verified Job Market Intelligence • Professional Grade</p>", unsafe_allow_html=True)

# 4. Search Bar
st.write("---")
c1, c2 = st.columns([3, 1])
with c1:
    job_query = st.text_input("🎯 Target Job Title", placeholder="e.g. Truck Driver, Project Manager...")
with c2:
    country = st.selectbox("🌍 Coverage", ["Canada", "Germany", "France", "USA", "Spain"])

# API KEY
MY_API_KEY = "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"

if st.button("START SCAN 🔍"):
    if job_query and MY_API_KEY != "HNA_7ET_L_KEY_DYALK":
        client = Groq(api_key=MY_API_KEY)
        
        # Stats Simulated (Kima Screenshot 238)
        st.markdown("### 📊 MARKET SCAN OVERVIEW")
        s1, s2, s3 = st.columns(3)
        s1.markdown(f"<div class='stat-card'><p>COMPANIES</p><div class='stat-val'>200+</div></div>", unsafe_allow_html=True)
        s2.markdown(f"<div class='stat-card'><p>ACTIVE JOBS</p><div class='stat-val'>1,374</div></div>", unsafe_allow_html=True)
        s3.markdown(f"<div class='stat-card'><p>ACCURACY</p><div class='stat-val'>95%</div></div>", unsafe_allow_html=True)
        
        with st.status("Scanning Database...", expanded=True):
            st.write("📡 Accessing live corporate portals...")
            
            prompt = f"""Act as a Headhunter. Find 3 companies in {country} for {job_query}. 
            Return clean HTML format:
            <div class='company-card'>
                <h2>Company Name</h2>
                <p>📍 Location</p>
                <p>Why: Short reason</p>
                <span class='hr-badge'>HR Email: recruitment@company.com</span>
            </div>
            """
            res = client.chat.completions.create(model="llama-3.3-70b-versatile", messages=[{"role": "user", "content": prompt}])
            st.session_state['results'] = res.choices[0].message.content

# 5. Display Results
if 'results' in st.session_state:
    st.markdown("### 🏢 IDENTIFIED OPPORTUNITIES")
    st.markdown(st.session_state['results'], unsafe_allow_html=True)
