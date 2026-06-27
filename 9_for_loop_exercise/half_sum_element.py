import sys

num = int(input())

max_num = -sys.maxsize
total_sum = 0

for i in range(num):
    new_num = int(input())
    if new_num >= max_num:
        max_num = new_num
    total_sum += new_num

total_sum = total_sum - max_num

if max_num == total_sum:
    print("Yes")
    print(f"Sum = {abs(total_sum)}")
else:
    print(f"No")
    print(f"Diff = {abs(max_num - total_sum)}")


