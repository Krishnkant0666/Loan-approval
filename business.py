import streamlit as st

# Page configuration
st.set_page_config(page_title="Business Loan", page_icon="💼", layout="centered")

# --- Custom CSS Matching Education Loan Theme ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(to right, #f3e8ff, #e0f2fe);
        font-family: 'Poppins', sans-serif;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    h1, h2, h3 {
        color: #1e293b !important;
    }

    .stButton>button {
        background-color: #3b82f6;
        color: white;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.6em 1.3em;
        font-size: 16px;
        transition: background 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #1d4ed8;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("<h1 style='text-align: center;'>💼 Business Loan Application</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>Check your eligibility and apply for a Business Loan with ease.</p>", unsafe_allow_html=True)
st.markdown("---")

# --- Business Loan Info ---
st.subheader("📋 Business Loan Criteria")
st.markdown("""
- Must have a registered business with valid documents
- Minimum 2 years of business operation
- Annual turnover should be ₹5 Lakhs or more
- Credit history should be good (score > 650)
- Purpose of loan must be clearly defined (working capital, expansion, etc.)
""")

# --- Application Form ---
st.subheader("🧾 Business Loan Application Form")
col1, col2 = st.columns(2)
with col1:
    business_name = st.text_input("Business Name")
    owner_name = st.text_input("Owner Full Name")
    years_operation = st.number_input("Years in Operation", 0, 50)
    turnover = st.number_input("Annual Turnover (₹)", 100000, 100000000)

with col2:
    purpose = st.text_area("Purpose of Loan")
    loan_amount = st.number_input("Requested Loan Amount (₹)", 50000, 10000000, step=50000)
    credit_score = st.number_input("Credit Score", 300, 900)

# --- Loan Decision Logic ---
if st.button("📤 Submit Business Loan Application"):
    if years_operation >= 2 and turnover >= 500000 and credit_score >= 650:
        st.success("✅ Your Business Loan request has been submitted successfully!")
        st.markdown("📞 Our team will contact you shortly for further documentation and processing.")
    else:
        st.error("❌ You are not eligible for a Business Loan at this time.")
        st.markdown("💡 Ensure your business meets the criteria or contact our support team for assistance.")

# --- Footer ---
st.markdown("---")
st.caption("🔐 Your information is secure and used only for loan evaluation purposes.")
