num = int(input())
total_even = 0
total_odd = 0

for even in range(num):
    new_num = int(input())
    if even % 2 == 0:
        total_even = new_num + total_even
    else:
        total_odd = new_num + total_odd

if total_even == total_odd:
    print("Yes")
    print(f"Sum = {total_even}")
else:
    print("No")
    print(f"Diff = {abs(total_odd - total_even)}")