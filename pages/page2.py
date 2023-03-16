import streamlit as st
import pandas as pd
import plotly.express as px

###############################################################################
######################## Secondary Home Rate v. POI ###########################
###############################################################################

st.write("""# Secondary home rate by department & POI (places of interest)""")


@st.cache
def get_dfsecpoi():
    df = pd.read_csv('data/dfsecpoi_grouped.csv')
    return df

df = get_dfsecpoi()

fig = px.scatter(df, x= 'department_name' , y= "secondary_home_rate", size="poi")
fig.update_layout(
    title="Secondary home rate by department<br><sup>Bubble size indicates no. of POIs</sup><br>",
    xaxis_title="Department",
    yaxis_title="Secondary home rate (%)",
    font=dict(
        family="Courier New, monospace",
        size=13,
        color="RebeccaPurple"
    ))
fig.update_xaxes(tickangle=45)

st.plotly_chart(fig)
