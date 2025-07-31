import streamlit as st

# Page configuration
st.set_page_config(page_title="Smart Loan Approval", page_icon="💸", layout="centered")

# --- Sidebar Navigation ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
    st.markdown("## SmartLoan™")
    st.markdown("### 🧭 Navigation")

    st.markdown("[🏠 Home](./)", unsafe_allow_html=True)
    st.markdown("[🎓 Education Loan](./education)", unsafe_allow_html=True)
    st.markdown("[🧑‍💼 Personal Loan](./personal)", unsafe_allow_html=True)
    st.markdown("[💼 Business Loan](./business)", unsafe_allow_html=True)
    st.markdown("[🏠 Home Loan](./home)", unsafe_allow_html=True)

# --- Custom CSS: Gradient Background & Styling ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(to right, #f3e8ff, #e0f2fe);
        font-family: 'Poppins', sans-serif;
    }
            
    /* Hide the default multipage navigation menu at the top */
    [data-testid="stSidebarNav"] {
        display: none;
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

    .stSuccess {
        background-color: #dcfce7 !important;
        color: #14532d !important;
        border-left: 6px solid #22c55e;
    }

    .stWarning {
        background-color: #fef9c3 !important;
        color: #78350f !important;
        border-left: 6px solid #facc15;
    }

    .stError {
        background-color: #fee2e2 !important;
        color: #991b1b !important;
        border-left: 6px solid #f87171;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("<h1 style='text-align: center;'>💸 Smart Loan Approval System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>Instantly check if you're eligible for a loan based on your profile and income.</p>", unsafe_allow_html=True)
st.markdown("---")

# --- Applicant Info ---
st.subheader("👤 Applicant Information")
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Full Name")
    age = st.number_input("Age", 18, 70)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    married = st.selectbox("Marital Status", ["Married", "Single"])
with col2:
    dependents = st.selectbox("Number of Dependents", ["0", "1", "2", "3+"])
    education = st.selectbox("Education Level", ["Graduate", "Not Graduate"])
    employment = st.selectbox("Employment Type", ["Salaried", "Self-Employed"])
    area = st.selectbox("Property Area", ["Urban", "Semi-Urban", "Rural"])

# --- Financial Info ---
st.markdown("---")
st.subheader("💵 Financial Information")
col3, col4 = st.columns(2)
with col3:
    income = st.number_input("Applicant's Annual Income (₹)", 100000, 10000000, step=10000)
    co_income = st.number_input("Co-applicant Annual Income (₹)", 0, 10000000, step=10000)
with col4:
    credit = st.selectbox("Credit History", ["Good", "Bad"])
    requested_loan = st.number_input("Requested Loan Amount (₹)", 50000, 10000000, step=50000)

# --- Loan Eligibility Logic ---
def get_loan_multiplier(credit_score, employment_type, education_level, area_type):
    multiplier = 4  # base multiplier
    if credit_score == 1:
        multiplier += 1
    if employment_type == "Salaried":
        multiplier += 1
    if education_level == "Graduate":
        multiplier += 0.5
    if area_type in ["Urban", "Semi-Urban"]:
        multiplier += 0.5
    return multiplier

# --- Prediction Logic ---
st.markdown("---")
if st.button("🔍 Check Loan Approval"):
    credit_val = 1 if credit == "Good" else 0
    total_income = income + co_income
    loan_multiplier = get_loan_multiplier(credit_val, employment, education, area)
    max_loan = total_income * loan_multiplier

    st.subheader("📋 Evaluation Result")
    if credit_val == 1 and income >= 200000:
        if requested_loan <= max_loan:
            st.success(f"✅ Loan Approved for ₹{requested_loan:,.0f}")
            st.markdown(f"🎉 You are eligible for up to **₹{max_loan:,.0f}**.")

            # --- Loan Type Selection via hyperlinks ---
            st.markdown("### 💡 <b>Select the Type of Loan You Want to Proceed With:</b>", unsafe_allow_html=True)
            col5, col6 = st.columns(2)
            with col5:
                st.markdown("[🎓 Education Loan](./education)", unsafe_allow_html=True)
                st.markdown("[💼 Business Loan](./business)", unsafe_allow_html=True)
            with col6:
                st.markdown("[🏠 Home Loan](./home)", unsafe_allow_html=True)
                st.markdown("[👤 Personal Loan](./personal)", unsafe_allow_html=True)
        else:
            st.warning(f"❌ Requested ₹{requested_loan:,.0f} exceeds your eligibility.")
            st.markdown(f"💡 You can apply for up to **₹{max_loan:,.0f}**.")
    else:
        st.error("❌ Loan Rejected")
        st.markdown("📉 Reason: Low income or poor credit history.")

# --- Footer ---
st.markdown("---")
st.caption("🔐 This is a secure educational demo. Your data is not stored.")
