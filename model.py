from transformers import GPT2LMHeadModel, GPT2Tokenizer

def initialize_model():
    """
    Load the GPT-2 model and tokenizer.
    """
    model_instance = GPT2LMHeadModel.from_pretrained("gpt2")
    tokenizer_instance = GPT2Tokenizer.from_pretrained("gpt2")
    return model_instance, tokenizer_instance
