# Conditional Operators

a = int(input("Enter your height : "))
b = int(input("Enter your age : "))

if a >120:
    print("You can ride")
    # nested If Statement 
    
    if b < 12:
        print("Pay 5")
    
    elif b >= 13 :
        print("Pay 20")
    
    else :
        print("Pay 25")
else:
    print("You can't Ride")