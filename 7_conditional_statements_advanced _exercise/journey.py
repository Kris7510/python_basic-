budget = float(input())
season = input()

destination = ""
place = ""

if budget <= 100:

    if season == "summer":
        budget = budget * 0.3
        destination = "Bulgaria"
        place = "Camp"

    elif season == "winter":
        budget = budget * 0.7
        destination = "Bulgaria"
        place = "Hotel"

elif budget <= 1000:

    if season == "summer":
        budget = budget * 0.4
        destination = "Balkans"
        place = "Camp"

    elif season == "winter":
        budget = budget * 0.8
        destination = "Balkans"
        place = "Hotel"

else:
    budget = budget * 0.9
    destination = "Europe"
    place = "Hotel"

print(f"Somewhere in {destination}")

print(f"{place:} - {budget:.2f}")

