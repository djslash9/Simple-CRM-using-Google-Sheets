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

st.subheader("🐞 Delete Record")

form2 = st.form(key="annotation1")
with form2:
    #del_index = cols[0].text_input("Index of the record:")
    del_index = st.number_input("Index of the record:", 0)
    del_index = del_index + 2
    deleted = st.form_submit_button(label="Delete")
if deleted:
    sheet_instance.delete_row(index=del_index)
    
    st.success("Thanks! Your record was deleted. Please refresh the page to see the updated records")
    st.balloons()
    
st.write(f"Open original [Google Sheet]({GSHEET_URL})")
# get all the records of the data
records = sheet_instance.get_all_records()

# convert the json to dataframe
records_df = pd.DataFrame.from_dict(records)

df = records_df.astype(str)
st.dataframe(df)