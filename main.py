import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import streamlit as st
from function_utils import *

st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(page_title='Analysis of multivariate data - NHANES case study', page_icon="./f.png")
st.title('Analysis of multivariate data - NHANES case study')
st.subheader('By [Francisco Tarantuviez](https://www.linkedin.com/in/francisco-tarantuviez-54a2881ab/) -- [Other Projects](https://franciscot.dev/portfolio)')
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.write('---')
st.write("""
  The purpose of this app is analyse the data from [NHANES](https://www.cdc.gov/nchs/nhanes/index.htm) survey. It contains a lot of different health statistics such as blood pressure, BMI, etc. and demographic one like gender, education level and so on. 
  We illustrate several basic techniques for exploring data using methods for understanding multivariate relationships.

  Consider this project as a sort of second part of [TODO](https://franciscot.dev), where I analysed the same data but as univariate analysis.
""")

def load_data():
  return pd.read_csv("https://raw.githubusercontent.com/ftarantuviez/Data/main/nhanes_2015_2016.csv")
df = load_data()

nhanes_multivariate_analysis(df)

# This app repository

st.write("""
## App repository

[Github](https://github.com/ftarantuviez/)TODO
""")
# / This app repository