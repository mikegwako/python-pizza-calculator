# Pizza order cost calculator program

print("Welcome to the pizza delivery service!")

size = input("Enter pizza size (small or large): ")
toppings = int(input("Enter number of toppings: "))
distance = float(input("Enter delivery distance in miles: "))

# figure out base price based on size
if size == "small":
    pizza_price = 8
elif size == "large":
    pizza_price = 12
else:
    pizza_price = 0
    print("Wrong size entered")

# calculate toppings cost ($1 each)
toppings_cost = toppings * 1

# delivery fee: $2 for first 5 miles, then $1 per extra mile
if distance <= 5:
    delivery_cost = 2
else:
    delivery_cost = 2 + (distance - 5) * 1

# add everything together and print final bill
total_bill = pizza_price + toppings_cost + delivery_cost

print(f"Your total bill is ${total_bill}")