import re, random
from colorama import Fore, init

init(autoreset=True)

weather_data = {
    "sunny": ["28°C with clear skies", "30°C and bright sun", "26°C with a gentle breeze"],
    "rainy": ["18°C with heavy rain", "20°C with light showers", "16°C and thunderstorms"],
    "snowy": ["-2°C with fresh snowfall", "-5°C and blizzards", "0°C with sleet"]
}

def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def check_weather():
    print(Fore.CYAN + "WeatherBot: Sunny, rainy, or snowy?")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalize_input(preference)

    if preference in weather_data:
        info = random.choice(weather_data[preference])
        print(Fore.GREEN + f"WeatherBot: The report shows {info}.")
        print(Fore.CYAN + "WeatherBot: Does this help? (yes/no)")
        answer = input(Fore.YELLOW + "You: ").lower()

        if answer == "yes":
            print(Fore.GREEN + "WeatherBot: Awesome! Stay prepared for the weather!")
        elif answer == "no":
            print(Fore.RED + "WeatherBot: Let's check another condition.")
            check_weather()
        else:
            print(Fore.RED + "WeatherBot: I'll check again.")
            check_weather()
    else:
        print(Fore.RED + "WeatherBot: Sorry, I don't have information on that weather type.")
        check_weather()

def chat():
    print(Fore.CYAN + "Hello! I'm WeatherBot.")
    name = input(Fore.YELLOW + "Your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}!")

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)

        if "weather" in user_input or "forecast" in user_input or "check" in user_input:
            check_weather()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "WeatherBot: Stay safe! Goodbye!")
            break
        else:
            print(Fore.RED + "WeatherBot: Could you rephrase?")

if __name__ == "__main__":
    chat()