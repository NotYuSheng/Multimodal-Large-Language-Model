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

# Title of the Streamlit app
st.title("MMLLM")

# Input field for the prompt
prompt = st.text_input("Enter your prompt:", "What's in this image?")

# Image upload field
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

# Button to submit the prompt and image
if st.button("Generate Response"):
    # Initialize the payload
    payload = {
        "model": "llava",
        "prompt": prompt
    }

    # If an image is uploaded, encode it to base64 and include it in the payload
    if uploaded_file is not None:
        # Open the image and encode it to base64
        image = Image.open(uploaded_file)
        image_base64 = base64.b64encode(uploaded_file.read()).decode("utf-8")

        # Include the base64 encoded image in the payload
        payload["images"] = image_base64

    # Send the POST request
    response = requests.post(url, json=payload, stream=True)

    # Check if the request was successful
    if response.status_code == 200:
        st.write("Response from the model:")

        # Initialize a placeholder to update the Streamlit display
        response_placeholder = st.empty()
        complete_response = ""

        # Stream the response
        for line in response.iter_lines():
            if line:
                # Decode the line (response part) from bytes to string
                decoded_line = line.decode('utf-8')

                # Convert the string response to a dictionary
                response_part = json.loads(decoded_line)

                # Display the response word by word in Streamlit
                words = response_part['response'].split()

                for word in words:
                    for char in word:
                        complete_response += char
                        html_content = f"""
                        <div style="white-space: normal;">
                            {complete_response}
                        </div>
                        """
                        response_placeholder.markdown(html_content, unsafe_allow_html=True)
                        time.sleep(0.1)
                complete_response += " "

    else:
        st.write("Failed to get a response from the server.")
