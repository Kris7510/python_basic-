flower = input()
number = int(input())
budget = int(input())

total = 0
price_roses = 5
price_dahlias = 3.8
price_tulips = 2.8
price_narcissus = 3
price_gladiolus = 2.5

if flower == "Roses":
    if number > 80:
        all_flower = number * price_roses
        total =  all_flower * 0.9

    else:
        total = number * price_roses

elif flower == "Dahlias":
    if number > 90:
        all_flower = number * price_dahlias
        total = all_flower * 0.85

    else:
        total = number * price_dahlias

elif flower == "Tulips":
    if number > 80:
        all_flower = number * price_tulips
        total = all_flower * 0.85


    else:
        total = number * price_tulips

elif flower == "Narcissus":
    if number < 120:
        all_flower = number * price_narcissus
        total = all_flower * 1.15

    else:
        total = number * price_narcissus

elif flower == "Gladiolus":
    if number < 80:
        all_flower = number * price_gladiolus
        total = all_flower * 1.20

    else:
        total = number * price_gladiolus




if budget >= total:
    print(f"Hey, you have a great garden with {number} {flower} and {budget - total:.2f} leva left.")


else:
    print(f"Not enough money, you need {total - budget:.2f} leva more.")
