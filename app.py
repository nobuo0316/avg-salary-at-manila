import streamlit as st
import pandas as pd

st.title("🇵🇭 Manila Salary Search")

# -----------------------------
# User Input
# -----------------------------
job = st.text_input("Enter Job Title (e.g. Engineer, Accountant)")

# -----------------------------
# Sample Dataset（あとでAPI/CSVに置き換え）
# -----------------------------
data = pd.DataFrame({
    "Job": ["Engineer", "Accountant", "HR"],
    "Newbie_gov": [15000, 14000, 13000],
    "Mid_gov": [35000, 30000, 28000],
    "Manager_gov": [80000, 70000, 65000],
    "Newbie_non": [18000, 16000, 15000],
    "Mid_non": [40000, 35000, 32000],
    "Manager_non": [90000, 80000, 75000],
})

# -----------------------------
# Search Logic
# -----------------------------
if job:
    result = data[data["Job"].str.contains(job, case=False)]

    if not result.empty:
        row = result.iloc[0]

        # Weighted calc
        def calc(gov, non):
            return gov * 0.8 + non * 0.2

        newbie = calc(row["Newbie_gov"], row["Newbie_non"])
        mid = calc(row["Mid_gov"], row["Mid_non"])
        manager = calc(row["Manager_gov"], row["Manager_non"])

        # Display
        st.subheader(f"💼 {job} Salary")

        col1, col2, col3 = st.columns(3)
        col1.metric("Newbie", f"₱{newbie:,.0f}")
        col2.metric("Mid-level", f"₱{mid:,.0f}")
        col3.metric("Manager", f"₱{manager:,.0f}")

    else:
        st.warning("No data found. Try another job.")
