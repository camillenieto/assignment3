def amount_of_money() :
    money_func = float(input("The amount of money that you have is "))
    return money_func

def price_of_apple() :
    apple_func = float(input("What is the price of the apple? "))
    return apple_func

def maximum_of_apples(amount_money,price_apple) :
    return float(amount_money)//float(price_apple)

def remaining_of_money(amount_money,maximum_apples,price_apple) :
    return (float(amount_money)-float(maximum_apples) * float(price_apple))

def display_output(apples_func,rmoney_func) :
    print(f"You can buy {apples_func} apples and your change is {rmoney_func} pesos.")

# Steps
# 1. enter how much money do you have
amount_money = amount_of_money()
# 2. ask how much is the apple
price_apple = price_of_apple()
# 3. calculate the maximum number of apples that you can buy and calculate the remaining money that you will have
amount_money
price_apple
maximum_apples = amount_money//price_apple
remaining_money = (amount_money)-((maximum_apples) *(price_apple))
print("Maximum apples that you can buy is",maximum_of_apples(amount_money,price_apple), "and the remaining money that you will have is",remaining_of_money(amount_money,maximum_apples,price_apple))
# 5. display the result
display_output(maximum_apples,remaining_money)
