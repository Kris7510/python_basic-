
num = int(input())
bonus  = 0

if 100 >= num:
   bonus = 5


elif 100 < num <= 1000:
    bonus = num * 0.2

else:

    bonus = num * 0.1

if num % 2 == 0:
    bonus += 1

elif num % 10 == 5:
    bonus += 2

total = num + bonus
print(f"{bonus} bonus" )
print(f"{total} total" )
