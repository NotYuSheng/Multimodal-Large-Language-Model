from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

device = torch.device('cpu')

def load_model():
    # Load the processor and model
    processor = ViLBERTProcessor.from_pretrained("microsoft/vilbert-base")
    model = ViLBERTForQuestionAnswering.from_pretrained("microsoft/vilbert-base")
    return processor, model

processor, model = load_model()

def process_image_and_question(processor, model, image, question):
    # Resize the image to a suitable size if needed
    # For ViLBERT, images typically need to be resized to 224x224
    resized_image = image.resize((224, 224))
    
    # Convert the image to RGB format if it's not already in that format
    if resized_image.mode != "RGB":
        resized_image = resized_image.convert("RGB")
    
    # Convert the image to PyTorch tensor
    image_tensor = processor.feature_extractor(images=resized_image, return_tensors="pt").to(device)
    
    # Preprocess the question
    inputs = processor.tokenizer(image, question, padding="max_length", max_length=128, truncation=True, return_tensors="pt").to(device)
    
    # Generate the answer
    outputs = model(**inputs)
    
    # Extract the answer from the model's output
    answer = processor.decode(outputs["question_answering"]["answer"][0], skip_special_tokens=True)
    
    return answer
"""

def load_model():
    # Load the processor and model
    processor = ViLBERTProcessor.from_pretrained("microsoft/vilbert-base")
    model = ViLBERTForQuestionAnswering.from_pretrained("microsoft/vilbert-base")
    return processor, model

processor, model = load_model()


def process_image_and_question(image, question):
    # Preprocess the image and question
    inputs = processor(image, question, return_tensors="pt")
    
    # Generate the answer
    outputs = model.generate(**inputs, max_new_tokens=50)
    answer = processor.decode(outputs[0], skip_special_tokens=True)
    
    return answer


def process_image_and_question(processor, model, image, question):
    # Preprocess the image and question
    inputs = processor(image, question, return_tensors="pt", padding=True, truncation=True)
    
    # Generate the answer
    outputs = model(**inputs)
    
    # Extract the answer from the model's output
    answer = processor.decode(outputs["question_answering"]["answer"][0], skip_special_tokens=True)
    
    return answer
"""
