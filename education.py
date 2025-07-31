import streamlit as st

st.set_page_config(page_title="🎓 Education Loan", page_icon="🎓", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');

    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(to right, #fdfcfb, #e2d1c3);
        font-family: 'Poppins', sans-serif;
    }

    .stButton > button {
        background-color: #6366f1;
        color: white;
        padding: 0.5em 1.3em;
        border-radius: 8px;
        font-weight: bold;
        font-size: 16px;
        transition: 0.3s;
    }

    .stButton > button:hover {
        background-color: #4f46e5;
    }

    h1, h3 {
        color: #1e293b;
    }

    </style>
""", unsafe_allow_html=True)

st.title("🎓 Apply for an Education Loan")
st.markdown("Welcome! Here's everything you need to know and do to apply for an education loan.")

st.markdown("---")

# --- Criteria & Documents Buttons ---
st.subheader("📌 What would you like to know?")
col1, col2 = st.columns(2)

with col1:
    show_criteria = st.button("✅ View Eligibility Criteria")
with col2:
    show_documents = st.button("📄 Required Documents")

if show_criteria:
    st.markdown("""
    ### ✅ Eligibility Criteria
    - Applicant must be an Indian national
    - Admission must be secured in a recognized institution
    - Courses allowed: Graduate, Postgraduate, Professional, Technical
    - Co-applicant (parent/guardian) needed if applicant has no income
    - Strong academic background may help
    """)
    
if show_documents:
    st.markdown("""
    ### 📄 Required Documents
    - Admission letter from institution
    - Academic mark sheets (10th, 12th, graduation if any)
    - Fee structure provided by college/university
    - Identity proof (Aadhaar, PAN)
    - Income proof of co-applicant (ITR/salary slips)
    """)

st.markdown("---")

# --- Application Form ---
st.subheader("📝 Apply for Education Loan")

with st.form("education_loan_form"):
    full_name = st.text_input("Full Name")
    age = st.number_input("Age", 17, 60)
    course = st.text_input("Course Name")
    institution = st.text_input("Institution Name")
    study_location = st.selectbox("Study Location", ["India", "Abroad"])
    loan_amount = st.number_input("Loan Amount Requested (₹)", min_value=50000, max_value=2500000, step=10000)
    submit = st.form_submit_button("📤 Submit Application")

if submit:
    if full_name and course and institution:
        st.success(f"🎉 Thank you {full_name}! Your application for ₹{loan_amount:,.0f} has been received.")
        st.info("✅ Our education loan specialist will reach out to you shortly.")
    else:
        st.error("❌ Please fill all the fields before submitting.")

st.markdown("---")
st.caption("🔐 This is a demo education loan form. No data is stored.")


