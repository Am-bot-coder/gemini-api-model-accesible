import requests

API_KEY = "YOUR_API_KEY"
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"

response = requests.get(url)

if response.status_code == 200:
    models = response.json()
    for model in models.get("models", []):
        print(model["name"])
else:
    print("Error:", response.status_code,response.text)