import streamlit as st
import pandas as pd
import plotly.express as px

###############################################################################
################### Year on year sales growth by department ###################
###############################################################################

st.write("""# Yearly sales growth""")

@st.cache
def load_yoy_df():
    df = pd.read_csv('data/yoy_sales_growth.csv')
    return df

yoy_sales_df = load_yoy_df()

yoy_sales_df_head = yoy_sales_df.sort_values(by='yoy_sales_growth', ascending=False).head(10)

fig2 = px.bar(yoy_sales_df_head, x="department_name"
              , y="yoy_sales_growth")
fig2.update_layout(
    xaxis_title="Department",
    yaxis_title="Avg yearly sales growth (%)",
    font=dict(
        family="Courier New, monospace",
        size=13,
        color="RebeccaPurple"
    ))
fig2.update_xaxes(tickangle=45)
fig2.update_layout(yaxis_range=[0,3])

st.write("""#### Top 10 Departments with the Biggest Sales Value Increase""")
st.plotly_chart(fig2)

yoy_sales_df_tail = yoy_sales_df.sort_values(by='yoy_sales_growth', ascending=False).tail(10)

fig3 = px.bar(yoy_sales_df_tail, x="department_name"
              , y="yoy_sales_growth")
fig3.update_layout(
    xaxis_title="Department",
    yaxis_title="Avg yearly sales growth (%)",
    font=dict(
        family="Courier New, monospace",
        size=13,
        color="RebeccaPurple"
    ))
fig3.update_xaxes(tickangle=45)
fig3.update_layout(yaxis_range=[0,3])

st.write("""#### Bottom 10 departments with the smallest sales value increases""")
st.plotly_chart(fig3)
