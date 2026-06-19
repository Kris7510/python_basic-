fruit = input()
day_of_the_week = input()
quantity = float(input())

result = 0

if day_of_the_week == "Saturday" or day_of_the_week == "Sunday":

    price_banana = 2.70
    price_apple = 1.25
    price_orange = 0.90
    price_grapefruit = 1.60
    price_kiwi = 3.00
    price_pineapple = 5.60
    price_grape = 4.20

    if fruit == "banana":
        result = price_banana * quantity
    elif fruit == "apple":
        result = price_apple * quantity
    elif fruit == "orange":
        result = price_orange * quantity
    elif fruit == "grapefruit":
        result = price_grapefruit * quantity
    elif fruit == "kiwi":
        result = price_kiwi * quantity
    elif fruit == "pineapple":
        result = price_pineapple * quantity
    elif fruit == "grapes":
        result = price_grape * quantity

elif (day_of_the_week == "Monday"
      or day_of_the_week == "Tuesday"
      or day_of_the_week == "Wednesday"
      or day_of_the_week == "Thursday"
      or day_of_the_week == "Friday"):

    price_banana = 2.50
    price_apple = 1.20
    price_orange = 0.85
    price_grapefruit = 1.45
    price_kiwi = 2.70
    price_pineapple = 5.50
    price_grape = 3.85

    if fruit == "banana":
        result = price_banana * quantity
    elif fruit == "apple":
        result = price_apple * quantity
    elif fruit == "orange":
        result = price_orange * quantity
    elif fruit == "grapefruit":
        result = price_grapefruit * quantity
    elif fruit == "kiwi":
        result = price_kiwi * quantity
    elif fruit == "pineapple":
        result = price_pineapple * quantity
    elif fruit == "grapes":
        result = price_grape * quantity

if result > 0:
    print(f"{result:.2f}")

else:
   print("error")
