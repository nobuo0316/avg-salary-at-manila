import streamlit as st
import pandas as pd

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Manila Salary Dashboard", layout="centered")

st.title("🇵🇭 Manila Salary Benchmark")
st.markdown("Weighted salary estimation (**80% Government + 20% Market Data**)")

# -----------------------------
# Multiplier（追加部分🔥）
# -----------------------------
st.sidebar.header("⚙️ Adjustment")

multiplier = st.sidebar.slider(
    "Salary Adjustment Multiplier",
    0.3, 1.5, 1.0, 0.01
)

st.sidebar.caption(f"Applied Multiplier: x{multiplier}")

# -----------------------------
# Data
# -----------------------------
data = pd.DataFrame({
    "Job": [
        "Engineer", "Accountant", "HR",
        "Sales", "Marketing", "IT Support", "Customer Service"
    ],

    "Entry_gov": [15000, 14000, 13000, 14000, 15000, 14000, 13000],
    "Entry_gov_src": ["PSA", "PSA", "DOLE", "PSA", "PSA", "PSA", "PSA"],
    "Entry_gov_url": ["https://psa.gov.ph"]*7,

    "Exp_gov": [35000, 30000, 28000, 30000, 32000, 30000, 27000],
    "Exp_gov_src": ["PSA", "PSA", "DOLE", "PSA", "PSA", "PSA", "PSA"],
    "Exp_gov_url": ["https://psa.gov.ph"]*7,

    "Mng_gov": [80000, 70000, 65000, 70000, 75000, 68000, 60000],
    "Mng_gov_src": ["PSA", "PSA", "DOLE", "PSA", "PSA", "PSA", "PSA"],
    "Mng_gov_url": ["https://psa.gov.ph"]*7,

    "Entry_non": [18000, 16000, 15000, 17000, 18000, 16000, 15000],
    "Entry_non_src": ["JobStreet", "Glassdoor", "JobStreet", "JobStreet", "Glassdoor", "JobStreet", "Glassdoor"],
    "Entry_non_url": ["https://www.jobstreet.com.ph", "https://www.glassdoor.com", "https://www.jobstreet.com.ph",
                      "https://www.jobstreet.com.ph", "https://www.glassdoor.com", "https://www.jobstreet.com.ph", "https://www.glassdoor.com"],

    "Exp_non": [40000, 35000, 32000, 35000, 38000, 34000, 30000],
    "Exp_non_src": ["JobStreet", "Glassdoor", "JobStreet", "JobStreet", "Glassdoor", "JobStreet", "Glassdoor"],
    "Exp_non_url": ["https://www.jobstreet.com.ph", "https://www.glassdoor.com", "https://www.jobstreet.com.ph",
                    "https://www.jobstreet.com.ph", "https://www.glassdoor.com", "https://www.jobstreet.com.ph", "https://www.glassdoor.com"],

    "Mng_non": [90000, 80000, 75000, 82000, 85000, 78000, 70000],
    "Mng_non_src": ["JobStreet", "Glassdoor", "JobStreet", "JobStreet", "Glassdoor", "JobStreet", "Glassdoor"],
    "Mng_non_url": ["https://www.jobstreet.com.ph", "https://www.glassdoor.com", "https://www.jobstreet.com.ph",
                    "https://www.jobstreet.com.ph", "https://www.glassdoor.com", "https://www.jobstreet.com.ph", "https://www.glassdoor.com"],
})

# -----------------------------
# UI
# -----------------------------
job = st.selectbox("💼 Select Job Role", data["Job"])
row = data[data["Job"] == job].iloc[0]

# -----------------------------
# Calculation（倍率適用🔥）
# -----------------------------
def calc(gov, non):
    base = gov * 0.8 + non * 0.2
    return base * multiplier

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
# Sources
# -----------------------------
with st.expander("🔎 View Data Sources"):
    st.markdown(f"""
### Entry Level
- [Gov: {row['Entry_gov_src']}]({row['Entry_gov_url']})
- [Market: {row['Entry_non_src']}]({row['Entry_non_url']})

### Experienced
- [Gov: {row['Exp_gov_src']}]({row['Exp_gov_url']})
- [Market: {row['Exp_non_src']}]({row['Exp_non_url']})

### Managerial
- [Gov: {row['Mng_gov_src']}]({row['Mng_gov_url']})
- [Market: {row['Mng_non_src']}]({row['Mng_non_url']})
""")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Sources: PSA, DOLE, JobStreet, Glassdoor (Top pages)")
