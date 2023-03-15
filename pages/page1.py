import streamlit as st
import pandas as pd
import plotly.express as px

###############################################################################
################### Year on year sales growth by department ###################
###############################################################################

@st.cache
def load_yoy_df():
    df = pd.read_csv('data/yoy_sales_growth.csv')
    return df

yoy_sales_df = load_yoy_df()

yoy_sales_df.sort_values(by='yoy_sales_growth', ascending=False).head(10)

fig2 = px.bar(yoy_sales_df, x="department_name"
              , y="yoy_sales_growth"
              , orientation='h')
fig2.update_layout(
    title="Top 10 Departments with the Biggest Sales Value Increase",
    xaxis_title="Mean Percentage Change in Sales Growth",
    yaxis_title="Department",
    font=dict(
        family="Courier New, monospace",
        size=15,
        color="RebeccaPurple"
    ))
fig2.update_xaxes(tickangle=45)

st.plotly_chart(fig2)
