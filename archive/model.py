from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

#device = torch.device('cpu') # Add if GPU not available

from transformers import AutoTokenizer, AutoModelForQuestionAnswering

def load_model():
    # Load the processor and model
    tokenizer = AutoTokenizer.from_pretrained("liuhaotian/llava-v1.6-vicuna-7b")
    model = AutoModelForQuestionAnswering.from_pretrained("liuhaotian/llava-v1.6-vicuna-7b")
    return tokenizer, model

processor, model = load_model()

def process_image_and_question(tokenizer, model, image, question, max_new_token=50, num_beams=5, temperature=1.0, top_k=50, top_p=0.95, do_sample=True):
    # Ensure inputs are on the CPU
    #image_tensor = tokenizer.feature_extractor(images=image, return_tensors="pt").to(device)
    
    # Preprocess the question
    inputs = tokenizer(question, return_tensors="pt", padding="max_length").to(device)
    
    # Compare the lengths
    max_length = 1024 # Increase if neccesary, a word is generally 2-3 tokens
    input_ids = inputs['input_ids'][0]
    tokenized_length = len(input_ids)
    if tokenized_length > max_length:
        print(f"Tokenized length ({tokenized_length}) exceeds max_length ({max_length})")
    else:
        print(f"Tokenized length ({tokenized_length}) is within the max_length ({max_length})")

    """
    # Generate the answer
    output_ids = model.generate(
        vision_x=image_tensor,
        lang_x=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_new_tokens=max_new_token,
        num_beams=num_beams,
        temperature=temperature,
        top_k=top_k,
        top_p=top_p,
        do_sample=do_sample,
    )[0]
    """
    # Adjusting the generation parameters to fine-tune output
    output_ids = model.generate(
        vision_x=vision_input,
        lang_x=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_new_tokens=max_new_token,  # Adjust this if you expect shorter/longer responses
        num_beams=num_beams,           # Beam search for better quality output
        temperature=temperature,       # Control randomness
        top_k=top_k,                   # Limit to top-k probable tokens
        top_p=top_p,                   # Nucleus sampling for variability
        do_sample=do_sample            # Whether to use sampling or not
    )[0]
    
    # Decode the output ids to get the generated text
    answer = tokenizer.decode(output_ids, skip_special_tokens=True)
    
    return answer
    
"""
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