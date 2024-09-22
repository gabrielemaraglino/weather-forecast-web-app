import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the next days")
place = st.text_input("Place: ")
days  = st.slider("Forecast Days", min_value=1, max_value=5,
                  help="Select the number of days to forecast")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"Temperature for the next {days} days in {place}")

data = get_data(place, days, option)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"},)
st.plotly_chart(figure)
