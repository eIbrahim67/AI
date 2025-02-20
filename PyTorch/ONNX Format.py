import requests
import json

text = "Hello this is something about my home country, egypt "

response = requests.post('http://localhost:11434/api/generate', 
        json={
            "model": "llama3.2:latest",
            "prompt": f"Summarize this article in 3 bullet points: {text}",
            "stream": False,
            "options": {
                "temperature": 0.3,
            }}
            )

print(response.text)