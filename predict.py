import requests

API_ENDPOINT = "http://0.0.0.0:8080/generate"

def request_prediction(prompt: str):
    """
    Send a POST request to fetch the predicted next word.
    """
    response = requests.post(API_ENDPOINT, json={"prompt": prompt})
    if response.status_code == 200:
        return response.json().get("prediction")
    else:
        return f"Request failed: {response.status_code}"

def main():
    user_input = input("Enter a text prompt: ")
    predicted_word = request_prediction(user_input)
    print(f"Predicted next word: {predicted_word}")

if __name__ == "__main__":
    main()
