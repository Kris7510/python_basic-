month = input()
night = int(input())

studio = 0
apartment = 0

if month == "May" or month == "October":
    studio = 50 * night
    apartment = 65 * night

    if night > 14:
         studio *= 0.7
    elif night > 7:
         studio *= 0.95

elif month == "June" or month == "September":
    studio = 75.2 * night
    apartment = 68.7 * night

    if night > 14:
        studio *= 0.8

elif month == "July" or month == "August":
    studio = 76 * night
    apartment = 77 * night

if night > 14:
    apartment *= 0.90

print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")