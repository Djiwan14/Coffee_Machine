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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickle": 0.05,
    "penny": 0.01,
}


def payment():
    quarters = int(input("how many quarters? ")) * coins['quarter']
    dimes = int(input("how many dimes? ")) * coins['dime']
    nickles = int(input("how many nickles? ")) * coins['nickle']
    pennies = int(input("how many pennies? ")) * coins['penny']
    return round(quarters + dimes + nickles + pennies, 2)


def work_with_resources(answer):
    if answer == "espresso":
        resources['water'] -= MENU[answer]['ingredients']['water']
        resources['coffee'] -= MENU[answer]['ingredients']['coffee']
    else:
        resources['water'] -= MENU[answer]['ingredients']['water']
        resources['coffee'] -= MENU[answer]['ingredients']['coffee']
        resources['milk'] -= MENU[answer]['ingredients']['coffee']


money = 0
continue_to_work = True

while continue_to_work:
    answer = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if answer == "report":
        print(f"Water : {resources['water']}\nMilk : {resources['milk']}\nCoffee : {resources['coffee']}\nMoney : ${money}")
    elif answer == "off":
        continue_to_work = False
        print("Bye bye")
    elif answer == "espresso":
        if resources['water'] >= MENU[answer]['ingredients']['water']:
            if resources['coffee'] >= MENU[answer]['ingredients']['coffee']:
                work_with_resources(answer)
                print("Please insert coins.")
                change = payment() - MENU['espresso']['cost']
                if change >= 0:
                    print(f"Here is {change} in change")
                    print("Here is your espresso ☕. Enjoy!")
                    money += MENU['espresso']['cost']
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print("Sorry there is not enough coffee")
        else:
            print("Sorry there is not enough water")
    elif answer == "latte":
        if resources['water'] >= MENU[answer]['ingredients']['water']:
            if resources['coffee'] >= MENU[answer]['ingredients']['coffee']:
                if resources['milk'] >= MENU[answer]['ingredients']['milk']:
                    work_with_resources(answer)
                    print("Please insert coins.")
                    change = payment() - MENU['latte']['cost']
                    if change >= 0:
                        print(f"Here is {change} in change")
                        print("Here is your latte ☕. Enjoy!")
                        money += MENU['latte']['cost']
                    else:
                        print("Sorry that's not enough money. Money refunded.")
                else:
                    print("Sorry there is not enough milk")
            else:
                print("Sorry there is not enough coffee")
        else:
            print("Sorry there is not enough water")
    elif answer == "cappuccino":
        if resources['water'] >= MENU[answer]['ingredients']['water']:
            if resources['milk'] >= MENU[answer]['ingredients']['milk']:
                if resources['coffee'] >= MENU[answer]['ingredients']['coffee']:
                    work_with_resources(answer)
                    print("Please insert coins.")
                    change = round(payment() - MENU[answer]['cost'], 2)
                    if change > 0:
                        print(f"Here is {change} in change ")
                        print("Here is your cappuccino ☕. Enjoy!")
                        money += MENU[answer]['cost']
                    else:
                        print("Sorry there is not enough money")
                else:
                    print("Sorry there is not enough coffee")
            else:
                print("Sorry there is not enough milk")
        else:
            print("Sorry there is not enough water")
