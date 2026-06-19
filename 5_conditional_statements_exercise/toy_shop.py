trip_price=float(input())
puzzle = int(input())
doll = int(input())
teddy = int(input())
minions = int(input())
trucks= int(input())

all_toys = puzzle + doll + teddy + minions + trucks

puzzle_price = 2.6
doll_price = 3
teddy_bear_price = 4.1
minions_price = 8.2
trucks_price = 2

all_puzzle_price = puzzle_price * puzzle
all_doll_price = doll_price * doll
all_teddy_bear_price = teddy_bear_price * teddy
all_minions_price = minions_price * minions
all_trucks_price = trucks_price * trucks

total = all_puzzle_price + all_doll_price + all_teddy_bear_price + all_minions_price + all_trucks_price

if all_toys >= 50:
    total = total * 0.75

total = total * 0.90

if total >= trip_price:
   needed_money = total - trip_price
   print(f"Yes! {needed_money:.2f} lv left.")

if total < trip_price:
    needed_money = trip_price - total
    print(f"Not enough money! {needed_money:.2f} lv needed.")
