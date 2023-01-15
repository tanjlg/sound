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

st.subheader('Method 1: Fast Fourier Transform')
st.markdown("Record the frequency $f_1$ of the sound produced by the string, using the Phyphox app, as indicated by the peak of the FFT.")
freq1[0] = st.number_input(label='Frequency reading', step=0.1)

st.subheader('Method 2: Period Measurement')
st.markdown("Record the period $T$ of the sound produced by the string, using the Audio Scope function of the Phyphox app.")
period[0] = st.number_input(label='Period reading', step=0.1)

df = pd.DataFrame({'length/cm': length, 'f/Hz': freq1, 'T/s': period, '1/T /Hz': freq2, '1/L /cm-1': length_inv})
st.write(df)

@st.cache
def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv().encode('utf-8')

csv_raw = convert_df(df)
st.download_button(
     label="Download the tabulated data as CSV",
     data=csv_raw,
     file_name='data_raw.csv',
     mime='text/csv',
 )


st.header('Part III: Data Analysis')
st.write('In Part III of the experiment, you will be processing the collected data and inferring the relationship between the period and length of the pendulum.')

st.markdown("7. By using an Excel Spreadsheet or otherwise, calculate $1/L /cm$ and record it in the corresponding entry in the CSV file.")

data_com = st.file_uploader("Upload the csv file with the inputted raw data and the derived quantities you computed.")
N = 8 # for computing root-mean-squared error

if data_com is not None:
  df = pd.read_csv(data_com)
  st.write(df)
  freq = df['f/Hz']
  length_inv = df['1/L /cm-1']
  N = np.count_nonzero(T2)

freq = df['f/Hz']
length_inv = df['1/L /cm-1']
         
st.markdown("Plot the graph of $f/$Hz against $\frac{1}{L}/$cm$^{-1}$.")
fig, ax = plt.subplots()
plt.plot(length-inv, freq, 'x', markersize=3)
plt.title('Scatterplot of Period squared against length of the pendulum')
plt.xlim(0,120)
plt.ylim(0,4.5)
plt.grid(b=True)
plt.xlabel('1 / Length of Pendulum/ cm-1')
plt.ylabel('Frequency/ Hz')

if st.button('Plot'):
    st.pyplot(fig)
    
st.markdown('10. By manipulating the line to minimise the error value, deduce the relationship between the period $T$ and length $l$ of the pendulum. The root-mean-square error (RMSE) is similar to the standard deviation of a dataset except that it calculates the sum of squared distances from the hypothesised interpolated period squared $\hat{T^2}$ instead of the mean $<T^2>$.')
m = st.slider('Gradient', min_value=0.00, max_value=0.10, value=0.04, step=0.0001)
c = st.slider('Intercept (vertical)', min_value=-0.20, max_value=0.20, value=0.0, step=0.01)
# root-mean-square deviation error
residuals = freq-(m*length-inv+c)
sum_squared_error = np.sum(residuals**2)
rms_error= np.sqrt(sum_squared_error/N)
st.write('Error: ')
st.write(rms_error)

plt.plot(length-inv, m*length+c)
plt.title('Linear fit of Period squared against length of the pendulum')
plt.xlim(0,120)
plt.ylim(0,4.5)     
st.pyplot(fig)
