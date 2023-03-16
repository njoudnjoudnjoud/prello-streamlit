import streamlit as st
import pandas as pd
import plotly.express as px

###############################################################################
##################### Sale value increases (yearly) ###########################
###############################################################################

st.write("""# Average sales growth""")

@st.cache
def get_df():
    df = pd.read_csv('data/df_sales_pivot.csv')
    return df

df = get_df()
df = df[df.index != 'Jura']
df['average_increase'] = df[['2017','2018','2019','2020','2021']].mean(axis=1)

##################### Top 10 ###########################

df_top10 = df.head(10)
df_top10.sort_values(by='average_increase',inplace=True)

fig1 = px.bar(df_top10, df_top10['department_name'], 'average_increase')
fig1.update_layout(
    xaxis_title="Department",
    yaxis_title="Avg sales value increase",
    font=dict(
        family="Courier New, monospace",
        size=13,
        color="RebeccaPurple"
    ))
fig1.update_xaxes(tickangle=45)

st.write("""#### Top 10 Department by average yearly sales value increases from 2017 to 2021""")
st.plotly_chart(fig1)
