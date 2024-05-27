from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

device = torch.device('cpu')

from transformers import AutoTokenizer, AutoModelForQuestionAnswering

def load_model():
    # Load the processor and model
    tokenizer = AutoTokenizer.from_pretrained("liuhaotian/llava-v1.6-vicuna-7b")
    model = AutoModelForQuestionAnswering.from_pretrained("liuhaotian/llava-v1.6-vicuna-7b")
    return tokenizer, model

processor, model = load_model()

def process_image_and_question(tokenizer, model, image, question):
    # Encode the question
    inputs = tokenizer(question, return_tensors="pt")
    
    # Generate the answer
    outputs = model(**inputs)
    
    # Extract the answer from the model's output
    answer_start = torch.argmax(outputs.start_logits)
    answer_end = torch.argmax(outputs.end_logits) + 1
    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(inputs.input_ids[0][answer_start:answer_end]))
    
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
