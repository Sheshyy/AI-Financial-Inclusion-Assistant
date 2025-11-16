# 💰 AI Financial Inclusion Assistant for Families with Special Needs Children

### 👩🏽‍💻 Developed by: **Sandra Wangeci Kirundi**  
**Course:** AI for Software Engineering – Power Learn Project (Capstone)  
**Date:** November 2025  
**Prototype Version:** 1.0  

🌍 **Live Demo:**  
👉 [Click here to try the app](https://ai-financial-inclusion-assistant-sheshyy-final-project.streamlit.app/)


## 🧠 Project Overview
The **AI Financial Inclusion Assistant** is a Streamlit-based machine learning prototype that helps **families raising children with special needs** predict their upcoming monthly expenses and receive **personalized financial advice**.  

This project was inspired by my volunteer work with **Special Olympics Kenya**, where I interacted with children with intellectual and physical disabilities and their families. Many of these households face financial strain due to therapy sessions, medication costs, and specialized education.  

Combining my **background in Financial Engineering** and **AI training**, I built this tool to promote **financial inclusion**, aligning with:  
- **SDG 1:** No Poverty  
- **SDG 10:** Reduced Inequalities  


## 🎯 Objectives
- Predict next month’s household expenses based on income and expense data.  
- Provide a **Financial Health Score** to evaluate spending efficiency.  
- Offer personalized budgeting and savings advice.  
- Allow users to **choose between a Random Forest model and a Deep Learning model** for prediction.  
- Demonstrate an **end-to-end AI pipeline** from data to deployment.  


## ⚙️ Tech Stack
| Category | Tools & Libraries |
|-----------|------------------|
| **Programming Language** | Python |
| **Machine Learning** | Scikit-learn (Random Forest Regressor) |
| **Deep Learning** | TensorFlow / Keras |
| **Frontend** | Streamlit |
| **Data Handling** | Pandas, NumPy |
| **Deployment** | Streamlit Cloud |
| **Model Storage** | joblib (.joblib), H5 (.h5) |


## 🧩 How It Works
1. **User Input:**  
   Families enter income and expense details (salary, business income, rent, school fees, therapy, etc.).  

2. **Model Selection:**  
   Users can choose between:  
   - 🟩 **Random Forest Regressor (Default):** Fast and stable predictions.  
   - 🧠 **Deep Learning Model (TensorFlow):** Captures complex non-linear expense trends.  

3. **Prediction Stage:**  
   The selected model predicts next month’s total expenses.  
   A “realism correction” ensures predictions stay within logical income limits.  

4. **Insights Generation:**  
   The app displays:  
   - Predicted total monthly expenses  
   - A **Financial Health Score** (progress bar)  
   - Personalised budgeting tips and financial advice  

5. **AI Financial Advisor:**  
   A rule-based chatbot answers financial questions about savings, grants, loans, and insurance options.  

6. **Support Resources:**  
   The app provides links to government and NGO programs like NCPWD, NHIF, and Special Olympics Kenya.  


## 🧪 Installation & Setup

### 1. Clone the repository
 git clone https://github.com/<your-username>/AI-Financial-Inclusion-Assistant.git
 cd AI-Financial-Inclusion-Assistant
 
### 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate     # on Windows
source venv/bin/activate  # on Mac/Linux

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run the Streamlit app
streamlit run app.py

📊 Example Inputs
| Category         | Example (KES) |
| ---------------- | ------------- |
| Salary Income    | 25,000        |
| Business Income  | 5,000         |
| Side Hustle      | 2,000         |
| Rent             | 8,000         |
| Food & Groceries | 5,000         |
| Physiotherapy    | 2,000         |
| Medication       | 1,000         |
| School Fees      | 4,000         |
## 📈 Expected Output

Predicted Total Monthly Expenses: KSh 23,500 (example)

Financial Health Score: 72%

Advice: “Your spending is balanced. Try saving 10% monthly for emergencies.”
## 🧠 Model Details
Model Type	Description	Use Case
Random Forest Regressor: A tree-based ensemble model trained on synthetic Kenyan household data.	Default option — provides fast, explainable predictions for small datasets.
Deep Learning Model (TensorFlow/Keras)	A simple feedforward neural network trained on the same dataset.	Optional — captures complex, non-linear expense patterns when more data is available.

## Dataset:
Synthetic Data Generation

Since no real financial inclusion dataset was available for this specific prediction task, this project utilises a synthetically generated dataset designed to mimic realistic household financial behaviour.

Limitations of Synthetic Data
While synthetic data enables experimentation, it may not capture the full complexity of real-world financial behaviour. For this reason, all results should be interpreted as prototype-level insights, not real financial advice.

## Features:
14 numeric inputs (income sources + general + special needs expenses).

## Evaluation Metrics:

R² Score: 0.883

Mean Absolute Error (MAE): KSh 4,823.39

## Fairness & Ethical Considerations

Model trained on synthetic data; may not represent all socioeconomic groups.

Inputs are processed locally; no user data is stored.

The tool is intended for financial awareness and budgeting guidance, not personalised financial advice.
Usage Disclaimer

This tool should not be used to make high-stakes financial decisions.

It is intended as an educational and exploratory prototype, not a real financial evaluation system.

## Limitations

- **Lightweight Model for Prediction:** The expense prediction uses a Random Forest or a small Deep Learning model. While accurate for demonstration, its predictions may not fully generalize to real-world financial data.

- **Rule-Based Chatbot:** The AI financial advisor responds using predefined keywords. It cannot interpret questions outside its known set of terms (e.g., 'saving', 'loan', 'grant', 'budget', 'insurance', 'expense'). Answers are not dynamically generated.

- **Tiny Synthetic Dataset:** The dataset used for demonstration is small and synthetically generated; it does not reflect real household financial behaviour.

- **No Long-Term Memory:** Each user query is processed independently; the system cannot remember prior conversations.


## Future Enhancements:

Integrate real anonymised expense data from NCPWD or NGOs.

Fine-tune the deep learning architecture for higher accuracy.

Replace rule-based NLP with a fine-tuned transformer model (e.g., BERT).

## 🚀 Deployment

The app is deployed publicly via Streamlit Cloud.

##🧾 Example Use Case

A parent caring for a child with autism enters their household income and therapy costs.
The AI model predicts next month’s likely expenses, calculates a financial health score, and provides tailored savings and budgeting advice — helping the family plan ahead while linking them to disability support programs.

## 📚 References

Power Learn Project (PLP) – AI for Software Engineering Course

Scikit-learn & TensorFlow Documentation

Streamlit Developer Guide

National Council for Persons with Disabilities (NCPWD)

Special Olympics Kenya

## 💬 Author

Sandra Wangeci Kirundi
📧 kirundisandra@gmail.com
 | 📞 +254 797 074 219
🌍 Nairobi, Kenya

## 💙 Acknowledgment

“This project was inspired by my volunteer experience at Special Olympics Kenya and my goal to use data science and AI to empower families raising children with special needs. Though a prototype, it demonstrates how AI can promote real social and economic impact.”
