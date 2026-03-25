import streamlit as st
import pandas as pd

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Manila Salary Dashboard", layout="centered")

st.title("🇵🇭 Manila Salary Benchmark")
st.markdown("Weighted salary estimation (**80% Government + 20% Market Data**)")

# -----------------------------
# Data（URL付き）
# -----------------------------
data = pd.DataFrame({
    "Job": [
        "Engineer", "Accountant", "HR",
        "Sales", "Marketing", "IT Support", "Customer Service"
    ],

    # Government
    "Entry_gov": [15000, 14000, 13000, 14000, 15000, 14000, 13000],
    "Entry_gov_src": [
        "https://psa.gov.ph/wages/engineer",
        "https://psa.gov.ph/wages/accountant",
        "https://dole.gov.ph/hr-wage",
        "https://psa.gov.ph/wages/sales",
        "https://psa.gov.ph/wages/marketing",
        "https://psa.gov.ph/wages/it-support",
        "https://psa.gov.ph/wages/customer-service"
    ],

    "Exp_gov": [35000, 30000, 28000, 30000, 32000, 30000, 27000],
    "Exp_gov_src": [
        "https://psa.gov.ph/wages/engineer-mid",
        "https://psa.gov.ph/wages/accountant-mid",
        "https://dole.gov.ph/hr-mid",
        "https://psa.gov.ph/wages/sales-mid",
        "https://psa.gov.ph/wages/marketing-mid",
        "https://psa.gov.ph/wages/it-mid",
        "https://psa.gov.ph/wages/cs-mid"
    ],

    "Mng_gov": [80000, 70000, 65000, 70000, 75000, 68000, 60000],
    "Mng_gov_src": [
        "https://psa.gov.ph/wages/engineer-manager",
        "https://psa.gov.ph/wages/accountant-manager",
        "https://dole.gov.ph/hr-manager",
        "https://psa.gov.ph/wages/sales-manager",
        "https://psa.gov.ph/wages/marketing-manager",
        "https://psa.gov.ph/wages/it-manager",
        "https://psa.gov.ph/wages/cs-manager"
    ],

    # Non-Government
    "Entry_non": [18000, 16000, 15000, 17000, 18000, 16000, 15000],
    "Entry_non_src": [
        "https://jobstreet.com/engineer-salary",
        "https://glassdoor.com/accountant-salary",
        "https://jobstreet.com/hr-salary",
        "https://jobstreet.com/sales-salary",
        "https://glassdoor.com/marketing-salary",
        "https://jobstreet.com/it-support-salary",
        "https://glassdoor.com/customer-service-salary"
    ],

    "Exp_non": [40000, 35000, 32000, 35000, 38000, 34000, 30000],
    "Exp_non_src": [
        "https://jobstreet.com/engineer-mid",
        "https://glassdoor.com/accountant-mid",
        "https://jobstreet.com/hr-mid",
        "https://jobstreet.com/sales-mid",
        "https://glassdoor.com/marketing-mid",
        "https://jobstreet.com/it-mid",
        "https://glassdoor.com/cs-mid"
    ],

    "Mng_non": [90000, 80000, 75000, 82000, 85000, 78000, 70000],
    "Mng_non_src": [
        "https://jobstreet.com/engineer-manager",
        "https://glassdoor.com/accountant-manager",
        "https://jobstreet.com/hr-manager",
        "https://jobstreet.com/sales-manager",
        "https://glassdoor.com/marketing-manager",
        "https://jobstreet.com/it-manager",
        "https://glassdoor.com/cs-manager"
    ],
})

# -----------------------------
# UI
# -----------------------------
job = st.selectbox("💼 Select Job Role", data["Job"])
row = data[data["Job"] == job].iloc[0]

# -----------------------------
# Calculation
# -----------------------------
def calc(gov, non):
    return gov * 0.8 + non * 0.2

entry = calc(row["Entry_gov"], row["Entry_non"])
exp = calc(row["Exp_gov"], row["Exp_non"])
mng = calc(row["Mng_gov"], row["Mng_non"])

# -----------------------------
# Display
# -----------------------------
st.subheader(f"📊 {job} Salary (Monthly PHP)")

col1, col2, col3 = st.columns(3)

col1.metric("Entry Level", f"₱{entry:,.0f}")
col2.metric("Experienced", f"₱{exp:,.0f}")
col3.metric("Managerial", f"₱{mng:,.0f}")

# -----------------------------
# Chart
# -----------------------------
chart_data = pd.DataFrame({
    "Level": ["Entry", "Experienced", "Managerial"],
    "Salary": [entry, exp, mng]
}).set_index("Level")

st.bar_chart(chart_data)

# -----------------------------
# Clickable Source
# -----------------------------
with st.expander("🔎 View Data Sources"):
    st.markdown(f"""
### Entry Level
- [Gov Source]({row['Entry_gov_src']})
- [Market Source]({row['Entry_non_src']})

### Experienced
- [Gov Source]({row['Exp_gov_src']})
- [Market Source]({row['Exp_non_src']})

### Managerial
- [Gov Source]({row['Mng_gov_src']})
- [Market Source]({row['Mng_non_src']})
""")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Note: Replace sample URLs with actual PSA / DOLE / JobStreet / Glassdoor deep links.")
