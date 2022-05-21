# -*- coding: utf-8 -*-
"""
Created on Sat May 21 09:02:40 2022

@author: Hp
"""

import streamlit as st
import pandas as pd
from gsheetsdb import connect

st.title("My First Streamlit Web App")

df = pd.DataFrame({"one": [1, 2, 3], "two": [4, 5, 6], "three": [7, 8, 9]})
st.write(df)

st.title("Connect to Google Sheets")
gsheet_url = "https://docs.google.com/spreadsheets/d/1_ccm9z_hr0o_Q6qpgE1PfgWnwlfTTMmElTKd92ZP09E/edit?usp=sharing"
conn = connect()
rows = conn.execute(f'SELECT * FROM "{gsheet_url}"')
df_gsheet = pd.DataFrame(rows)
st.write(df_gsheet)