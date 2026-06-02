import requests

url = "http://127.0.0.1:8000/v1/chat/completions"

data = {
    "model": "deepseek-chat",
    "messages": [
        {
            "role": "user",
            "content": "hello"
        }
    ]
}

response = requests.post(url, json=data)

print(response.text)