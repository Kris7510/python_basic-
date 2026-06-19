needed_nylon= int(input())
needed_paint= int(input())
needed_thinner= int(input())
needed_hours= int(input())

price_nylon =  1.50
price_paint = 14.50
price_thinner =  5.00
nylon_bag = 0.40

total_nylon = (needed_nylon + 2) * price_nylon
total_paint = (needed_paint + needed_paint * (10/100)) * price_paint
total_thinner = needed_thinner * price_thinner

total = total_nylon + total_paint + total_thinner + nylon_bag

workers = total * (30/100) * needed_hours

all_expense = total + workers

print(all_expense)
