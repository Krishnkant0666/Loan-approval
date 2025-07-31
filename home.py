import streamlit as st

# Page configuration
st.set_page_config(page_title="🏠 Home Loan", page_icon="🏠", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');

    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(to right, #f0fdfa, #fefce8);
        font-family: 'Poppins', sans-serif;
    }

    .stButton > button {
        background-color: #10b981;
        color: white;
        padding: 0.5em 1.3em;
        border-radius: 8px;
        font-weight: bold;
        font-size: 16px;
        transition: 0.3s;
    }

    .stButton > button:hover {
        background-color: #059669;
    }

    h1, h3 {
        color: #1e293b;
    }
    </style>
""", unsafe_allow_html=True)

# Page Title
st.title("🏠 Apply for a Home Loan")
st.markdown("Build or buy your dream home with our easy and fast home loan options.")
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
    - Age: 23 to 65 years
    - Stable income source
    - Minimum 2 years in current job/business
    - Property must be approved and legally clear
    - Good credit score recommended
    """)

if show_documents:
    st.markdown("""
    ### 📄 Required Documents
    - Identity Proof (Aadhaar, PAN, Passport)
    - Address Proof
    - Income documents (Salary Slips / ITR)
    - Property documents (Agreement, Plan, NOC)
    - Bank statements (last 6 months)
    """)

st.markdown("---")

# Loan Application Form
st.subheader("📝 Apply for Home Loan")

with st.form("home_loan_form"):
    name = st.text_input("Full Name")
    age = st.number_input("Age", 23, 65)
    employment = st.selectbox("Employment Type", ["Salaried", "Self-Employed"])
    monthly_income = st.number_input("Monthly Income (₹)", min_value=15000, step=1000)
    property_value = st.number_input("Property Value (₹)", min_value=1000000, step=50000)
    loan_amount = st.number_input("Loan Amount Requested (₹)", min_value=500000, max_value=property_value, step=10000)
    submit = st.form_submit_button("📤 Submit Application")

if submit:
    if name:
        st.success(f"🎉 Thank you {name}! Your home loan request of ₹{loan_amount:,.0f} has been submitted.")
        st.info("✅ Our housing finance team will contact you shortly to proceed.")
    else:
        st.error("❌ Please complete all the fields before submitting.")

st.markdown("---")
st.caption("🔐 This is a demo home loan form. No data is stored.")
