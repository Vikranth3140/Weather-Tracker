import os
import requests
import streamlit as st

api_key = "1c4aaa597dd29ba9c44da6839c89fbf6"

st.title("Weather Tracker☁️")
prompt = st.text_input("Which city do you want to know the weather of?")

base_url = "http://api.openweathermap.org/data/2.5/weather?"
complete_url = base_url + "appid=" + api_key + "&q=" + prompt

print("The url you are being directed to: " + complete_url)

if prompt:
    response = requests.post(complete_url, json={"prompt": prompt})
    if response.status_code == 200:
        response_text = requests.get(complete_url).json()
        
        st.write("The weather in " + prompt + " is:")
        st.write()

        for i in response_text.keys():
            if i == "main":
                st.write(response_text.get(i))
            if i == "weather":
                st.write(response_text.get(i)[0].get("description"))
            if i == "wind":
                st.write(response_text.get(i).get("speed"))

    else:
        st.write("Please give a correct city name.")