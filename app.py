import streamlit as st
import pandas as pd
import plotly.express as px

st.image('data/prello.png',width=450)

###############################################################################
################### Bubble chart for department & metrics #####################
###############################################################################

st.markdown('''
## Bubble chart showing relationship between department & metrics of interest
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
        size=15,
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
        size=15,
        color="RebeccaPurple"
    ))
    fig.update_xaxes(tickangle=45)

st.plotly_chart(fig)

###############################################################################
################### Bubble chart for department & metrics #####################
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
    title="Secondary home rate by department<br><sup>Bubble size indicates sales price per m2</sup><br>",
    xaxis_title="Department",
    yaxis_title="Secondary home rate",
    font=dict(
        family="Courier New, monospace",
        size=15,
        color="RebeccaPurple"
    ))

st.plotly_chart(fig2)


# ax.set_title('Top 10 Departments with the Biggest Sales Value Increase', fontsize=16)
# ax.set_xlabel('Mean Percentage Change in Sales Growth', fontsize=14)
# ax.set_ylabel('Department', fontsize=14)
# plt.show()
