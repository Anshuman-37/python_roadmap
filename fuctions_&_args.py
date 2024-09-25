# The * acts as in iterable over an iterable object
# nums = [1,2,3,4,5,6,7,8,9,10]
# print(*nums)

# If I have a function for example
def order_pizza(size, *toppings, **details):
    print(f"A '{size}' pizza has these toppings:")
    for topping in toppings:
        print(f"- {topping}")

    print('The details for the pizza are as follows:')
    for detail in details:
        print(f"- {detail}")

# When I call it in this way there is no arguments so only large will be printed
# Size automatically is assigned the first value that is passed in
print("\nNo args and No kwargs\n",'-'*100)
order_pizza("large")

## As now this function contains the *arguments toppings will be populated
print("\nargs but No kwargs\n",'-'*100)
order_pizza("large", "cheese", "pepperoni")

## As now this function contains keyword arguments these things will show up in the print operation
print("\nargs and kwargs\n",'-'*100)
order_pizza("large", "cheese", "pepperoni", paid=True, ordered_online=True)
