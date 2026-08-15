print("Hello! I am AI Bot. What's Your name? : ")

name = input()

print(f"Nice To Meet You, {name}!")

print("How Are You ? (good/bad) : ")
mood = input().lower()

if mood == "good":
    print("I'm glad to hear that!")
elif mood == "bad":
    print("I am Sorry To Hear That! Hope you will get better soon!. ")
else:
    print("I see, Sometimes its hard to put feelings into words.")

print(f"It was nice chatting with you {name}. GoodBye! ")    