# -*- coding: utf-8 -*-
"""
Spyder Editor

Tan Jing Long
1st November 2021

This is a Python script for deployment on Streamlit.

The Streamlit app is intended to digitise the classic pendulum experiment we perform in secondary school, particularly for the data tabulation and analysis aspects.

The content for the pendulum experiment is standard. Here, I have adapted it from Physics Matters Practical Book (3rd ed.) by Charles Chew and Ho Boon Tiong.
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import streamlit as st
from sklearn.linear_model import BayesianRidge, LinearRegression, ARDRegression
from sklearn.metrics import mean_squared_error
from PIL import Image

st.title('Pendulum Experiment')
st.header('Part I: Data Collection')
st.write('In Part I of the experiment, you will be physically performing the experiment and collecting the data in the laboratory.')

st.markdown('1. From the fitted graph, estimate the length of the pendulum that will yield a period of 2.0 s')
st.markdown('2. The formula for the period of a pendulum is $2\pi\sqrt{l/g}$, where $l$ is the length of the pendulum, and $g$ an unknown constant. Derive the value of the physical constant $g$, including its units and comment on its physical significiance.')

    
