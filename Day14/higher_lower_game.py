import random 
import art
facts = {"Kholi" : 13000 , 
         "Dhoni" : 12000 , 
         "Rohit" : 11000 , 
         "Bumrah" : 10000 , 
         "Jadeja" : 9000 , 
         "Ashwin" : 8000 , 
         "Bhuvneshwar" : 7000 , 
         "Yadav" : 6000 , 
         }

def main():
    print(art.logo)
    res = input("Want to play the game ? (y/n)").lower()
    if res =="y":
        game_over = False
        score = 0
        
        while not game_over:
            a = random.choice(list(facts))
            b = random.choice(list(facts))


            if a == b:
                b = random.choice(list(facts))
            

            ans = input(f"Who has more runs ? {a=} or {b=} \n")
            
            if facts[a] > facts[b] :
                if ans == "a":
                    print("Your answer is correct")
                    score += 1 
                    print(f"Your score is : {score}")
                else:
                    print("Your answer is incorrect")
                    game_over = True
                    print(f"Your score is : {score}")
            if facts[a] < facts[b]:
                if ans == "b":
                    print("Your answer is correct")
                    score += 1 
                    print(f"Your score is : {score}")
                else:
                    print("Your answer is incorrect")
                    game_over = True
                    print(f"Your score is : {score}")
            
                        
main()
