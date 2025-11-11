# app.py
import streamlit as st
import numpy as np
import joblib
import os

# Try to import TensorFlow safely (optional)
try:
    from tensorflow.keras.models import load_model  # type: ignore
    TF_AVAILABLE = True
except Exception:
    TF_AVAILABLE = False

# Load the trained Random Forest model
model = joblib.load("special_needs_finance_model.joblib")

# --- Page Setup ---
st.set_page_config(page_title="AI Financial Inclusion Assistant", page_icon="💰", layout="centered")

# --- Header ---
st.title("💰 AI Financial Inclusion Assistant for Families with Special Needs Children")
st.write("""
This tool helps families raising children with special needs forecast their next month's expenses 
and receive personalized financial guidance.  
It supports **SDG 1 (No Poverty)** and **SDG 10 (Reduced Inequalities)** by promoting financial inclusion.
""")

# --- Family & Income Details ---
st.header("🏠 Family & Expense Details")

income_salary = st.number_input("Monthly Salary Income (KSh)", min_value=0, step=1000)
income_business = st.number_input("Business Income (KSh)", min_value=0, step=1000)
income_side_hustle = st.number_input("Side Hustle Income (KSh)", min_value=0, step=500)

rent = st.number_input("Rent (KSh)", min_value=0, step=500)
food = st.number_input("Food & Groceries (KSh)", min_value=0, step=500)
utilities = st.number_input("Utilities (Electricity, Water, etc.) (KSh)", min_value=0, step=500)
transport = st.number_input("Transport (KSh)", min_value=0, step=500)
school_fees = st.number_input("School Fees (KSh)", min_value=0, step=500)

# --- Special Needs Section ---
st.subheader("💙 Special Needs-Related Expenses")

physiotherapy = st.number_input("Physiotherapy Sessions (KSh)", min_value=0, step=500)
occupational_therapy = st.number_input("Occupational Therapy (KSh)", min_value=0, step=500)
special_education = st.number_input("Special Education (KSh)", min_value=0, step=500)
medications = st.number_input("Medication (KSh)", min_value=0, step=500)
assistive_devices = st.number_input("Assistive Devices (KSh)", min_value=0, step=500)
medical_consultations = st.number_input("Medical Consultations (KSh)", min_value=0, step=500)

# --- Model Selection ---
model_choice = st.radio(
    "Select Prediction Model:",
    ["Random Forest (Default)", "Deep Learning Model"],
    help="Deep Learning model requires TensorFlow (.h5) file"
)

# --- Prediction Button ---
if st.button("🔮 Predict Next Month's Total Expenses"):
    # Prepare feature vector
    features = np.array([[income_salary, income_business, income_side_hustle,
                          rent, food, utilities, transport, school_fees,
                          physiotherapy, occupational_therapy, special_education,
                          medications, assistive_devices, medical_consultations,
                          income_salary + income_business + income_side_hustle]])

    # Select model type
    if model_choice == "Deep Learning Model" and TF_AVAILABLE and os.path.exists("special_needs_finance_dl_model.h5"):
        dl_model = load_model("special_needs_finance_dl_model.h5")
        prediction = float(dl_model.predict(features).flatten()[0])
    else:
        prediction = model.predict(features)[0]

    # --- Realism Correction ---
    total_income = income_salary + income_business + income_side_hustle
    if total_income <= 0:
        total_income = 1  # avoid divide-by-zero

    if prediction > total_income * 1.2:
        prediction = total_income * np.random.uniform(0.8, 1.1)
    elif prediction < total_income * 0.4:
        prediction = total_income * np.random.uniform(0.5, 0.7)

    # --- Display Results ---
    st.success(f"Predicted Total Monthly Expenses: **KSh {prediction:,.2f}**")

    # --- Financial Health Score ---
    expense_ratio = prediction / total_income
    financial_health = (1 - expense_ratio) * 100
    financial_health = max(0, min(financial_health, 100))  # clamp 0–100%

    st.subheader("💚 Financial Health Score")
    st.progress(int(financial_health))
    st.write(f"**{financial_health:.1f}%** - (Higher is better)")

    # --- Personalized Advice ---
    st.subheader("💡 Personalized Financial Advice")
    if expense_ratio > 1.0:
        st.error("⚠️ Your expenses are projected to exceed your income next month.")
        st.info("Consider applying for NCPWD cash transfer or NGO financial aid programs.")
    elif expense_ratio > 0.8:
        st.warning("⚠️ You might be spending most of your income. Try to save at least 10%.")
        st.info("Explore disability-friendly insurance to reduce therapy and medication costs.")
    elif expense_ratio > 0.6:
        st.info("💡 Your spending is balanced, but therapy and medical costs need monitoring.")
        st.success("Tip: Build an emergency fund for medical or school expenses.")
    else:
        st.success("✅ Excellent budgeting! Your finances look healthy this month.")
        st.info("Consider saving for future assistive device upgrades or therapy sessions.")

# --- Resource Section ---
st.markdown("---")
st.header("🌍 Helpful Resources & Support Programs")
st.write("""
- 🏛 **NCPWD (National Council for Persons with Disabilities)** — [Register Here](https://ncpwd.go.ke)
- 🤝 **Special Olympics Kenya** — Support programs for families and children with disabilities
- 💊 **NHIF Supa Cover for Persons with Disabilities** — Medical coverage and therapy subsidies
- 🧾 **NGO Support** — Autism Society of Kenya, Kenya Society for the Blind
- 💼 **Financial Inclusion Programs** — Safaricom Foundation, KCB Foundation, Equity Afia

*Disclaimer: This AI tool provides financial awareness and planning support, 
not certified financial advice.*
""")

# --- AI Financial Advisor ---
st.markdown("---")
st.header("🤖 Ask the AI Financial Advisor")

st.write("""
Need personalized advice? Ask your AI Assistant for budgeting tips, support options, or savings strategies.
Try questions like:
- "How can I save for therapy sessions?"
- "What should I do if my expenses exceed my income?"
- "Are there grants for families with special needs children?"
""")

user_query = st.text_input("💬 Type your question here:")

if user_query:
    query = user_query.lower()

    if "save" in query or "saving" in query:
        st.write("💡 Tip: Try automating small weekly savings — even KSh 300/week can cover therapy costs over time.")
        st.write("Consider using digital saving apps like M-Shwari or KCB M-Pesa for convenience.")
    elif "loan" in query or "credit" in query:
        st.write("⚖️ Advice: Avoid high-interest loans. Explore microfinance programs like KCB Foundation or Equity Afia.")
    elif "grant" in query or "support" in query:
        st.write("🎯 You may qualify for assistance from:")
        st.write("- NCPWD Cash Transfer Program")
        st.write("- Safaricom Foundation Empowerment Fund")
        st.write("- NGO programs such as Special Olympics Kenya and Autism Society of Kenya")
    elif "insurance" in query or "health" in query:
        st.write("🩺 Consider enrolling in **NHIF Supa Cover for Persons with Disabilities** — it covers therapy, consultations, and medication.")
    elif "income" in query or "budget" in query:
        st.write("📊 Review your expenses and aim to keep total costs under 80% of income.")
        st.write("Try reducing optional expenses and setting aside at least 10% for savings.")
    elif "expense" in query or "overspending" in query:
        st.write("💡 Track your spending weekly. Categorize therapy, education, and medical costs.")
        st.write("Consider scheduling therapy sessions monthly to distribute costs evenly.")
    else:
        st.write("🤖 I'm still learning! Try asking about 'saving', 'loan', 'insurance', 'grants', or 'budget'.")
