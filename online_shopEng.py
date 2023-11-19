# code of online shop
import random
print("Welcome to MarketFood")
pay = input()
amount = random.randint(10, 100)
moneys = random.randint(10, 500)
delivery = random.randint(10, 45)
print("your money account",moneys)
print(pay, "required", amount)
x3 = int(input())
if x3 > moneys:
    print("you dont have that much money!")
else:
    if x3 < amount:
        print("you didnt give out enough")
    elif x3 > amount:
        print("you have given too much, we will give you change")
        change = x3 - amount
        moneys + change
        print("your money account after payment:", moneys - x3 + change)
        print("the courier will a arrive", delivery, "minutes")
    else:
        print("оплачено")
        print("your money account after payment", moneys - x3)
        print("the courier will a arrive", delivery,"minutes")
        print("sorry for a bad translate")