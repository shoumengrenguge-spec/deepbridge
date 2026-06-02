import requests

url = "http://127.0.0.1:8000/v1/chat/completions"

data = {
    "model": "deepseek-chat",
    "messages": [
        {
            "role": "user",
            "content": "你好"
        }
    ]
}

r = requests.post(url, json=data)

print(r.json())