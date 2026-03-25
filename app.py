import streamlit as st

st.set_page_config(page_title="Manila Salary Dashboard", layout="centered")

st.title("🇵🇭 Manila Salary Benchmark Dashboard")

st.markdown("This dashboard shows estimated salary levels in Manila using weighted data sources.")

# -----------------------------
# Sample Data (Monthly PHP)
# -----------------------------
# Government Data (e.g. PSA, DOLE)
gov_data = {
    "Newbie": 15000,
    "Mid-level": 35000,
    "Manager": 80000
}

# Non-Government Data (e.g. Jobstreet, Glassdoor)
nongov_data = {
    "Newbie": 18000,
    "Mid-level": 40000,
    "Manager": 90000
}

# Weights
GOV_WEIGHT = 0.8
NONGOV_WEIGHT = 0.2

# -----------------------------
# Weighted Calculation
# -----------------------------
def weighted_salary(level):
    return (
        gov_data[level] * GOV_WEIGHT +
        nongov_data[level] * NONGOV_WEIGHT
    )

# Compute results
results = {
    level: weighted_salary(level)
    for level in gov_data.keys()
}

# -----------------------------
# UI Display
# -----------------------------
st.subheader("💰 Estimated Monthly Salary (PHP)")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Newbie", f"₱{results['Newbie']:,.0f}")

with col2:
    st.metric("Mid-level", f"₱{results['Mid-level']:,.0f}")

with col3:
    st.metric("Manager", f"₱{results['Manager']:,.0f}")

# -----------------------------
# Details Section
# -----------------------------
with st.expander("📊 Data Sources & Methodology"):
    st.markdown("""
    **Weighting Method**
    - Government Data: 80%
    - Non-Government Data: 20%

    **Government Sources (Example)**
    - Philippine Statistics Authority (PSA)
    - DOLE

    **Non-Government Sources (Example)**
    - JobStreet
    - Glassdoor

    *Note: Values are sample estimates. Replace with real datasets if available.*
    """)

# -----------------------------
# Optional Chart
# -----------------------------
st.subheader("📈 Salary Comparison")

st.bar_chart(results)
