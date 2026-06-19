hours = int(input()) * 60
minutes = int(input())

total_min = minutes + hours + 15

new_hours = total_min // 60
new_minutes = total_min % 60
if new_minutes > 59:
   new_hours += 1
   new_minutes = 0

if new_hours > 23:
    new_hours = 0

if new_hours < 1:
    new_hours = 0

if new_minutes < 10:
   new_minutes = "0" + str(new_minutes)

print (f"{new_hours}:{new_minutes}")



