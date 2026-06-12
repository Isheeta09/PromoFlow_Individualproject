# PromoFlow: Promotion Effectiveness and Demand Forecasting Dashboard

## Project Overview

PromoFlow is a machine learning-powered decision support application developed as part of the Data Science for Business minor at HAN University of Applied Sciences.

The project explores how promotional activities influence product demand and inventory-related decision-making. By combining demand forecasting, promotion analytics, and business intelligence concepts, PromoFlow enables users to simulate promotional scenarios and generate sales forecasts through an interactive Streamlit dashboard.

The project follows the CRISP-DM methodology and incorporates concepts from pharmaceutical supply chains, retail demand forecasting, machine learning, and data storytelling.

---

## Project Objectives

The primary objective of this project was to investigate how machine learning can support promotion planning and demand forecasting.

Specific objectives included:

* Exploring forecasting challenges within pharmaceutical and retail environments.
* Reviewing academic literature and industry practices related to forecasting and supply chain management.
* Evaluating multiple datasets and forecasting approaches.
* Developing a machine learning model capable of predicting future sales.
* Building an interactive Streamlit dashboard.
* Translating model outputs into practical business insights.
* Demonstrating the complete CRISP-DM lifecycle from business understanding to deployment.

---

## Business Context

Accurate demand forecasting is essential for balancing inventory availability with operational efficiency. Poor forecasting can result in stock shortages, excess inventory, lost sales, and increased costs.

This challenge becomes even more complex when promotions are introduced. Discounts and marketing campaigns can significantly influence customer behaviour, making future demand difficult to predict.

PromoFlow was developed to explore how machine learning can assist with these forecasting challenges by allowing users to evaluate promotional scenarios before implementation.

---

## CRISP-DM Methodology

The project was developed using the CRISP-DM framework:

1. Business Understanding
2. Data Understanding
3. Data Preparation
4. Modelling
5. Evaluation
6. Deployment

This methodology provided a structured approach for dataset exploration, feature engineering, model development, evaluation, and dashboard deployment.

---

## Datasets

### Final Datasets Used

#### Pharma Sales Data

Source:
https://www.kaggle.com/datasets/milanzdravkovic/pharma-sales-data

Purpose:

* Provided pharmaceutical industry context.
* Supported exploration of forecasting challenges within pharmaceutical supply chains.
* Contributed to the business understanding phase of the project.

#### Retail Pricing and Demand Signals Dataset

Source:
https://www.kaggle.com/datasets/sudipmanchare/retail-pricing-and-demand-signals-dataset

Purpose:

* Primary modelling dataset.
* Contains pricing, demand, promotion, inventory, and sales-related variables.
* Used for feature engineering, model training, and dashboard predictions.

### Additional Datasets Explored

#### Rossmann Store Sales

https://www.kaggle.com/competitions/rossmann-store-sales

Explored because:

* Widely used demand forecasting dataset.
* Contains promotion and sales variables.

Not selected because:

* Limited inventory-related information.

#### Online Retail Dataset (UCI)

https://archive.ics.uci.edu/ml/datasets/online+retail

Explored because:

* Contains detailed historical transaction data.

Not selected because:

* Limited promotional and inventory variables.

---

## Machine Learning Approach

Several modelling approaches were explored during the project, including:

* Linear Regression
* Decision Trees
* Random Forest
* Gradient Boosting
* XGBoost (reviewed during exploration)

The final model selected was a Random Forest Regressor.

Random Forest was chosen because it:

* Handles non-linear relationships effectively.
* Works well with mixed categorical and numerical variables.
* Provides robust predictive performance.
* Is relatively easy to deploy within an MVP environment.

The trained model is stored as:

```text
rf_model.pkl
```

---

## MVP Features

The final Streamlit dashboard includes:

### Demand Forecasting

Users can generate sales predictions based on:

* Product information
* Pricing variables
* Discount percentages
* Promotion type
* Inventory level
* Demand indicators
* Seasonal information

### Revenue Estimation

The application estimates expected revenue based on predicted sales and pricing inputs.

### Inventory Risk Assessment

The dashboard provides simple inventory risk indicators designed to support decision-making.

### Interactive Scenario Analysis

Users can modify inputs and immediately observe the impact on forecast outcomes.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Joblib
* Streamlit
* Matplotlib

---

## Repository Structure

```text
PromoFlow/
│
├── PromoFlow.ipynb
├── app.py
├── rf_model.pkl
├── requirements.txt
├── README.md
├── report.pdf
└── screenshots/
```

---

## Installation

### Step 1 – Clone Repository

```bash
git clone [REPOSITORY_URL]
```

### Step 2 – Install Requirements

```bash
pip install -r requirements.txt
```

### Step 3 – Run Application

```bash
streamlit run app.py
```

The dashboard will open automatically in your browser.

---

## Project Deliverables

This repository contains:

* Complete Jupyter Notebook
* Trained Machine Learning Model
* Streamlit MVP Dashboard
* Project Report
* Documentation

---

## Video Demonstration

YouTube Video:

[INSERT YOUTUBE LINK]

---

## Author

Isheeta [Surname]

Data Science for Business Minor

HAN University of Applied Sciences

2025
