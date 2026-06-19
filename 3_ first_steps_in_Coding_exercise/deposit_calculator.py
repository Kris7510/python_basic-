deposit_sum = int(input())
time_deposit = int(input())
year_interest = float(input())

total_sum = deposit_sum + time_deposit * ((deposit_sum * year_interest / 100)/12)

print(total_sum)

