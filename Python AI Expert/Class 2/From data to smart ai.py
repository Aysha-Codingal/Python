import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

print(f"{Fore.CYAN}🧑🏻‍🏭 WELOCOME TO THE SENTIMENT SPY! 🧑🏻‍🏭{Style.RESET_ALL}")

user_name = input(f"{Fore.MAGENTA} Please Enter Your Name: {Style.RESET_ALL}").strip()
if not user_name:
    user_name = "Mystery Agent"

conversation_history = []

print(f"{Fore.CYAN}Hello Agent {user_name}!{Style.RESET_ALL}")
print("Type a Sentence and I Will Analyse Your Sentence With TextBlob And Show You The Sentement.")

print(
    f"{Fore.RED}Type, reset, history, exit{Style.RESET_ALL}\n"
)

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED}Enter Some Text Or Valid Messege. {Style.RESET_ALL}")
        continue

    elif user_input.lower() == "exit":
        print(f"{Fore.BLUE}👋🏻 BYE SENTIMENT SPY {user_name}! 👋🏻 {Style.RESET_ALL}")
        break

    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.CYAN}🔄️History Cleared 🙂 {Style.RESET_ALL}")
        continue

    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No Conversation History Yet. {Style.RESET_ALL}")

        else:
            print(f"{Fore.CYAN}📜Conversation History: {Style.RESET_ALL}")
            for text, polarity, sentiment in conversation_history:{Style.RESET_ALL} 
            print(f"- \"{text}\"👉🏻 {sentiment} ({"polarity"})")
        continue

    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive 😃"

    elif polarity < 0:
        sentiment = "Negetive 😔"

    else:
        sentiment = "Neutral 😑" 

    conversation_history.append((user_input, polarity, sentiment))
    print(f"{Fore.BLUE}SENTIMENT: {sentiment} | Polarity Score: {polarity} {Style.RESET_ALL}")           

        
