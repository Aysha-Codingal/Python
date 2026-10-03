import requests

def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)

    if response.status_code == 200:
        ''' response usually comes from an API request (commonly using the requests library).
        . json() converts the API response into a Python dictionary.
        joke_data becomes a Python dictionary:
        joke_data['setup']- Gets the setup of the joke.
        joke_data['punchline']- Gets the punchline of the joke.'''

        joke_data = response.json()
        return f"{joke_data['setup']} - {joke_data['punchline']}"
    else:
        return "Failed to recieve joke."

def main():
    print("Welcome To The Random Joke Generator!")

    while True:
        user_input = input("Press Enter To Get New Joke, Or Type 'q'/ 'exit' to quit the joke generator!")

        if user_input in ("q", "exit"):
            print("GoodBye!")
            break

        joke = get_random_joke()
        print(joke)

if __name__ == "__main__":
    main()        
