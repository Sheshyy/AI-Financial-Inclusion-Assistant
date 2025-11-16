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

5. **AI Financial Advisor (NLP):**  
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

Since no real financial inclusion dataset was available for this specific prediction task, this project utilises a synthetically generated dataset designed to mimic realistic household financial behaviour. The synthetic data was generated using controlled probabilistic distributions based on common financial patterns observed in low-income and middle-income populations.

The generation process followed these principles:

Income Values

Generated using a log-normal distribution to reflect skewed real-world income levels.

Ensures a high proportion of low-income entries and a lower proportion of high-income entries.

Expenses Breakdown

Food, transport, healthcare, utilities, and miscellaneous expenses were generated using:

Fixed percentages based on realistic household budget ratios

Random variation introduced using normal noise

Ensures variance while keeping values realistic.

Savings Behavior

Modeled as a function of disposable income

Added randomness to simulate unpredictable human financial decisions

Debt Levels

Generated with a right-skewed distribution to reflect real debt patterns

Higher-income households more likely to have formal loans

Lower-income households more likely to have smaller or informal debts

Random Noise for Realism

Gaussian noise added to all numerical values to avoid overly clean data

Limitations of Synthetic Data
While synthetic data enables experimentation, it may not capture the full complexity of real-world financial behavior. For this reason, all results should be interpreted as prototype-level insights, not real financial advice.

## Features:
14 numeric inputs (income sources + general + special needs expenses).

## Evaluation Metrics:

Coefficient of Determination (R²)

Mean Absolute Error (MAE)

## Fairness & Ethical Considerations

This project operates in a socially sensitive domain (financial inclusion), which requires awareness of potential bias, unequal model performance, and ethical implications.

Key fairness considerations include:

Bias from Synthetic Data

Since the model was trained on synthetic data, it may learn patterns that reflect the assumptions used during data generation rather than real population diversity.

Group Fairness

Different income ranges may receive different quality predictions.

For example, the model might be more accurate for middle-income households than extremely low-income households.

Mitigation Approach

During data generation, the synthetic dataset was designed to represent a wide range of income and expense levels to help reduce bias.

Expense proportions and noise were applied uniformly across all groups to avoid favouring one category over another.

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
