import requests

url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"

def get_random_technology_fact():
    response = requests.get(url)
    if response.status_code == 200:
        fact_data = response.json()
        print(f"Did You Know? {fact_data['text']}")
    else:
        print("Failed To Fetch Fact")

while True:
    user_input = input("Press Enter To Get A Random Technology Fact Or Type 'q' to quiz the progmamme.")    
    if user_input.lower() == 'q':
        break
    get_random_technology_fact()        