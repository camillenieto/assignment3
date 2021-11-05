def total_of_apple() :
    total_apples = input("The total of apples that I want to buy : ")
    return total_apples

def total_of_orange() :
    total_oranges = input("The total of apples I want to buy : ")
    return total_oranges

def price_of_apple(apple_price=20) :
    print(f"The price of apple is {apple_price}.")

def price_of_orange(orange_price=25) :
    print(f"The price of orange is {orange_price}.")

def amount_of_apples(apples,apple_price) :
    return float(apples)*float(apple_price)
    
def amount_of_oranges(oranges,orange_price) :
    return float(oranges)*float(orange_price)

def display_output(sum_apples_oranges_func) :
    print(f"The total amount is {sum_apples_oranges_func}.")

# Steps
# 1. ask how many apples you want to buy and save to variable
apples = total_of_apple()
# 2. ask how many oranges you want to buy and save to variable
oranges = total_of_orange()
# 3. display the price of apple
price_of_apple()
apple_price = 20
# 4. display the price of orange
price_of_orange()
orange_price = 25
# 5. calculate the total amount of the apples you bought 
mul_apples = int(apples)*int(apple_price)
total_amount_apples = apples*apple_price
print(f"Total amount of apple is ",amount_of_apples(apples,apple_price))
# 6. calculate the total amount of the oranges you bought
mul_oranges = int(oranges)*int(orange_price)
total_amount_oranges = oranges*orange_price
print(f"Total amount of orange is ",amount_of_oranges(oranges,orange_price))
# 7. display the result
sum_apples_oranges = int(mul_apples)+int(mul_oranges)
display_output(sum_apples_oranges)
#print(f"The total amount is {sum_apples_oranges}")