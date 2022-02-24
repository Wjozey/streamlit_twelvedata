import streamlit as st
import pandas as pd
import numpy as np
import requests
import config

api_key = config.twelve_api


symbol = st.sidebar.selectbox("Symbol", ('AAPL', 'TSLA', 'GOOGL'), 1)

    
r = requests.get(f"https://api.twelvedata.com/time_series?&start_date=2020-01-06&end_date=2020-05-06&symbol={symbol}&interval=1day&apikey={api_key}")

data = r.json()
df = pd.DataFrame(data['values'])
st.write(df)

    # for message in data['messages']:
    #     st.image(message['user']['avatar_url'])
    #     st.write(message['user']['username'])
    #     st.write(message['created_at'])
    #     st.write(message['body'])