MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def resources_sufficient(drink_ingredients):
    for item in drink_ingredients:
        if item in resources:
            if resources[item] < drink_ingredients[item]:
                print(f"Sorry there is not enough {item}")
                return False
    return True  

def calculate_coins():
    quarters = int(input("How many quarters :"))
    dimes = int(input("How many dimes :"))
    nickles = int(input("How many nickles :"))
    pennies = int(input("How many pennies :"))
    
    Total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return Total
    
def is_transaction_successful(money_received , drink_cost):   
    
    global profit 
    
    if money_received >= drink_cost:
        
        change = round(money_received - drink_cost, 2)
        print(f"Here is the change: ${change}")
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

def main():
    is_on = True
    while is_on :
        choice =  input("What would you like to order (espresso/latte/cappuccino) : ").lower()
        if choice == "off" :
            is_on = False
        elif choice == "report":
            
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
        elif choice in MENU:
            drink = MENU[choice]
            if resources_sufficient(drink["ingredients"]):
                payment = calculate_coins()
                if is_transaction_successful(payment , drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
        else:
            print("Invalid choice. Please select a valid drink.")

main()
                
            