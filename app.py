import streamlit as st
from PIL import Image
from model import load_model, process_image_and_question

# Load model and processor
processor, model = load_model()

# Streamlit app
st.title("Multimodal Large Language Model Web App")

# Image upload
uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_image is not None:
    # Display the uploaded image
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # User question input
    question = st.text_input("Ask a question about the image")

    if st.button("Get Answer"):
        if question:
            # Process image and question to get the answer
            answer = process_image_and_question(processor, model, image, question)
            
            # Display the answer
            st.write(f"Answer: {answer}")
        else:
            st.write("Please ask a question.")
