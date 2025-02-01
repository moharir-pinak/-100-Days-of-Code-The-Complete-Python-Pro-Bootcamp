import random

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

words = ["peocock" , "budget" , "mouse","skill"]
guessed = []
lives = 6

# choosing a random word

chosen_word = random.choice(words)
print(chosen_word)


# To collect the guessed letters 
guessed = ""
# adding blanks 
for position in range(len(chosen_word)):
    guessed += '_'
print(guessed)

game_over = False
correct_letters = []


while not game_over:
# Guessing the word 
    guess = input("Enter your guess: ").lower()
    print(guess)

    # To display the guessed letter and to display _ in unguessed ones
    display = ""


    for letter in chosen_word:
        
        if letter == guess:
            display +=letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter 
        else : 
            display +="_"
        print(display)
        
        if guess not in chosen_word:
            lives -=1
            if lives == 0:
                print("You lose")
                game_over = True
            
        print(display)   
    
    if "_" not in display:
        print("You Win")
        game_over = True 
        
    print(stages[lives])   


