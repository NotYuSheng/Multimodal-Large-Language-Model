import requests
import streamlit as st
import time
import json
import os
import uuid
import base64
from PIL import Image

# Ollama server address
url = "http://localhost:11434/api/generate"

st.set_page_config(page_title="Multimodal AI Assistant")

# Title of the Streamlit app
st.title("Multimodal AI Assistant")

# Image upload field
uploaded_file = st.sidebar.file_uploader("Upload image :gear:", type=["jpg", "png", "jpeg"])

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

# Directory to save uploaded images
UPLOAD_DIR = os.path.join(os.getcwd(), "tmp")
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR, exist_ok=True)

session_prompts = []
session_responses = []

# Input field for the prompt
prompt = st.chat_input("Message AI Assistant")
        
# Button to submit the prompt and image
if prompt:
    session_prompts.append(prompt)
    # Initialize the payload
    payload = {
        "model": "llava",
        "prompt": prompt,
        "stream": False
    }

    # If an image is uploaded, encode it to base64 and include it in the payload
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        unique_filename = str(uuid.uuid4()) + os.path.splitext(uploaded_file.name)[1]
        image_filename = os.path.join(UPLOAD_DIR, unique_filename)
        image.save(image_filename)

        # Set the file permissions to read and writable by all users
        os.chmod(image_filename, 0o666)

        # Get the absolute path of the image file
        image_fullpath = os.path.abspath(image_filename)

        with open(image_fullpath, 'rb') as f:
            img_str = base64.b64encode(f.read()).decode('utf-8')
            payload["images"] = [img_str]

    # Send the POST request
    response = requests.post(url, json=payload, stream=True)

    response_time = 0
    
    # Check if the request was successful
    if response.status_code == 200:
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode('utf-8')
                response_part = json.loads(decoded_line)
                chat_response = response_part['response']
                eval_count = response_part['eval_count']
                eval_duration = response_part['eval_duration']

                session_responses.append(chat_response)
                response_time = round(eval_count / eval_duration * 10**9, 2)
                

    else:
        st.write("Failed to get a response from the server.")
        st.write(f"Response code: {response.status_code}")
        
    for i in range(len(session_prompts)):
        with st.chat_message("user"):
            st.write(session_prompts[i])
        with st.chat_message("assistant"):
            st.write(session_responses[i])
    st.markdown("Response time: "+ str(response_time))
