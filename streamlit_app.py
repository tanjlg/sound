# -*- coding: utf-8 -*-
"""
Spyder Editor

Tan Jing Long
15 January 2023

This is a Python script for deployment on Streamlit.

The Streamlit app is intended to digitise an inquiry activity we perform in secondary school, particularly for the data tabulation and analysis aspects.

The students will be investigating the relationship between frequency and length.
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import streamlit as st
from sklearn.linear_model import BayesianRidge, LinearRegression, ARDRegression
from sklearn.metrics import mean_squared_error
from PIL import Image

st.title('Sound Activity')
st.header('Part I: Experimental Set-Up')
st.write('In Part I of the experiment, you will be physically performing the experiment and collecting the data in the laboratory.')

st.subheader('Aim')
st.write('To investigate the relationship between the length of a string and the frequency of the sound produced when struck, for a string under tension.')

st.subheader('Apparatus')
st.write('Retort stand  \n',
         'Sets of boss and clamp  \n',
         'Metre rule  \n',
         'Wooden blocks  \n',
         'Tuning fork  \n',
         'Ukelele')

st.subheader('Procedure')
st.markdown(
"""
Analyse the problem and produce an appropriate plan for your investigation. In your plan, you should:
- state the problem you are investigating
- list all variables (variables to be kept constant and those to be changed)
- write your suggested procedure as a series of step-by-step instructions
- describe how data collected are processed
- include diagram(s) of the investigation set-up
- any safety precautions
"""
)

st.header('Part II: Data Collection')

length, freq1, freq2, period, length_inv = np.zeros(8, dtype=np.float16), np.zeros(8, dtype=np.float16), np.zeros(8, dtype=np.float16), np.zeros(8, dtype=np.float16), np.zeros(8, dtype=np.float16)

length[0] = st.number_input('Measure the length of the string under tension',
                     value=100.0, step=0.1)
st.markdown("4. Record the frequency $f_1$ of the sound produced by the string, using the Phyphox app, as indicated by the peak of the Fast Fourier Transform (FFT)")
freq1[0] = st.number_input(label='First reading', step=0.1)

df = pd.DataFrame({'length/cm': length, 'f/Hz': freq1, 'T/s': period, '1/T/Hz': freq2, '1/L/cm-1': length_inv})
st.write(df)
