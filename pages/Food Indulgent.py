import streamlit as st
import pandas as pd
from datetime import datetime
import numpy as np

# Get today's date and format it as YYYY-MM-DD
today = datetime.today()

#Bring in the Indulge Data
indulge = pd.read_excel('C:/Users/Calvin/Documents/TrackerCS/Trackers/FoodIndulgentDB.xlsx',
                        sheet_name='FoodIndulgent')

#Title
title = st.markdown(
        f"""
        <h3 style="
            text-align: center;
            font-weight: 400;
            font-size: 300%;
            color: white;
            ">
        Food Indulgent
        </h3>
        """,
        unsafe_allow_html=True
    )

#About
About = st.markdown(
        f"""
        <h3 style="
            text-align: center;
            font-weight: 100;
            font-size: 100%;
            color: white;
            ">
        Utilize this application to track the days that I indulge in eating food I should not be.
        </h3>
        """,
        unsafe_allow_html=True
    )



st.divider()






edited_indulge_df = st.data_editor(indulge_df,
                                    disabled=['Date'],
                                    hide_index=True)

# Styling for Button
st.markdown(""" 
            <style>
                .stButton {
                    display: flex;
                    justify-content: center;
                }
            </style>
            """, unsafe_allow_html=True
        )

confirm = st.button("Confirm",
                    key='food_inludge_confirm')

if confirm:
    indulge_df.to_excel('C:/Users/Calvin/Documents/TrackerCS/Trackers/FoodIndulgentDB.xlsx',
                        sheet_name='FoodIndulgent',
                        index=False)