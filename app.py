import requests
import streamlit as st
import time
import json
import os
import uuid
import base64
import io
from PIL import Image

# Ollama server address
url = "http://localhost:11434/api/generate"

st.set_page_config(page_title="Multimodal AI Assistant")

# Title of the Streamlit app
st.title("💬 Multimodal AI Assistant")

# Image upload field
uploaded_file = st.sidebar.file_uploader("Upload image :gear:", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    st.sidebar.image(uploaded_file, use_column_width = True, caption='Uploaded image')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input field for the prompt
prompt = st.chat_input("Message AI Assistant")

# Button to submit the prompt and image
if prompt:
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Initialize the payload
    payload = {
        "model": "llava",
        "prompt": prompt,
        "stream": False
    }

    if 'context' in st.session_state:
        payload["context"] = st.session_state['context']

    # If an image is uploaded, encode it to base64 and include it in the payload
    if uploaded_file is not None:
         # Open the image using PIL
        image = Image.open(uploaded_file)

        # Convert the image to a base64 string
        buffered = io.BytesIO()
        image.save(buffered, format=image.format)
        img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

        # Prepare the payload
        payload["images"] = [img_str]

    # Send the POST request
    response = requests.post(url, json=payload, stream=True)

    response_time = 0
    chat_response = ""
    # Check if the request was successful
    if response.status_code == 200:
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode('utf-8')
                response_part = json.loads(decoded_line)
                chat_response = response_part['response']
                eval_count = response_part['eval_count']
                eval_duration = response_part['eval_duration']
                response_time = round(eval_count / eval_duration * 10**9, 2)
                st.session_state['context'] = response_part['context']
    else:
        st.write("Failed to get a response from the server.")
        st.write(f"Response code: {response.status_code}")

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(chat_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": chat_response})
    st.write("Response time: " + str(response_time) + " second(s)")
