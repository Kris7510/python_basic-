
day_of_stay = int(input()) - 1
type_of_room = input()
review = input()
total = 0

price_room_for_one_person = day_of_stay * 18
price_apartment = day_of_stay * 25
price_president_apartment = day_of_stay * 35

if type_of_room == 'room for one person':
    total = price_room_for_one_person

elif type_of_room == 'apartment':
    if day_of_stay < 10:
        total = price_apartment * 0.7

    elif 10 <= day_of_stay <= 15:
        total = price_apartment * 0.65

    else:
        total = price_apartment * 0.5

elif type_of_room == 'president apartment':
    if day_of_stay < 10:
        total = price_president_apartment * 0.9

    elif 10 <= day_of_stay <= 15:
        total = price_president_apartment * 0.85

    else:
        total = price_president_apartment * 0.8

if review == "positive":
    total = total * 1.25

elif review == "negative":
    total = total * 0.90


print(f"{total:.2f}")
