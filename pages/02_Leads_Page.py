#Read json file
import json
#Install Library
import streamlit as st
import numpy as np
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

import google_auth_httplib2
import httplib2

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import HttpRequest

GSHEET_URL = "https://docs.google.com/spreadsheets/d/1FXYbgs8kAk0DoaLyMOufpHBuWTODxLBTq3WueyrTfao/edit#gid=0"

# defining the scope of the application
# scope_app = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive'] 

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive',
         'https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/spreadsheets']


#credentials to the account
cred = ServiceAccountCredentials.from_json_keyfile_name('cams2022-f38431cfe8d6.json',scope) 

# authorize the clientsheet 
client = gspread.authorize(cred)

# get the sample of the Spreadsheet
sheet = client.open('CAMS')

# get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(0)

st.set_page_config(page_title="CAMS", page_icon="🐞", layout="centered")

st.title("Customer Management Sysytem 2.0")

st.sidebar.write(f"Customer Management System 1.0")

st.subheader("🐞 New Leads")

form = st.form("checkboxes", clear_on_submit = True)
with form:
    cols = st.columns((1, 1, 1))
    Lead_Date = cols[0].date_input("Date:")
    Cust_Name = cols[1].text_input("Name:")
    Cust_Phone = cols[2].text_input("Phone:")
    
    cols = st.columns((1, 1, 1))
    Cust_Email = cols[0].text_input("Email:")
    Cust_City = cols[1].text_input("City:")
    
    cols = st.columns((1, 1, 1))
    Lead_Source = cols[0].selectbox(
        "Lead Source:", ["Facebook", "Website", "Touch", "Email", "Other"], index=1
    )
    Lead_Name = cols[1].selectbox(
        "Lead Name:", ["Call & Go", "Healthcare", "SME", "Home", "Travel", "Commercual"], index=0
    )
    Lead_Type = cols[2].selectbox(
        "Lead Type:", ["Motor", "Fire", "Medical", "Miscellaneous", "Marine"], index=0
    )

    cols = st.columns(2)
    submitted = st.form_submit_button(label="Submit")
    
if submitted:
    #row = [str(Lead_Date), Cust_Name, Cust_Phone, Cust_Email, Cust_City, Lead_Source, Lead_Name, Lead_Type]
    #index = 2
    #sheet_instance.insert_row(row, index)
        
    st.success("Thanks! Your lead was recorded.")
    st.balloons()
    
expander = st.expander("See all records")   
 
st.write(f"Open original [Google Sheet]({GSHEET_URL})")
# get all the records of the data
records = sheet_instance.get_all_records()
# convert the json to dataframe
records_df = pd.DataFrame.from_dict(records)

df = records_df.astype(str)
st.dataframe(df)