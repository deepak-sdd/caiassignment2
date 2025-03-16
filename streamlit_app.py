import streamlit as st
import requests
import os
os.environ["KERAS_BACKEND"] = "tensorflow"
import keras
import tensorflow as tf
from keras import layers
import matplotlib.pyplot as plt
import numpy as np
from keras.callbacks import Callback
from keras.applications import InceptionV3
from scipy.linalg import sqrtm
from PIL import Image
import tensorflow as tf
from skimage.transform import resize

API_URL = "https://your-deployed-flask-app.com/api/rag/chat"  # Replace with your actual deployed API URL

st.title("CAI Assignment 2 - Group #75 Chatbot")

user_input = st.text_input("Type your message:")

if st.button("Send"):
    with st.spinner("Processing..."):
        response = requests.post(API_URL, json={"message": user_input})
        bot_reply = response.json().get("reply", "Error processing request.")
    
    st.write(f"**Bot:** {bot_reply}")
