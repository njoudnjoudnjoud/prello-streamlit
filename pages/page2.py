import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_extras.colored_header import colored_header

###############################################################################
######################## Secondary Home Rate v. POI ###########################
###############################################################################

st.write("""# Secondary home rate""")


@st.cache
def get_dfsecpoi():
    df = pd.read_csv('data/dfsecpoi_grouped.csv')
    return df

df = get_dfsecpoi()

fig = px.scatter(df, x= 'department_name' , y= "secondary_home_rate", size="poi")
fig.update_layout(
    title="Bubble size indicates no. of POIs",
    xaxis_title="Department",
    yaxis_title="Secondary home rate (%)",
    font=dict(
        family="Courier New, monospace",
        size=13,
        color="RebeccaPurple"
    ))
fig.update_xaxes(tickangle=45)

st.write("""#### Secondary home rate by department & POIs (places of interest)""")
st.plotly_chart(fig)
