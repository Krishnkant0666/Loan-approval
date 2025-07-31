import streamlit as st

# Page configuration
st.set_page_config(page_title="🧍 Personal Loan", page_icon="🧍", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');

    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(to right, #fff5e4, #e1f5fe);
        font-family: 'Poppins', sans-serif;
    }

    .stButton > button {
        background-color: #ef4444;
        color: white;
        padding: 0.5em 1.3em;
        border-radius: 8px;
        font-weight: bold;
        font-size: 16px;
        transition: 0.3s;
    }

    .stButton > button:hover {
        background-color: #dc2626;
    }

    h1, h3 {
        color: #1e293b;
    }
    </style>
""", unsafe_allow_html=True)

# Page Title
st.title("🧍 Apply for a Personal Loan")
st.markdown("Need funds for emergencies, weddings, travel, or anything personal? Apply for a personal loan instantly.")
st.markdown("---")

# Buttons
st.subheader("📌 What would you like to know?")
col1, col2 = st.columns(2)

with col1:
    show_criteria = st.button("✅ View Eligibility Criteria")
with col2:
    show_documents = st.button("📄 Required Documents")

if show_criteria:
    st.markdown("""
    ### ✅ Eligibility Criteria
    - Age: 21 to 60 years
    - Monthly income of at least ₹20,000
    - Employment: Salaried or self-employed
    - Minimum 6 months in current job/business
    - Good credit history preferred
    """)

if show_documents:
    st.markdown("""
    ### 📄 Required Documents
    - Identity Proof (Aadhaar, PAN, Passport)
    - Address Proof (Utility bill, Aadhaar, Passport)
    - Salary slips (last 3 months) or ITR for self-employed
    - Bank statements (last 6 months)
    - Passport size photograph
    """)

st.markdown("---")

# Loan Application Form
st.subheader("📝 Apply for Personal Loan")

with st.form("personal_loan_form"):
    name = st.text_input("Full Name")
    age = st.number_input("Age", 21, 60)
    employment = st.selectbox("Employment Type", ["Salaried", "Self-Employed"])
    purpose = st.text_input("Loan Purpose (e.g., Medical, Travel, Wedding)")
    monthly_income = st.number_input("Monthly Income (₹)", min_value=10000, step=1000)
    loan_amount = st.number_input("Loan Amount Requested (₹)", min_value=50000, max_value=1500000, step=10000)
    submit = st.form_submit_button("📤 Submit Application")

if submit:
    if name and purpose:
        st.success(f"🎉 Thank you {name}! Your personal loan request of ₹{loan_amount:,.0f} has been submitted.")
        st.info("✅ Our team will contact you shortly to proceed.")
    else:
        st.error("❌ Please complete all the fields before submitting.")

st.markdown("---")
st.caption("🔐 This is a demo personal loan form. No data is stored.")
