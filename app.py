import streamlit as st
from PIL import Image
from model import load_model, process_image_and_question

st.markdown(
    """
    <style>
        button[title^=Exit]+div [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
)

# Streamlit app
st.title("Multimodal Large Language Model Web App")

# Image upload
uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# Display uploaded image
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    # Resize the image to a maximum width of 500 pixels
    resized_image = image.resize((500, int(500 * image.height / image.width)))
    st.image(resized_image, caption="Uploaded Image", output_format='auto')

# User question input
question = st.text_input("Ask a question about the image")

if st.button("Get Answer"):
    if uploaded_image is not None and question:
        # Load model and processor
        processor, model = load_model()
        
        # Process image and question to get the answer
        answer = process_image_and_question(processor, model, image, question)
        
        # Display the answer
        st.write(f"Answer: {answer}")
    else:
        st.write("Please upload an image and ask a question.")
