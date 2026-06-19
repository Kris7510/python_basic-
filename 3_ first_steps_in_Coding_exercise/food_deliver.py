chicken  = int(input())
fish = int(input())
vegan = int(input())
delivery = 2.50

price_chicken = 10.35
price_fish = 12.40
price_vegan = 8.15

total_chicken  = chicken * price_chicken
total_fish = fish * price_fish
total_vegan = vegan * price_vegan


dessert = (20/100) * (total_chicken+ total_fish + total_vegan)

total = total_fish + total_vegan + total_chicken +  dessert + delivery


print(total)
