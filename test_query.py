import requests

def main():
    url = "http://127.0.0.1:5000/query"
    payload = {"input": "Hello, LLaMA 3! Tell me a fun fact."}

    response = requests.post(url, json=payload)
    data = response.json()
    print("Model response:", data["response"])

if __name__ == "__main__":
    main()
