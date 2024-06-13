import requests
import streamlit as st
import time
import json
import os
import uuid
import base64
from PIL import Image

context = None

# Ollama server address
url = "http://localhost:11434/api/generate"

st.set_page_config(page_title="Multimodal AI Assistant")

# Title of the Streamlit app
st.title("Multimodal AI Assistant")

# Image upload field
uploaded_file = st.sidebar.file_uploader("Upload image :gear:", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    st.sidebar.image(uploaded_file, use_column_width = True, caption='Uploaded image')

# Directory to save uploaded images
UPLOAD_DIR = os.path.join(os.getcwd(), "tmp")
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR, exist_ok=True)

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
    
