from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine 

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True



while is_on :
    options = menu.get_items()
    choice = input(f"What would wou like to take : {options} : ")
    if choice == "report":
        # to get a report 
        money_machine.report()
        coffee_maker.report()
    elif choice == "off":
        is_on = False
    else:
        drink = menu.find_drink(choice)
        resource = coffee_maker.is_resource_sufficient(drink)
        
        if resource == True : 
            money = money_machine.make_payment(drink.cost)
            if money == True:
                coffee_maker.make_coffee(drink)
            else:
                print("Not enough monney")
        else:
            print("Sorry not enough resources available")
