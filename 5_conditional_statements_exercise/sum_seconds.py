first_time = int(input())
second_time = int(input())
third_time = int(input())

total = first_time + second_time + third_time

total_min  =  total // 60
total_sec  =  total % 60

if total_sec < 10:
    print  (f"{total_min}:0{total_sec} ")
else:
    print(f"{total_min}:{total_sec} ")


