# Next Word Prediction API

This project provides a FastAPI-based API that predicts the next word in a given text sequence using a pre-trained GPT-2 model from Hugging Face Transformers.

---



## Requirements

To run this project, you'll need the following:

- Python 3.8+
- `pip` (Python package manager)

Install the dependencies using the following command:

```bash
pip install -r requirements.txt
Setup and Usage
1. Clone the Repository
bash
Copy code
git clone <repository_url>
cd project-root
2. Install Dependencies
bash
Copy code
pip install -r requirements.txt
3. Run the API Server
Start the FastAPI server by running:

bash
Copy code
python main.py
The server will be accessible at http://0.0.0.0:8080.

4. Test the API
You can test the API using the predict.py script:

bash
Copy code
python predict.py
Alternatively, use tools like Postman or cURL to send a POST request to the /generate endpoint:

bash
Copy code
curl -X POST -H "Content-Type: application/json" -d '{"prompt": "Hello, my name is"}' http://0.0.0.0:8080/generate
Example Response
json
Copy code
{
  "prediction": "GPT"
}
API Endpoints
POST /generate
Description: Predicts the next word based on the input text.

Request Body:

json
Copy code
{
  "prompt": "Hello, my name is"
}
Response Body:

json
Copy code
{
  "prediction": "GPT"
}
Technologies Used
FastAPI: For building the API.
Transformers Library: For using the pre-trained GPT-2 model.
PyTorch: Backend for model inference.
Future Enhancements
Add support for batch predictions.
Extend the API to handle longer text completions.
Optimize the model for deployment using ONNX or TorchScript.
Feel free to contribute or raise issues for improvements!

markdown
Copy code

---

### Steps for Implementation
1. **Create the Directory Structure**:
   - Create a folder named `project-root` and subfolders like `app/`.
   - Move the respective files into the appropriate folders.

2. **Update Import Paths**:
   - Adjust import paths in `api.py`, `main.py`, and other files to match the folder structure (e.g., `from app.model import initialize_model`).

3. **Dependencies**:
   - Ensure `requirements.txt` includes all dependencies:
     ```text
     fastapi
     uvicorn
     transformers
     torch
     requests
     ```

This will ensure your project is modular, readable, and easy to maintain or ext