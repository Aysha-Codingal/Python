# Flashcards

class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return f"{self.word} ({self.meaning})"

flash = [ ]      
print("********* WELCOME TO FLASHCARD APPLICATION *********")  
while True:
    word = input("ENTER THE WORD: ")
    meaning = input ("ENTER THE MEANING: ")
    flash.append(flashcard(word,meaning))
    ch = input ("\n DO YOU WANT TO CONTINUE (Y / N) : ")
    if ch.lower() == 'n':
        break
    print()
    for i in flash:
        print("=>",i)
        