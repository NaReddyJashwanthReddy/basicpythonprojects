from collections import Counter
import random 

print("Hangman game \nAll the best")

sentence='''apple banana mango strawberry  
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

words=sentence.split(' ')
word=random.choice(words)

if __name__=='__main__':
    print('Guss the word! HINT: the word is a fruit')

    for _ in word:
        print('_',end=" ")
    
    guesses=""
    chances=len(word)+2
    correct=0
    flag=0

    try:
        while (chances != 0) and flag ==0:
            print()
            chances -=1
            try:
                guess=str(input('enter the character : '))
            except:
                print('Enter only a letter!')
                continue
            if not guess.isalpha():
                print('Enter only Letters')
                continue
            elif len(guess)>1:
                print('Enetr no more than One Letter!')
                continue 
            elif guess in guesses:
                print('You have already gueese it')
                continue 
            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    guesses += guess
            else:
                print("You have guess it wrong\nTry Again!\nYou have {} Chances".format(chances))
            for char in word:
                if char in guesses and (Counter(guesses)!=Counter(word)):
                    print(char,end=" ")
                elif (Counter(guesses)==Counter(word)):
                    print(f"The guess the word\nthe word is {word}")
                    flag=1
                    break
                else:
                    print('_',end=" ")
        if chances == 0 and (Counter(guesses)!=Counter(word)):
            print()
            print("You Lost! Try again....")
            print(f"the word is {word}")

    except KeyboardInterrupt:
        print()
        print('BYE! try again')
        exit()