import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_extras.colored_header import colored_header

st.image('data/prello.png',width=450)

###############################################################################
################### Bubble chart for department & metrics #####################
###############################################################################

st.write('')

st.markdown('''
#### Sales price / secondary home rate by department
''')

st.write('')

@st.cache
def load_df():
    df = pd.read_csv('data/dfsalessec_group.csv')
    return df

df = load_df()

option = st.selectbox(
    'Please select the variable you want to show on the y-axis',
    ('Sale price per m2', 'Secondary home rate'))

st.write('')

if option == 'Sale price per m2':
    fig = px.scatter(df, x= 'department_name'
                     , y= "sales_price_m2"
                     , size="secondary_home_rate"
                     , width = 750, height = 600)
    fig.update_layout(
    title="Sales price by department<br><sup>Bubble size indicates secondary home rate</sup><br>",
    xaxis_title="Department",
    yaxis_title="Sales price per m2",
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="RebeccaPurple"
    ))
    fig.update_xaxes(tickangle=45)

if option == 'Secondary home rate':
    fig = px.scatter(df, x= 'department_name'
                     , y= 'secondary_home_rate'
                     , size="sales_price_m2"
                     , width = 750, height = 600)
    fig.update_layout(
    title="Secondary home rate by department<br><sup>Bubble size indicates sales price per m2</sup><br>",
    xaxis_title="Department",
    yaxis_title="Secondary home rate",
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="RebeccaPurple"
    ))
    fig.update_xaxes(tickangle=45)

st.plotly_chart(fig)
