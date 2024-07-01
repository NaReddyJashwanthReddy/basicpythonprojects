import random 

name=input("whats your name: ")

print(f"Good luck {name}")

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)

print("Guess the character ...")

guessess = ""

turns= len(words)

while turns>0:
    failed=0

    for char in word:
        if char in guessess:
            print(char)
        else:
            print("_")
            failed +=1

    if failed == 0:
        print(f"congrats you guessed the word \nthe word is {word}")
        break
    guess=input("guess the word : ")
    guessess += guess

    if guess not in word:
         turns -= 1

         print("wrong")

         print("you have", turns, "number of turns left")

         if turns==0:
             print("you loss")
        

