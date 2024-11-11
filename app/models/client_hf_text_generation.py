import requests

# OpenAI API standard endpoint
SERVER_URL = "http://127.0.0.1:8000/v1/chat/completions"

request_data = {
    "model": "gpt2",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "How are you?"}
    ]
}

if __name__ == "__main__":
    # response = requests.post(SERVER_URL, json=request_data)    
    # print(response.json())
    print("streaming")
    response = requests.post(SERVER_URL, json=request_data, stream=True)
    for chunk in response.iter_lines():
        print(chunk.decode("utf-8"))