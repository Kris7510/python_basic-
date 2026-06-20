time = input()
vertical = int(input())
horizontal = int(input())

total = 0
Premiere = 12
Normal = 7.5
Discount  = 5

if time == "Premiere":
    total = Premiere * vertical * horizontal

elif time == "Normal":
    total = Normal * vertical * horizontal

elif time == "Discount":
    total = Discount * vertical * horizontal

print(f"{total:.2f} leva")






