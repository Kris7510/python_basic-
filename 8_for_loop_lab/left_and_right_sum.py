num = int(input())
total_left = 0
total_right = 0

for left in range(num):
    new_num = int(input())
    total_left = new_num + total_left

for right in range(num):
    new_num = int(input())
    total_right = new_num + total_right


if total_left == total_right:
    print(f"Yes, sum = {total_left}")

elif total_left > total_right:
    print(f"No, diff = {total_left-total_right}")

else:
    print(f"No, diff = {total_right-total_left}")

