

import streamlit as st
import pandas as pd
import joblib

# --------------------------------------------------
# LOAD FILES
# --------------------------------------------------

df = pd.read_csv("promo_mvp_dataset_clean.csv")

model = joblib.load("promoflow_model.pkl")
encoders = joblib.load("encoders.pkl")
model_features = joblib.load("model_features.pkl")

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="PromoFlow",
    page_icon="📈",
    layout="wide"
)

st.title("📈 PromoFlow")
st.subheader(
    "Promotion Effectiveness & Demand Forecasting Dashboard"
)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.header("Promotion Scenario")

product = st.sidebar.selectbox(
    "Product",
    sorted(df["product_id"].unique())
)

region = st.sidebar.selectbox(
    "Region",
    sorted(df["region"].unique())
)

brand = st.sidebar.selectbox(
    "Brand",
    sorted(df["brand"].unique())
)

promotion = st.sidebar.selectbox(
    "Promotion Type",
    sorted(df["promotion_type"].unique())
)

discount = st.sidebar.slider(
    "Discount %",
    0,
    50,
    15
)

inventory = st.sidebar.slider(
    "Inventory Level",
    0,
    200,
    50
)

# --------------------------------------------------
# BUSINESS OVERVIEW
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Revenue",
    f"${df['revenue'].mean():,.0f}"
)

col2.metric(
    "Average Units Sold",
    f"{df['units_sold'].mean():.1f}"
)

col3.metric(
    "Average Inventory",
    f"{df['inventory_level'].mean():.0f}"
)

st.divider()

# --------------------------------------------------
# SCENARIO CREATION
# --------------------------------------------------

sample = df.iloc[0].copy()

sample["product_id"] = product
sample["region"] = region
sample["brand"] = brand
sample["promotion_type"] = promotion
sample["discount_pct"] = discount
sample["inventory_level"] = inventory

prediction_df = pd.DataFrame([sample])

# Encode exactly as notebook

for col in encoders:
    if col in prediction_df.columns:
        prediction_df[col] = encoders[col].transform(
            prediction_df[col]
        )

prediction_df = prediction_df.reindex(
    columns=model_features,
    fill_value=0
)

predicted_sales = model.predict(prediction_df)[0]

# --------------------------------------------------
# KPI SECTION
# --------------------------------------------------

# --------------------------------------------------
# DECISION SUPPORT KPIs
# --------------------------------------------------

average_price = sample["revenue"] / max(sample["units_sold"], 1)

expected_revenue = predicted_sales * average_price

# Stock cover ratio
stock_cover = inventory / max(predicted_sales, 1)

# Inventory risk assessment
if stock_cover < 1:
    inventory_risk = "HIGH"

elif stock_cover < 3:
    inventory_risk = "MEDIUM"

else:
    inventory_risk = "LOW"

# Business recommendation engine
if inventory_risk == "HIGH":

    recommendation = (
        "High stockout risk. Increase inventory before launching promotion."
    )

elif inventory_risk == "MEDIUM":

    recommendation = (
        "Moderate inventory risk. Monitor inventory closely during promotion."
    )

elif discount >= 35:

    recommendation = (
        "Promotion likely to drive demand but may negatively impact margins."
    )

else:

    recommendation = (
        "Promotion recommended under current operating conditions."
    )

# --------------------------------------------------
# RESULTS
# --------------------------------------------------
st.header("Forecast Results")

k1, k2, k3, k4 = st.columns(4)

k1.metric(
    "Predicted Units Sold",
    f"{predicted_sales:.1f}"
)

k2.metric(
    "Expected Revenue",
    f"${expected_revenue:,.0f}"
)

k3.metric(
    "Inventory Risk",
    inventory_risk
)

k4.metric(
    "Stock Cover",
    f"{stock_cover:.1f}x"
)

# --------------------------------------------------
# HISTORICAL DATA
# --------------------------------------------------

st.header("Historical Performance")

filtered = df[
    (df["product_id"] == product)
]

st.dataframe(filtered.head(20))

# --------------------------------------------------
# REVENUE TREND
# --------------------------------------------------

st.header("Revenue Trend")

if len(filtered) > 0:
    st.line_chart(filtered["revenue"])

# --------------------------------------------------
# ABOUT
# --------------------------------------------------

st.header("About PromoFlow")

st.markdown(
"""
PromoFlow is a machine learning decision-support system designed
to evaluate promotional effectiveness and forecast expected sales.

Users can simulate promotional scenarios by adjusting:

- Product
- Region
- Brand
- Promotion Type
- Discount Percentage
- Inventory Level

The Random Forest model estimates expected demand and supports
data-driven promotional planning decisions.
"""
)