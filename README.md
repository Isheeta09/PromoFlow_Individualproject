PromoFlow
Project Information
Module: DATDRD05-T08 – Data Science Tools and Techniques
Assignment: Individual Project
Student: Isheeta Mishrra
Academic Year: 2025–2026
 
⸻
Project Overview
PromoFlow is a machine learning and decision-support application developed to explore the relationship between promotions, demand forecasting and inventory planning.
The project investigates how promotional activities can influence future demand and how machine learning can support inventory-related decision making. The application was developed following the CRISP-DM methodology and combines demand forecasting with inventory recommendations through an interactive Streamlit dashboard.
The project was inspired by challenges commonly encountered in pharmaceutical and retail supply chains, where organisations must balance product availability with inventory costs while managing uncertainty created by promotional campaigns.
⸻
 
Repository Contents
This repository contains:
* PromoFlow.ipynb – Jupyter Notebook containing data exploration, preprocessing, modelling, evaluation and explanation in Markdown. 
* new_version.py – Streamlit dashboard application.
* requirements.txt – Required Python libraries.
* README.md – Project documentation.

⸻
 
Datasets Used
Pharma Sales Dataset
Source: https://www.kaggle.com/datasets/milanzdravkovic/pharma-sales-data
Purpose:
* Demand forecasting exploration
* Pharmaceutical industry context
* Sales trend analysis
Retail Pricing and Demand Signals Dataset
Source: https://www.kaggle.com/datasets/sudipmanchare/retail-pricing-and-demand-signals-dataset
Purpose:
* Promotion analysis
* Demand forecasting
* Inventory planning experimentation
 
⸻
 
Running the Application
Step 1 – Install Dependencies
Open a terminal and run:
pip install -r requirements.txt

Step 2 – Download Supporting Files
Due to GitHub file size limitations, the trained model and supporting files are stored separately.
Google Drive Folder:
https://drive.google.com/drive/folders/1B6tByHHS03OFtX4eIX1EPqcT8K3GwEwH?usp=share_link

Download the following files and place them in the same directory as new_version.py:
* promoflow_model.pkl
* encoders.pkl
* model_features.pkl
* promo_mvp_dataset_clean.csv

Step 3 – Run the Application
Open a terminal and run:
streamlit run new_version.py
The application will launch locally in your browser.
 
⸻ 
Video Demonstration
YouTube Video:
 https://youtu.be/P-UODSOMo2s

The video demonstrates the complete functionality of the application, including data exploration, model development and dashboard usage.
 
⸻ 
Notes
The application was successfully developed and demonstrated locally. Due to file-size constraints associated with hosting large machine learning model files, deployment through Streamlit Community Cloud was not included in the final submission. All files required to reproduce the project are provided through the GitHub repository and accompanying Google Drive folder.
 
⸻ 
Author
Isheeta Mishrra
HAN University of Applied Sciences
DATDRD05-T08 – Data Science Tools and Techniques
2025–2026
