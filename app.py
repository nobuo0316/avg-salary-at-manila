import streamlit as st
import pandas as pd

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Manila Salary Dashboard", layout="centered")

st.title("🇵🇭 Manila Salary Dashboard")
st.markdown("Salary benchmark with **80% Government + 20% Non-Government data weighting**")

# -----------------------------
# Data（ソース付き）
# -----------------------------
data = pd.DataFrame({
    "Job": ["Engineer", "Accountant", "HR"],

    "Newbie_gov": [15000, 14000, 13000],
    "Newbie_gov_source": ["PSA 2024", "PSA 2024", "DOLE 2023"],

    "Mid_gov": [35000, 30000, 28000],
    "Mid_gov_source": ["PSA 2024", "PSA 2024", "DOLE 2023"],

    "Manager_gov": [80000, 70000, 65000],
    "Manager_gov_source": ["PSA 2024", "PSA 2024", "DOLE 2023"],

    "Newbie_non": [18000, 16000, 15000],
    "Newbie_non_source": ["JobStreet", "Glassdoor", "JobStreet"],

    "Mid_non": [40000, 35000, 32000],
    "Mid_non_source": ["JobStreet", "Glassdoor", "JobStreet"],

    "Manager_non": [90000, 80000, 75000],
    "Manager_non_source": ["JobStreet", "Glassdoor", "JobStreet"],
})

# -----------------------------
# UI（入力不要）
# -----------------------------
job = st.selectbox("💼 Select Job Role", data["Job"])

row = data[data["Job"] == job].iloc[0]

# -----------------------------
# Calculation（80/20）
# -----------------------------
def calc(gov, non):
    return gov * 0.8 + non * 0.2

newbie = calc(row["Newbie_gov"], row["Newbie_non"])
mid = calc(row["Mid_gov"], row["Mid_non"])
manager = calc(row["Manager_gov"], row["Manager_non"])

# -----------------------------
# Display（メイン）
# -----------------------------
st.subheader(f"📊 {job} Salary (Monthly PHP)")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Newbie",
    f"₱{newbie:,.0f}",
    help=f"Gov: {row['Newbie_gov_source']} / Non-Gov: {row['Newbie_non_source']}"
)

col2.metric(
    "Mid-level",
    f"₱{mid:,.0f}",
    help=f"Gov: {row['Mid_gov_source']} / Non-Gov: {row['Mid_non_source']}"
)

col3.metric(
    "Manager",
    f"₱{manager:,.0f}",
    help=f"Gov: {row['Manager_gov_source']} / Non-Gov: {row['Manager_non_source']}"
)

# -----------------------------
# Chart
# -----------------------------
chart_data = pd.DataFrame({
    "Level": ["Newbie", "Mid", "Manager"],
    "Salary": [newbie, mid, manager]
}).set_index("Level")

st.subheader("📈 Salary Comparison")
st.bar_chart(chart_data)

# -----------------------------
# Source Detail（透明性）
# -----------------------------
with st.expander("📊 Data Sources Detail"):
    source_df = pd.DataFrame({
        "Level": ["Newbie", "Mid", "Manager"],
        "Gov Source": [
            row["Newbie_gov_source"],
            row["Mid_gov_source"],
            row["Manager_gov_source"]
        ],
        "Non-Gov Source": [
            row["Newbie_non_source"],
            row["Mid_non_source"],
            row["Manager_non_source"]
        ]
    })

    st.dataframe(source_df, use_container_width=True)

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Note: Sample data. Replace with real PSA / DOLE / JobStreet / Glassdoor datasets.")
