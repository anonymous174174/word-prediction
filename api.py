from fastapi import FastAPI
from pydantic import BaseModel
from app.model import initialize_model
from app.utils import get_next_token

service = FastAPI()

# Initialize model and tokenizer when the app starts
gpt_model, gpt_tokenizer = initialize_model()

class PredictionInput(BaseModel):
    prompt: str

@service.post("/generate")
def generate(input_data: PredictionInput):
    """
    Generate the next word based on input prompt.
    """
    prediction = get_next_token(gpt_model, input_data.prompt)
    return {"prediction": prediction}
