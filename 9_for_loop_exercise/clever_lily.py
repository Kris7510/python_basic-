age = int(input())
washer_price = float(input())
unit_price_per_toy = int(input())

total_toys = 0
given_money = 0
toys = 0

for i in range(1 ,age + 1):
    if i % 2 == 0:
      given_money += (5 * i) - 1
    else:
        toys += 1

total_toys = unit_price_per_toy * toys

all_money = given_money + total_toys

if washer_price <= all_money:
    print(f"Yes! {abs(all_money - washer_price):.2f}")
else:
    print(f"No! {abs(all_money - washer_price):.2f}")

