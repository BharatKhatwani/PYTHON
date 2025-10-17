import requests

def fetch_random_jokes_freeApi():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    response = requests.get(url)
    data = response.json()

    if data.get("success") and "data" in data:
        joke_content = data["data"]["content"]   # ✅ Correct path
        message = data["message"]
        return joke_content, message
    else:
        raise Exception("Failed to fetch joke data")

def main():
    try:
        joke, message = fetch_random_jokes_freeApi()
        print(f"Joke: {joke}")
        print(f"Message: {message}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
