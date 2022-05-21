# -*- coding: utf-8 -*-
"""
Created on Sat May 21 09:02:40 2022

@author: Hp
"""

import streamlit as st
import pandas as pd



st.title("My First Streamlit Web App")

df = pd.DataFrame({"one": [1, 2, 3], "two": [4, 5, 6], "three": [7, 8, 9]})
st.write(df)

