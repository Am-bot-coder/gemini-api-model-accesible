# Google Generative Language API - Model Listing Script

This Python script retrieves and displays available models from the **Google Generative Language API (Gemini)**.

## 📜 Description

The script sends a GET request to the Google Generative Language API endpoint to fetch a list of models. It prints out the names of each available model.

## 🧾 Requirements

- Python 3.x
- `requests` library

Install `requests` using pip if it's not already installed:

```bash
pip install requests
```

## 📂 Usage

1. Replace the placeholder `YOUR_API_KEY` with your actual Google API key in the script:

```python
API_KEY = "YOUR_API_KEY"  # Replace with your real API key
```

2. Run the script:

```bash
python list_models.py
```

3. If successful, it will output:

```
models/chat-bison-001
models/text-bison-001
...
```

If there’s an error (e.g., invalid API key), it will show:

```
Error: 403 {
  "error": {
    "code": 403,
    "message": "API key not valid.",
    ...
  }
}
```


```

## 🔐 How to Get an API Key

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create or select a project.
3. Enable the **Generative Language API** (a.k.a. PaLM API).
4. Go to **APIs & Services > Credentials** and create an API key.
5. Use that key in the script.

## 🛑 Notes

- Make sure your API key is active and has the necessary permissions.
- Billing and quota limits may apply depending on your usage.

---

