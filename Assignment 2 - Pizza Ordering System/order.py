"""
Name: James Wong
Date: Oct 21 2022
Professor: Brian Sarlo
Class: 1026A - 002
Python Ver: 3.9
Program: Prompt the user for their pizza order
        Ask the user for the size of their pizza
        Ask the for their toppings until they input x
        Add the pizza to the order list
        repeat until user is done ordering pizzas
"""
import pizzaReceipt     # import so the functions in pizzaReceipt are callable

# price for ordering and topping
def ordercost():
    print("Small(S): $7.99, Topping $0.50")
    print("Medium(M): $9.99, Topping $0.75")
    print("Large(L): $11.99, Topping $1.00")
    print("Extra Large(XL): $13.99, Topping $1.25")

# instructions for ordering
def orderInst():
    print("'No' and 'Q' will exit the program and send you the receipt")
    print("Anything else will order a pizza")

# instructions for toppings
def toppingInst():
    print("Each pizza comes with three free toppings.")
    print("Each topping added after that will vary in cost depending on the size of the pizza")
    print("Input 'LIST' to see topping menu")

# list of toppings
LIST = ('ONION', 'SPINACH', 'HAM', 'TOMATO', 'BROCCOLI', 'BACON', 'GREEN PEPPER', 'PINEAPPLE', 'GROUND BEEF', 'MUSHROOM',
'HOT PEPPER', 'CHICKEN', 'OLIVE', 'PEPPERONI', 'SAUSAGE')
orderList = []      # order list
morePizza = True    # parameter for looping multiple pizzas

ordercost()     # output the pricing of all pizzas

# while loop to keep looping the request for more than one pizza
while morePizza:
    toppingCost = 0     # set cost of toppings to 0
    orderInst()         # instructions on how to order
    order = input("Do you want to order a pizza? ")
    order = order.upper()           # set order to all capitals

    if order == "NO" or order == "Q"  or order == "":           # exit pizza builder
        pizzaReceipt.generateReceipt(orderList)
        morePizza = False

    else:      # continue making pizza

        sizeCheck = True
        while sizeCheck:
            size = input("Choose a size:")
            size = size.upper()  # change case to all upper
            if size == "S":
                sizeCheck = False
            elif size == "M":
                sizeCheck = False
            elif size == "L":
                sizeCheck = False
            elif size == "XL":
                sizeCheck = False
            else :
                print("Invalid input")

        countTopping = True     # set conditional to true
        toppings = []           # make topping list
        count = 3               # counter for 3 free toppings
        toppingInst()           # instructions on how to add toppings
        while countTopping:
            topping = input("Type in one of our toppings. When you are done adding toppings, enter \"X\"\n")      # ask the user for their toppings
            topping = topping.upper()               # change case to all upper

            if topping in LIST:                     # if the topping user inputted is in the list
                toppings.append(topping)            # add the topping to the toppings list

                print("Added {} to your pizza".format(topping))     # topping was added text

            elif topping == "LIST":                 # print the topping selection
                print(LIST)
            elif topping == "X":                    # all toppings are chosen
                countTopping = False
            else:                                   # invalid topping
                print("Invalid Input")

        finalOrder = (size, toppings)               # put order into a list
        orderList.append(finalOrder)                # add the list to the order list
