import streamlit as st
import pandas as pd

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Manila Salary Dashboard", layout="centered")

st.title("🇵🇭 Manila Salary Benchmark")
st.markdown("Weighted salary estimation (**80% Government + 20% Market Data**)")

# -----------------------------
# Multiplier
# -----------------------------
st.sidebar.header("⚙️ Adjustment")

multiplier = st.sidebar.slider("Salary Multiplier", 0.3, 1.5, 1.0, 0.01)
use_median = st.sidebar.checkbox("Use All Jobs Median")

# -----------------------------
# Data
# -----------------------------
data = pd.DataFrame({
    "Job": [
        "Engineer", "Accountant", "HR",
        "Sales", "Marketing", "IT Support", "Customer Service"
    ],

    "Entry_gov": [15000, 14000, 13000, 14000, 15000, 14000, 13000],
    "Exp_gov": [35000, 30000, 28000, 30000, 32000, 30000, 27000],
    "Mng_gov": [80000, 70000, 65000, 70000, 75000, 68000, 60000],

    "Entry_non": [18000, 16000, 15000, 17000, 18000, 16000, 15000],
    "Exp_non": [40000, 35000, 32000, 35000, 38000, 34000, 30000],
    "Mng_non": [90000, 80000, 75000, 82000, 85000, 78000, 70000],

    "gov_url": ["https://psa.gov.ph"]*7,
    "non_url": ["https://www.jobstreet.com.ph"]*7,
})

# -----------------------------
# Calculation Function
# -----------------------------
def calc(gov, non):
    return (gov * 0.8 + non * 0.2) * multiplier

# -----------------------------
# Median or Single Job
# -----------------------------
if use_median:
    entry = calc(data["Entry_gov"].median(), data["Entry_non"].median())
    exp = calc(data["Exp_gov"].median(), data["Exp_non"].median())
    mng = calc(data["Mng_gov"].median(), data["Mng_non"].median())

    title = "All Jobs Median"

else:
    job = st.selectbox("💼 Select Job Role", data["Job"])
    row = data[data["Job"] == job].iloc[0]

    entry = calc(row["Entry_gov"], row["Entry_non"])
    exp = calc(row["Exp_gov"], row["Exp_non"])
    mng = calc(row["Mng_gov"], row["Mng_non"])

    title = job

# -----------------------------
# Display
# -----------------------------
st.subheader(f"📊 {title} Salary (Monthly PHP)")

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
# Notes
# -----------------------------
st.markdown("---")
st.markdown("""
### 📝 Notes on Government Data Sources

- Data from :contentReference[oaicite:0]{index=0}:
  "Statistics → Labor and Employment → Occupational Wages Survey (OWS)"

- Data from :contentReference[oaicite:1]{index=1}:
  "Labor Standards / Wages and Productivity"

- Data often comes in PDF/Excel format and may require interpretation.
""")
