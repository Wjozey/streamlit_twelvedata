import streamlit as st
import pandas as pd
import numpy as np
import requests
import config
import plotly.express as px

# api_key = config.twelve_api
api_key = st.secrets["API_URL"]


st.title('Finance Chart')
st.write('---')

tickers = ('AAPL', 'TSLA', 'GOOGL')
symbol = st.sidebar.selectbox("Pick your assets", tickers )

start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2021-01-31", format="%Y-%m-%d"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("today", format="%Y-%m-%d"))

    
r = requests.get(f"https://api.twelvedata.com/time_series?&start_date={start_date}&end_date={end_date}&symbol={symbol}&interval=1day&apikey={api_key}")

data = r.json()
df = pd.DataFrame(data['values'])
st.write(df)

st.write('---')
st.title("Closing Price")
st.write('---')



line_chart_data = df.copy()
line_chart_data['datetime'] = pd.to_datetime(line_chart_data['datetime'])
line_chart_data['close'] = pd.to_numeric(line_chart_data['close'])


fig = px.line(line_chart_data,x='datetime', y='close', title='Stock Price Trend')
fig.update_layout(
    showlegend=False,
    width=800,
    height=500,
    margin=dict(l=1,r=1,b=1,t=1),
    font=dict(color='#32a8a4', size=15)
)
fig.update_xaxes(rangeslider_visible=True)
st.write(fig)
