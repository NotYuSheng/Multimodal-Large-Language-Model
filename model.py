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

def process_image_and_question(image, question):
    # Preprocess the image and question
    inputs = processor(image, question, return_tensors="pt")
    
    # Generate the answer
    outputs = model.generate(**inputs, max_new_tokens=50)
    answer = processor.decode(outputs[0], skip_special_tokens=True)
    
    return answer
