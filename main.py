MENU = {
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 150,

        },
        "cost": 1.5,
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
    "water": 10000,
    "milk": 10000,
    "coffee": 10000,
}

do_coffee = False
machine = True
answer = ''
count_money = False

total_money = 0
change = 0
machine_money = 0

quarters = 0
dimes = 0
nickles = 0
pennies = 0


def compare():
    global count_money
    global quarters
    global dimes
    global nickles
    global pennies
    keep_comparing = True
    for key in resources:
        while keep_comparing:
            if MENU[answer]["ingredients"][key] < resources[key]:
                print("Please insert coins")
                quarters = int(input("how many quarters?:"))
                dimes = int(input("how many dimes?:"))
                nickles = int(input("how many nickles?:"))
                pennies = int(input("how many pennies?:"))
                keep_comparing = False
                count_money = True
            else:
                print(f"Sorry there is not enough {key}.")


def money():
    global machine_money
    global total_money
    global do_coffee
    global change
    total_money = int(quarters) * 0.25 + int(dimes) * 0.10 + int(pennies) * 0.05 + int(pennies) * 0.01
    if total_money == MENU[answer]["cost"]:
        do_coffee = True
        machine_money += MENU[answer]["cost"]
    if total_money > MENU[answer]["cost"]:
        do_coffee = True
        change = total_money - MENU[answer]["cost"]
        print(f"Here is ${change} dollars in change.”")
        machine_money += MENU[answer]["cost"]
    else:
        print("Sorry that's not enough money. Money refunded.")

def prep_coffe():
    global resources
    for key in resources:
        resources[key] -= MENU[answer]["ingredients"][key]
    print(f"Here is your {answer}. Enjoy!")


while machine:
    answer = input("What would you like? (espresso/latte/cappuccino):")
    if answer == "off":
        on = False
    if answer == "report":
        print(resources)
        print(f"money: ${machine_money}")
    else:
        compare()
        if count_money:
            money()
            if do_coffee:
                prep_coffe()


