import time
import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

conversation_history = []
positive_count = 0
negative_count = 0
neutral_count = 0

print(f"{Fore.CYAN}🧑🏻‍🏭 WELCOME TO THE SENTIMENT SPY! 🧑🏻‍🏭{Style.RESET_ALL}")

while True:
    user_name = input(
        f"{Fore.MAGENTA} Please Enter Your Name: {Style.RESET_ALL}"
    ).strip()
    if user_name.isalpha():
        break
    print(
        f"{Fore.RED} Invalid Name! Please use alphabetic characters only.{Style.RESET_ALL}"
    )

print(f"{Fore.CYAN}Hello Agent {user_name}!{Style.RESET_ALL}")
print(
    "Type a Sentence and I Will Analyse Your Sentence With TextBlob And Show You The Sentiment."
)
print(
    f"{Fore.RED}Type summary, reset, history, or exit{Style.RESET_ALL}\n"
)

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED}Enter Some Text Or Valid Message.{Style.RESET_ALL}")
        continue

    elif user_input.lower() == "exit":
        print(f"{Fore.BLUE}👋🏻 BYE SENTIMENT SPY {user_name}! 👋🏻{Style.RESET_ALL}")
        print(f"\n{Fore.CYAN}Mission Report:{Style.RESET_ALL}")
        print(f"Positive messages: {positive_count}")
        print(f"Negative messages: {negative_count}")
        print(f"Neutral messages: {neutral_count}")
        break

    elif user_input.lower() == "reset":
        conversation_history.clear()
        positive_count = 0
        negative_count = 0
        neutral_count = 0
        print(f"{Fore.CYAN}🔄️ History Cleared 🙂{Style.RESET_ALL}")
        continue

    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No Conversation History Yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}📜 Conversation History:{Style.RESET_ALL}")
            for text, polarity, sentiment in conversation_history:
                print(f'- "{text}" 👉🏻 {sentiment} ({polarity:.2f})')
        continue

    elif user_input.lower() == "summary":
        print(f"{Fore.CYAN}📊 Sentiment Summary:{Style.RESET_ALL}")
        print(f"Positive messages: {positive_count}")
        print(f"Negative messages: {negative_count}")
        print(f"Neutral messages: {neutral_count}")
        continue



    print(f"{Fore.CYAN}🕵🏻‍♂️ Analyzing Sentiment", end="", flush=True)
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print("\n")

    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity

    if polarity > 0.25:
        sentiment = f"{Fore.GREEN}Positive 😃{Style.RESET_ALL}"
        positive_count += 1
    elif polarity < -0.25:
        sentiment = f"{Fore.RED}Negative 😔{Style.RESET_ALL}"
        negative_count += 1
    else:
        sentiment = f"{Fore.YELLOW}Neutral 😑{Style.RESET_ALL}"
        neutral_count += 1

    conversation_history.append((user_input, polarity, sentiment))
    print(
        f"{Fore.BLUE}SENTIMENT: {sentiment} | Polarity Score: {polarity:.2f}{Style.RESET_ALL}\n"
    )