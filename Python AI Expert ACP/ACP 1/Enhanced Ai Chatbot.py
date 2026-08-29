print("Hello! I am AI Bot. What's your name? : ")
name = input()

print(f"Nice to meet you, {name}!")

print("How's your day going so far? (good/bad/okay) : ")
mood = input().lower()

if "good" in mood:
    print("That's awesome! I hope it keeps getting better.")
    print("Did anything exciting happen today? (yes/no) : ")
    exciting = input().lower()
    if "yes" in exciting:
        print("That's fantastic! I love days full of good news.")
    else:
        print("Hey, a peaceful, smooth day is a win in my book!")

elif "bad" in mood:
    print("I'm really sorry to hear that. We all have those days.")
    print("Do you want to talk about it, or would you prefer a distraction? (talk/distract) : ")
    choice = input().lower()
    if "talk" in choice:
        print("I'm all ears. Sometimes typing it out helps relieve the stress.")
        vent = input()
        print("Thank you for sharing that with me. Hang in there, you've got this!")
    else:
        print("I completely understand. Just remember to take it easy on yourself today!")

else:
    print("I feel you. Some days are just middle-of-the-road, and that's totally fine.")

print(f"\nBefore you go, {name}, what's your favorite thing to do to relax? : ")
hobby = input()
print(f"Ah, {hobby} sounds like a great way to unwind!")

print(f"\nIt was really nice chatting with you, {name}. Have a wonderful rest of your day! Goodbye!")