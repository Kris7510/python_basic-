budget = float(input())
video_card = int(input())
processor = int(input())
ram = int(input())


video_card_price_per_one = 250 * video_card
processor_price_per_one = (0.35 * video_card_price_per_one) * processor
ram_price_per_one = (0.10 * video_card_price_per_one) * ram

total = video_card_price_per_one + processor_price_per_one + ram_price_per_one

if video_card > processor:
   discount = 0.15 * total
   total -= discount

if budget >= total:
    plus_money = budget - total
    print(f"You have {plus_money:.2f} leva left!")

else:
    needed_money = total - budget
    print(f"Not enough money! You need {needed_money:.2f} leva more!")

