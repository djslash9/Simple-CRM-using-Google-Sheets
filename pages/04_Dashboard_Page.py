# Contents of ~/my_app/pages/page_3.py
import streamlit as st

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
cred = ServiceAccountCredentials.from_json_keyfile_name("cams2022-f38431cfe8d6.json",scope) 

# authorize the clientsheet 
client = gspread.authorize(cred)

# get the sample of the Spreadsheet
sheet = client.open('CAMS')

# get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(0)

st.set_page_config(page_title="CAMS", page_icon="🐞", layout="centered")

st.markdown("# DASHOBOARD 🎉")
st.sidebar.markdown("# Dashboard Page 🎉")

st.markdown('_This is for the analysis part.  Real time visual output_') # see *


st.title("Customer Management Sysytem 2.0")