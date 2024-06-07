import streamlit as st

# Streamlit app
st.title("Multimodal Large Language Model")

# Image upload
uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
temp_file_path = ""

# Display uploaded image
if uploaded_image is not None:
    # Save uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name

    # Display the image with resized dimensions
    st.image(temp_file_path, caption="Uploaded Image")

# User question input
question = st.text_input("Ask a question about the image")

if st.button("Get Answer"):
    if uploaded_image is not None and question:
        try:
            # Append image path to question
            prompt = question + " " + temp_file_path
            
            # Prompt to ollama server
            response = ollama.chat(model='llama3', messages=[
              {
                'role': 'user',
                'content': prompt,
              },
            ])
            
            # Display the answer
            st.write(f"Answer: {response['message']['content']}")
            
        except Exception as e:
            st.error("An error occurred while processing the image and question. Please try again.")
    else:
        st.warning("Please upload an image and ask a question.")
