from math import floor

record = float(input())
distance = float(input())
time_second_per_meter = float(input())

swim_time = distance * time_second_per_meter

delay = floor(distance / 15) * 12.5

total_time = (swim_time + delay)

if record <= total_time:
    needed_time = total_time - record
    print(f"No, he failed! He was {needed_time:.2f} seconds slower.")

else:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")