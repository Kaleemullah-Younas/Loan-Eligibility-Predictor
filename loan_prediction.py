import streamlit as st
import requests
from streamlit_lottie import st_lottie
import pickle

model = pickle.load(open('svm_model.pkl', 'rb'))


st.set_page_config(page_title="Bank Loan Predictor", page_icon="🏛️")

# Function to load Lottie animation from URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

col1, col2 = st.columns([1,4])
with col1:
    lottie_url = "https://lottie.host/823637a6-7914-486c-9718-100563a1e07e/BCAH4h7weL.json"
    lottie_json = load_lottieurl(lottie_url)
    app_icon = st_lottie(lottie_json, speed=1, width=100, height=100, key="lottie")
with col2:
    welcome_container = st.empty()
    welcome_container.header("Bank Loan Prediction Model")

# Define variables
account_no = ''
fn = ''
gen = ''
mar = ''
dep = ''
edu = ''
emp = ''
prop = ''
cred = ''
mon_income = 0
co_mon_income = 0
loan_amt = 0
dur = ''

# Function to check if mandatory fields are filled
def check_mandatory_fields_filled():
    return all([account_no, fn, gen, mar, dep, edu, emp, prop, cred, mon_income, loan_amt, dur])

# Main section for other input fields
st.subheader("Personal Information")
# Sidebar for account number and full name
col1, col2 = st.columns([1, 2])
with col1:
    account_no = st.text_input('Account number')
with col2:
    fn = st.text_input('Full Name')
col1, col2 = st.columns(2)
with col1:
    gen_display = ('Female', 'Male')
    gen = st.selectbox("Gender", gen_display)
    mar_display = ('No', 'Yes')
    mar = st.selectbox("Marital Status", mar_display)
    dep_display = ('No', 'One', 'Two', 'More than Two')
    dep = st.selectbox("Dependents", dep_display)
    edu_display = ('Not Graduate', 'Graduate')
    edu = st.selectbox("Education", edu_display)
    emp_display = ('Job', 'Business')
    emp = st.selectbox("Employment Status", emp_display)
    dur_display = ['2 Month', '6 Month', '8 Month', '1 Year', '16 Month']
    dur = st.selectbox("Loan Duration", dur_display)
with col2:
    prop_display = ('Rural', 'Semi-Urban', 'Urban')
    prop = st.selectbox("Property Area", prop_display)
    cred_display = ('Between 300 to 500', 'Above 500')
    cred = st.selectbox("Credit Score", cred_display)
    mon_income = st.number_input("Applicant's Monthly Income($)", value=0)
    co_mon_income = st.number_input("Co-Applicant's Monthly Income($)", value=0)
    loan_amt = st.number_input("Loan Amount", value=0)

# Submit button to make predictions
if st.button("Submit"):
    # Check if mandatory fields are filled
    if not check_mandatory_fields_filled():
        st.warning('Please fill in all mandatory fields to proceed.')
        st.stop()

    # Function to map loan duration to months
    def get_loan_duration(dur):
        durations = {'2 Month': 60, '6 Month': 180, '8 Month': 240, '1 Year': 360, '16 Month': 480}
        return durations.get(dur, 0)

    duration = get_loan_duration(dur)
    features = [[gen_display.index(gen), mar_display.index(mar), dep_display.index(dep),
                 edu_display.index(edu), emp_display.index(emp), mon_income, co_mon_income,
                 loan_amt, duration, cred_display.index(cred), prop_display.index(prop)]]

    prediction = model.predict(features)

    if prediction == 0:
        st.error(
            f"Hello: {fn} | Account number: {account_no} | According to our calculations, Sorry! 😔 you will not get the loan from the Bank.")
    else:
        st.success(
            f"Hello: {fn} | Account number: {account_no} | Congratulations!! 🥳 You will get the loan from the Bank.")
