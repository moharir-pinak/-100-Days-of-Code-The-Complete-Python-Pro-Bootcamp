import random
import art
easy_chances = 10
hard_chances = 5
game_over = False

def easy(n):
    global easy_chances
    global game_over
    while not game_over:
        if easy_chances !=0:
            easy_chances -= 1
            compare(n)
        else:
            print("you lose")
            game_over = True
    

        
    
def hard (n):
    global hard_chances
    global game_over
    while not game_over:
        if hard_chances !=0:
            hard_chances -= 1
            compare(n)
        else:
            print("you lose")
            game_over = True

    
def compare(n):
    global easy_chances
    global hard_chances
    global game_over
    
    guess = int(input("Enter yout guess: "))
    if guess > n :
        print("Too high")
    elif guess<n:
        print("Too Low")
    elif guess == n:
        print("You Won")
        game_over = True
    

print(art.logo)
print("Welcome to Guessing game ")
difficulty = input("Enter difficulty in which You would Like to play : Easy , Medium , Hard :\n").lower()
n = random.randint(1,100)
# print(n)
if difficulty == "easy":
    easy(n)
elif difficulty == "hard":
    hard(n)
  