import streamlit as st
import requests

# === Page Config ===
st.set_page_config(
    page_title="Credit Card Fraud Detector",
    page_icon="💳",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# === Professional Minimalist CSS – 2025 Enterprise SaaS Style ===
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .main {
        background-color: #f8f9fa;
        color: #212529;
    }
    
    h1 {
        font-weight: 700;
        color: #0d6efd;
        text-align: center;
        margin-bottom: 0.5rem;
        font-size: 2.5rem;
    }
    
    .subtitle {
        text-align: center;
        color: #6c757d;
        font-size: 1.1rem;
        margin-bottom: 3rem;
    }
    
    .section-card {
        background-color: white;
        border-radius: 12px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        border: 1px solid #e9ecef;
    }
    
    .section-header {
        font-weight: 600;
        color: #343a40;
        margin-bottom: 1.5rem;
        font-size: 1.3rem;
        border-bottom: 1px solid #dee2e6;
        padding-bottom: 0.5rem;
    }
    
    .result-container {
        text-align: center;
        padding: 3rem;
        border-radius: 16px;
        background-color: white;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
        margin: 3rem 0;
    }
    
    .probability-text {
        font-size: 4rem;
        font-weight: 700;
        margin: 1rem 0;
    }
    
    .decision-text {
        font-size: 2rem;
        font-weight: 600;
    }
    
    .fraud-prob {
        color: #dc3545;
    }
    
    .legit-prob {
        color: #198754;
    }
    
    .stButton > button {
        background-color: #0d6efd;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.8rem 2rem;
        font-weight: 600;
        width: 100%;
        height: 3rem;
        font-size: 1.1rem;
        box-shadow: 0 4px 10px rgba(13, 110, 253, 0.2);
        transition: all 0.2s;
    }
    
    .stButton > button:hover {
        background-color: #0b5ed7;
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(13, 110, 253, 0.3);
    }
    
    .stNumberInput > div > div > input {
        border-radius: 8px;
        border: 1px solid #ced4da;
    }
    
    hr {
        border-color: #dee2e6;
    }
    
    .footer {
        text-align: center;
        color: #6c757d;
        font-size: 0.9rem;
        margin-top: 4rem;
    }
</style>
""", unsafe_allow_html=True)

# === Header ===
st.markdown("<h1>💳 Credit Card Fraud Detector</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Enterprise-grade machine learning model for real-time transaction fraud assessment</p>", unsafe_allow_html=True)

# === PCA Features Section ===
st.markdown("<div class='section-card'>", unsafe_allow_html=True)
st.markdown("<div class='section-header'>Anonymized PCA Components (V1–V28)</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

features = [
    ("V1", 0.0), ("V2", 0.0), ("V3", 0.0), ("V4", 0.0), ("V5", 0.0), ("V6", 0.0),
    ("V7", 0.0), ("V8", 0.0), ("V9", 0.0), ("V10", 0.0), ("V11", 0.0), ("V12", 0.0),
    ("V13", 0.0), ("V14", 0.0), ("V15", 0.0), ("V16", 0.0), ("V17", 0.0), ("V18", 0.0),
    ("V19", 0.0), ("V20", 0.0), ("V21", 0.0), ("V22", 0.0), ("V23", 0.0), ("V24", 0.0),
    ("V25", 0.0), ("V26", 0.0), ("V27", 0.0), ("V28", 0.0)
]

inputs = {}

with col1:
    for i in range(0, len(features), 3):
        if i < len(features):
            key, val = features[i]
            inputs[key] = st.number_input(key, value=val, step=0.01, format="%.4f", key=f"c1_{key}")

with col2:
    for i in range(1, len(features), 3):
        if i < len(features):
            key, val = features[i]
            inputs[key] = st.number_input(key, value=val, step=0.01, format="%.4f", key=f"c2_{key}")

with col3:
    for i in range(2, len(features), 3):
        if i < len(features):
            key, val = features[i]
            inputs[key] = st.number_input(key, value=val, step=0.01, format="%.4f", key=f"c3_{key}")

st.markdown("</div>", unsafe_allow_html=True)

# === Engineered Features Section ===
st.markdown("<div class='section-card'>", unsafe_allow_html=True)
st.markdown("<div class='section-header'>Engineered Features</div>", unsafe_allow_html=True)

col_a, col_b, col_c = st.columns(3)

with col_a:
    inputs["Amount_log"] = st.number_input("Amount (log scale)", value=5.0, step=0.1, format="%.3f")
with col_b:
    inputs["Hour"] = st.number_input("Hour of Transaction (0-23)", min_value=0, max_value=23, value=12)
with col_c:
    inputs["IsoScore"] = st.number_input("Isolation Score", value=0.0, step=0.01, format="%.4f")

st.markdown("</div>", unsafe_allow_html=True)

# === Prediction Button ===
if st.button("Analyze Transaction"):
    transaction = {
        "V1": inputs["V1"], "V2": inputs["V2"], "V3": inputs["V3"], "V4": inputs["V4"],
        "V5": inputs["V5"], "V6": inputs["V6"], "V7": inputs["V7"], "V8": inputs["V8"],
        "V9": inputs["V9"], "V10": inputs["V10"], "V11": inputs["V11"], "V12": inputs["V12"],
        "V13": inputs["V13"], "V14": inputs["V14"], "V15": inputs["V15"], "V16": inputs["V16"],
        "V17": inputs["V17"], "V18": inputs["V18"], "V19": inputs["V19"], "V20": inputs["V20"],
        "V21": inputs["V21"], "V22": inputs["V22"], "V23": inputs["V23"], "V24": inputs["V24"],
        "V25": inputs["V25"], "V26": inputs["V26"], "V27": inputs["V27"], "V28": inputs["V28"],
        "Amount_log": inputs["Amount_log"], "Hour": inputs["Hour"], "IsoScore": inputs["IsoScore"]
    }
    
    with st.spinner("Processing transaction..."):
        try:
            response = requests.post("http://127.0.0.1:8000/predict", json=transaction)
            response.raise_for_status()
            result = response.json()
            
            prob = result['Fraud Probability']
            decision = 'FRAUD' if result['Fraud Decision'] == 1 else 'LEGITIMATE'
            is_fraud = result['Fraud Decision'] == 1
            
            prob_class = "fraud-prob" if is_fraud else "legit-prob"
            
            st.markdown(f"""
            <div class='result-container'>
                <div style='color: #495057; font-size: 1.3rem;'>Fraud Probability</div>
                <div class='probability-text {prob_class}'>{prob:.2%}</div>
                <div class='decision-text'>{decision}</div>
            </div>
            """, unsafe_allow_html=True)
            
            if is_fraud:
                st.error("🚨 Potential fraud detected – Recommend declining transaction")
            else:
                st.success("✅ Transaction appears legitimate")
                
        except requests.exceptions.ConnectionError:
            st.error("❌ Unable to connect to prediction server. Ensure FastAPI backend is running.")
        except Exception as e:
            st.error(f"⚠️ Error: {e}")

# === Footer ===
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div class='footer'>Professional Fraud Detection System • Built for Data-Driven Decisions • 2025</div>", unsafe_allow_html=True)