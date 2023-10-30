"""
Name: James Wong
Date: Oct 21 2022
Professor: Brian Sarlo
Class: 1026A - 002
Python Ver: 3.9
Program: Create a receipt for the user's order from order.py
"""

TAXES = 1.13            # write the tax as a constant hold the toppings of each pizza


# function to create the receipt
def generateReceipt(pizzaOrder):
    price = 0
    if len(pizzaOrder) <= 0:        # if the user did not order pizza
        print("You did not order anything")
    else:                           # if the user ordered pizza

        print("Your order:")
        cost = 0
        for x in range(len(pizzaOrder)):        # run a loop for the number of items in the list
            
            # setting prices for each size
            if pizzaOrder[x][0] == "S":         
                price = 7.99
                topPrice = 0.50
                cost += 7.99
            elif pizzaOrder[x][0] == "M":
                price = 9.99
                topPrice = 0.75
                cost += 9.99
            elif pizzaOrder[x][0] == "L":
                price = 11.99
                topPrice = 1.00
                cost += 11.99
            elif pizzaOrder[x][0] == "XL":
                price = 13.99
                topPrice = 1.25
                cost += 13.99
            else:
                print("Invalid Input")

            # format the print for each # pizza, their size and their cost
            print("Pizza {}: {:2} {:20.2f}".format(x + 1, pizzaOrder[x][0], price))  
            
            # put the toppings in a list
            toppingList = pizzaOrder[x][1]

            # run a loop for as many toppings in each list
            for d in range(len(toppingList)):
                print("- {}".format(toppingList[d]))      # print proper receipt formatting
                hold = d                                  # hold the value of d to see if there are more than 3 toppings

            if hold >= 3:                       # checking the number of toppings
                extraTop = hold - 2             # getting the number of extra toppings

                n = 0
                while n < extraTop:
                    cost += topPrice

                    # if the size is one character long and if the size is 2 characters long
                    if len(pizzaOrder[x][0]) == 1:
                        print("Extra Topping ({}) {:14.2f}".format(pizzaOrder[x][0], topPrice))
                    elif len(pizzaOrder[x][0]) == 2:
                        print("Extra Topping ({}) {:13.2f}".format(pizzaOrder[x][0], topPrice))

                    n += 1

        totalCost = cost*TAXES
        tax = totalCost - cost                      # calculating the tax added
        print("Tax: {:27.2f}".format(tax))          # print the tax amount
        print("Total: {:25.2f}".format(totalCost))  # print the total amount