import streamlit as st
import pandas as pd
import plotly.express as px

import matplotlib.pyplot as plt

###############################################################################
##################### Sale value increases (yearly) ###########################
###############################################################################

st.write("""# Year-on-Year average growth rate""")

@st.cache
def get_df():
    df = pd.read_csv('data/df_sales_pivot.csv')
    return df

df = get_df().head(10)

df = df[df.index != 'Jura']

df['average_increase'] = df[['2017','2018','2019','2020','2021']].mean(axis=1)

fig = px.bar(df, df['department_name'], 'average_increase')
fig.update_layout(
    title="Top 10 Department Average Sales Value Increases (2017-2021)",
    xaxis_title="Department",
    yaxis_title="Avg sales value increase",
    font=dict(
        family="Courier New, monospace",
        size=13,
        color="RebeccaPurple"
    ))
fig.update_xaxes(tickangle=45)

st.plotly_chart(fig)
