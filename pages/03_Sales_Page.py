#Read json file
import json
from turtle import textinput
from pyparsing import col
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

#form = st.form(key="annotation")
st.subheader("🐞 Load Record")

phon_no = str

form2 = st.form(key="Search_data")

with form2:
    phon_no = st.text_input("Phone Number of the Customer:")
    loaded = st.form_submit_button(label="Load Details")
    
if loaded:
    load = "Yes"
    records_data = sheet_instance.get_all_records()
    test = sheet_instance.col_values(3)
    rownum = test.index(phon_no) + 1
    record = sheet_instance.row_values(rownum)
    records_df = pd.DataFrame(record)
    records_df = records_df.T
    df = records_df
    st.dataframe(df)

    Name = df.iloc[0, 1]
    Phone = df.iloc[0, 2]
    Email = df.iloc[0, 3]
    City = df.iloc[0, 4]
    Lead_Source = df.iloc[0, 5]
    Lead_Name = df.iloc[0, 6]
    Lead_Type = df.iloc[0, 7]
    
    st.sidebar.write("Name: ", Name)
    st.sidebar.write("Phone:", Phone)
    st.sidebar.write("Email:", Email)
    st.sidebar.write("City:", City)
    st.sidebar.write("Lead Source:", Lead_Source)
    st.sidebar.write("Lead Name:", Lead_Name)
    st.sidebar.write("Lead Type:", Lead_Type)
    
st.subheader("🐞 Update Record")

form3 = st.form(key="Update_data", clear_on_submit = True)
with form3:
    cols = st.columns((1, 1, 1))
    phon_no = cols[0].text_input("Phone Number of the Customer:", phon_no)
    
    cols = st.columns((1, 1, 1))
    ZM_Name = cols[0].text_input("ZM Name:")
    Region = cols[1].text_input("Region:")
    SE_Name = cols[2].text_input("SE Name:")

    cols = st.columns((1, 1, 1, 1))
    SE_Branch = cols[0].text_input("SE Branch:")
    SE_Contacted = cols[1].selectbox("SE Contacted:", ["Yes", "No"], index=1)
    Quotation_Issued = cols[2].selectbox("Quotation Issued:", ["Yes", "No"], index=1)
    Awarded = cols[3].selectbox("Awarded:", ["Yes", "No"], index=1)
    
    cols = st.columns(1)
    Remarks = cols[0].text_area("Remarks:")
    
    cols = st.columns(2)
    updated = st.form_submit_button(label="Update Details")
    
if updated:
    records_data = sheet_instance.get_all_records()
    test = sheet_instance.col_values(3)
    rownum = test.index(phon_no) + 1
    sheet_instance.update_cell(rownum, 12, ZM_Name)
    sheet_instance.update_cell(rownum, 13, Region)
    sheet_instance.update_cell(rownum, 14, SE_Name)
    sheet_instance.update_cell(rownum, 15, SE_Branch)
    sheet_instance.update_cell(rownum, 16, SE_Contacted)
    sheet_instance.update_cell(rownum, 17, Quotation_Issued)
    sheet_instance.update_cell(rownum, 18, Awarded)
    sheet_instance.update_cell(rownum, 19, Remarks)
    
    st.success("Thanks! Your lead was recorded.")
    st.balloons()
     
 
st.write(f"Open original [Google Sheet]({GSHEET_URL})")
# get all the records of the data
records = sheet_instance.get_all_records()
# convert the json to dataframe
records_df = pd.DataFrame.from_dict(records)

df = records_df.astype(str)
st.dataframe(df)