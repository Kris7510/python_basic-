
budget = int(input())
season = input()
fishermen = int(input())

if season == "Spring":
    total = 3000
elif season == "Summer":
    total = 4200
elif season == "Autumn":
    total = 4200
else:
    total = 2600

if fishermen <= 6:
    total  = total * 0.90
elif fishermen <= 11:
    total = total * 0.85
else:
    total = total * 0.75

if fishermen % 2 == 0 and season != "Autumn":
    total  = total * 0.95

if budget >= total:
    print(f"Yes! You have {budget - total:.2f} leva left.")
else:
    print(f"Not enough money! You need {total - budget:.2f} leva.")
