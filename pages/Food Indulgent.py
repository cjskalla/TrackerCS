import streamlit as st
import pandas as pd
from datetime import datetime
import numpy as np

st.set_page_config(layout="centered", page_title="Food Indulgence", page_icon=":cookie:")


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



# Get today's date and format it as YYYY-MM-DD
today = datetime.today().date()

#Bring in the Indulge Data
indulge = pd.read_excel('C:/Users/Calvin/Documents/TrackerCS/Trackers/FoodIndulgentDB.xlsx',
                        sheet_name='FoodIndulgent',
                        dtype = {
                            'Food Type' : 'str',
                            'Merchant' : 'str',
                            'Cost' : 'float64'
                        }
                    )

indulge['Date'] = pd.to_datetime(indulge['Date'])

# Get max date to assure to not duplicate today
max_date = indulge['Date'].max()


if max_date != today:
    
    today_df =  pd.DataFrame({'Date': [today], 'Food Type': [np.nan], 'Merchant': [np.nan], 'Cost': [np.nan]})

    # Concatenate the original DataFrame with the missing rows
    indulge_df = pd.concat([indulge, today_df], ignore_index=True)

    max_date = indulge_df['Date'].max()


with st.form("data_editor_form"):
    edited_indulge_df = st.data_editor(indulge_df,
                                    disabled=['Date'],
                                    hide_index=True,
                                    num_rows='dynamic',
                                    use_container_width=True)

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

    confirm = st.form_submit_button("Confirm")

if confirm:
    indulge_df.to_excel('C:/Users/Calvin/Documents/TrackerCS/Trackers/FoodIndulgentDB.xlsx',
                        sheet_name='FoodIndulgent',
                        index=False)
    
    st.text("Changes Made to Sheet")