import pandas as pd
import streamlit as st

rulesData = pd.read_csv("rules.csv")
rawData = pd.read_csv("Groceries_dataset.csv")
recommendedItems = pd.DataFrame()

product_choose = st.selectbox(label="select product to choose the recommendation", key="chooseFromDropDown", options=pd.unique(rulesData['antecedents']))

if product_choose is not None:
    filteredData = rulesData[rulesData['antecedents'] == product_choose]
    recommendedItems = filteredData.sort_values(by=['consequent support'])['consequents']
    recommendedItems = recommendedItems.iloc[:5].reset_index()
    # itemsToDisplay = recommendedItems['consequents'].tolist()
    st.table(recommendedItems['consequents'].values)
