import streamlit as st
import requests as rq
server_url=st.secrets("screct_ur")
st.title("AI_WEATHER_FORECASTING")
city=st.text_input("enter city")
question=st.text_input("ask your question..")
if st.button("ask ai"):
    res=rq.post(f"{server_url}/get_weather",params={
        "city":city,
        "question":question
    })
    st.success(res.json()["messages"][-1]["content"])

