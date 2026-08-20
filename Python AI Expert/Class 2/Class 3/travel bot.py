import re, random
from colorama import Fore, init

init(autoreset = True)

destinations = {
    "beaches":["Bali", "Maldives", "Phuket"],
    "mountains":["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities":["Los Angeles", "Paris", "Abu Dhabi"]
}
jokes = [
    "Why do programmers prefer dark mode ? Because like attracts bugs",
    "Why did the Maths book is always sad ? Because it has problems 🤣",
    "Why don't secrets last in a family ? Because someone always spill the tea 🤣"
]

def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def recommend():
    print(Fore.CYAN + "Travel_Bot: Beaches OR Mountains OR Cities ?")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalize_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"Travel_Bot: How About {suggestion} ?")
        print(Fore.CYAN + "Travel_Bot: Do You like it ? (yes / no)")
        answer = input(Fore.YELLOW + "You: ").lower()

        if answer == "yes":
            print(Fore.GREEN + f"Travel_Bot: Awesome! Enjoy {suggestion}!")
        elif answer == "no":
            print(Fore.RED + "Travel_Bot: Let's try another.")
            recommend()
        else:
            print(Fore.RED + "Travel_Bot: Let's try another.")
            recommend()


def chat():
    print(Fore.CYAN + "Hello! I'm Travel_Bot")
    name = input(Fore.YELLOW + "Your Name ?") 
    print(Fore.GREEN + f"Nice to meet you, {name}!")

    
    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)

        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "exit" in user_input or "bye" in user_input.lower():
            print(Fore.CYAN + "Travel_Bot: Safe Travels! Goodbye!")
            break
        else:
            print(Fore.RED + "Travel_Bot: Could You Rephrase ? ") 


if __name__ == "__main__":
    chat()            




    