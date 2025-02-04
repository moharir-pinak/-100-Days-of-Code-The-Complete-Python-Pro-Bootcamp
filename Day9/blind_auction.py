import art 

bidding = {}
more_users = True
print(art.logo)


def highestbid(bidding_dict):
    highest = 0
    winner = ""
    for bidder in bidding_dict:
        bid_amt = bidding_dict[bidder]
        if bid_amt >highest:
            bid_amt = highest
            winner = bidder
    print(f"The winner for this auction is {winner} with a bid of {highest}")

print(art)
while more_users:
    a = input("Enter your name :\n")
    b = int(input("Enter the bid:\n"))
    bidding[a] = b
    print(bidding)
    n = input("Are there some more users :\n").lower()
    if n == "no":
        more_users = False
        highestbid(bidding)
    elif n == "yes":
        print("\n" * 20)
       
        
    
