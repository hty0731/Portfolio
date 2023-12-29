#!/usr/bin/env python
# coding: utf-8

# In[1]:

import time

import streamlit as st

import numpy as np
import pandas as pd

import webbrowser


### Header:
st.set_page_config(page_title='Tingyi Ho\'s Portfolio', layout='wide')
st.title('Tingyi Ho\'s Portfolio')
st.write('Always enjoy exploring insights from data and developing workable solutions to the problems')

### Summary
st.subheader('Summary')
file_path = 'summary.txt'

# Read the contents of the text file
with open(file_path, 'r') as file:
    text_content = file.read()

# Display the text using Streamlit
st.write(text_content)

### Project
st.subheader('Project')
st.write('Projects done in Columbia University and Self Side Projects')

left_column, right_column = st.columns(2)

left_column.image('youtube_trending.jpg')
left_column.write('Factors of Trending Videos using Regression Analysis')
left_column.link_button("Check it out!", "https://hty0731.github.io/Modeling/")

left_column.image('furniture.jpeg')
left_column.write('Effects of Background photo of Online Product using R')
left_column.link_button("Check it out!","https://hty0731.github.io/Research/")

left_column.image('spotify.png')
left_column.write('Spotify Song Rating Prediction using data modeling')
left_column.link_button("Check it out!","https://github.com/hty0731/Kaggle/tree/24dc4fab4ee29e6155ffdf483b0581832f52fdca/spotify%20ranking")

right_column.image('aws.jpeg')
right_column.write('Ecommerce Platform Cloud System Construction using AWS')
right_column.link_button("Check it out!","https://github.com/hty0731/AWS")

right_column.image('vehicle.jpeg')
right_column.write('USA Vehicle Population Search Engine using ETL and Flask')
right_column.link_button("Check it out!","https://github.com/hty0731/ETL")

right_column.image('house.png')
right_column.write('House Prices Prediction - Advanced Regression using python')
right_column.link_button("Check it out!","https://hty0731.github.io/Kaggle/")

### Skills
st.subheader('Skills')

col1,col2,col3,col4 = st.columns(4)
with col1:
    st.success('SQL')
    st.info('Python-Matplotlib')
    st.warning('R')

with col2:
    st.info('Python-Pandas')
    st.warning('Python-Numpy')
    st.error('Minitab')

with col3:
    st.warning('Power BI')
    st.error('Data Modeling')
    st.success('A/B Testing')

with col4:
    st.success('Tableau')
    st.info('Regression Analysis')
    st.warning('Google Analytics')

### Time line
st.subheader('Education and Professional Experiences')

from streamlit_timeline import st_timeline


items = [
    {"Title": 'Bachelor Student', "content": "National Taiwan University", "start": "2015-09", "end":"2019-06", "description":"aaa"},
    {"Title": 'Project Management Intern', "content": "Uber", "start": "2017-11","end":"2018-05"},
    {"Title": "Marketing Analytics Intern", "content": "Baidu", "start": "2018-06","end":"2018-08"},
    {"Title": "Ecommerce Sales Analyst, Key Account Supervisor", "content": "Loreal", "start": "2019-07", "end":"2022-05"},
    {"Title": "Master Student", "content": "Columbia University", "start": "2022-09", "end":"2023-12"},
    {"Title": "Data Analyst", "content": "Veritas Technologies", "start": "2023-05","end":"2023-09"},
]

timeline = st_timeline(items, groups=[], options={}, height="300px")
st.write("Click on the timeline to know more!")
st.write(timeline)


### Sidebar
st.sidebar.write('Hello! This is Ting!')
#Insert image
st.sidebar.image('gradphoto01.jpg')
#Insert words
st.sidebar.write('Wish to connect?')
email = 'th3019@columbia.edu'
linkedin_profile_url = 'https://www.linkedin.com/in/ting-yi-ho/'


# Create a button
if st.sidebar.button('Connect via email'):
    # Open the default email client
    subject = 'Invitation to connect'
    body = 'Dear Ting'
    webbrowser.open(f'mailto:{email}?subject={subject}&body={body}')
    
# Create a button
st.sidebar.link_button("Visit LinkedIn!","https://www.linkedin.com/in/ting-yi-ho/")

#if st.sidebar.button('Visit LinkedIn'):
    # Open the LinkedIn profile in a new tab
    #st.sidebar.markdown(f'<a href="{linkedin_profile_url}" target="_blank">Click for visiting LinkedIn</a>', unsafe_allow_html=True)

