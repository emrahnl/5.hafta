##Sayi Tahmin Oyunu
import random
number=random.randint(0,100)

guess=int(input("Pls guess a number between 0-100: "))
count=1
while number!=guess:
    if number>guess:
        print("+")
    else:
        print("-")
    guess=int(input("Pls guess a number between 0-100: "))
    count=count+1
print("You found the number")
print("Number of tries:", count)


