budget = float(input())
screenwriters = int(input())
outfit_put_screenwriters = float(input())
decor =  0.1 * budget

if screenwriters > 150:
    outfit_put_screenwriters *= 0.9

screenwriters_total = screenwriters * outfit_put_screenwriters


total = screenwriters_total + decor

if total > budget:
    needed_money = total - budget
    print(f"Not enough money!")
    print(f" Wingard needs {needed_money:.2f} leva more.")

if total < budget:
    left_money = budget - total
    print("Action!")
    print(f"Wingard starts filming with {left_money:.2f} leva left.")


