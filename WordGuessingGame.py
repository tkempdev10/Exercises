#!/usr/bin/env python
# coding: utf-8

# In[1]:


Guesses = 7
Word = "puppy"
Blank_Word = ['_' for i in Word]
indexlist = []

print("Welcome to the word-guessing game! You can guess letters or the whole word and you get 7 guesses to start with! Each letter or word guess that is incorrect will decrease your guess count by 1")
while Guesses >= 1:
    print(f"You have {Guesses} remaining guesses!")
    User_Guess = str(input("Enter your guess!"))
    if len(User_Guess)>1:
        if User_Guess == Word:
            print(f"Congratulations! {Word} was the word!")
            break
        elif User_Guess != Word and Guesses == 1:
            print(f"Game Over! The word was {Word}. Better luck next time!")
            break
        else:
            print("Sorry, that was not the word! Try again!")
            Guesses = Guesses-1
    else:
        if User_Guess in Word:
            indexlist = [i for i, ltr in enumerate(Word) if ltr == User_Guess]
            for i in indexlist:
                    Blank_Word[i] = User_Guess
            if '_' not in Blank_Word:
                print(f"Congratulations! The word was {Word}!")
                break
            else:
                print(f'You guessed one of the letters! Here are the letters you have found! {Blank_Word}')
        else:
            print(f'Sorry, {User_Guess} was not in the word!')
            Guesses = Guesses - 1
            if Guesses == 0:
                print(f"Sorry! You have run out of guesses. The word was {Word}, better luck next time!")
                break
        


# In[ ]:




