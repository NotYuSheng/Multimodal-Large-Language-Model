from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

def load_model():
    # Load the processor and model
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

def process_image_and_question(processor, model, image, question):
    # Preprocess the image and question
    inputs = processor(image, question, return_tensors="pt")
    
    # Generate the answer
    outputs = model.generate(**inputs)
    answer = processor.decode(outputs[0], skip_special_tokens=True)
    
    return answer
