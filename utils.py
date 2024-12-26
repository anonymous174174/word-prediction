import torch
from transformers import GPT2Tokenizer

# Use a single tokenizer instance to prevent repeated initialization
gpt_tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

def clean_text(input_text: str) -> str:
    """
    Clean and preprocess the input text.
    """
    return input_text.strip()

def tokenize_text(text: str):
    """
    Convert text into tokenized tensor format.
    """
    return gpt_tokenizer.encode(text, return_tensors="pt")

def decode_token(token_tensor) -> str:
    """
    Convert token tensor into a readable string.
    """
    return gpt_tokenizer.decode(token_tensor[0], skip_special_tokens=True)

def get_next_token(model, text: str) -> str:
    """
    Predict the next word from the given input.
    """
    prepared_text = clean_text(text)
    tokenized_input = tokenize_text(prepared_text)
    
    with torch.no_grad():
        output_logits = model(tokenized_input).logits
    
    # Extract logits for the final token and determine the most probable next token
    last_token_logits = output_logits[0, -1, :]
    next_token_id = torch.argmax(last_token_logits).item()
    return decode_token(torch.tensor([[next_token_id]]))
