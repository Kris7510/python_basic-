
budget = float(input())
season = (input())

destination = ""
place = ""
price = 0.00


if budget <= 100:
    if season == "summer":
        price = budget * 0.3
        destination = "Bulgaria"
        place = "Camp"

    else:
        price = budget * 0.7
        destination = "Bulgaria"
        place = "Hotel"

elif budget <= 1000:
    if season == "summer":
        price = budget * 0.4
        destination = "Balkans"
        place = "Camp"

    else:
        price = budget * 0.8
        destination = "Balkans"
        place = "Camp"

elif budget > 1000:
    price = budget * 0.9
    destination = "Europe"
    place = "Hotel"

print(f"Somewhere in {destination}")
print(f"{place} - {price:.2f}")