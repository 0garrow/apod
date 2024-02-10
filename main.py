import requests
import streamlit as st

api_key = "LXgCDumRYz9nEapRiuSXrm00urHarnFdOhmb14Zb"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

response = requests.get(url)
data = response.json()

image_response = requests.get(data['url'])

with open("image.jpg", "wb") as file:
    file.write(image_response.content)


st.title(data['title'])

st.image("image.jpg")

st.write(data['explanation'])
