city = input()
sells = float(input())
commission = -1


if city == 'Sofia':
    if 0 <= sells <= 500:
        commission = 0.05
    elif 500 < sells <= 1000:
        commission = 0.07
    elif 1000 < sells <= 10000:
        commission = 0.08
    else:
        commission = 0.12


elif city == 'Varna':
    if 0 <= sells <= 500:
        commission = 0.045
    elif 500 < sells <= 1000:
        commission = 0.075
    elif 1000 < sells <= 10000:
        commission = 0.1
    else:
        commission = 0.13

elif city == 'Plovdiv':
    if 0 <= sells <= 500:
        commission = 0.055
    elif 500 < sells <= 1000:
        commission = 0.08
    elif 1000 < sells <= 10000:
        commission = 0.12
    else:
        commission = 0.145


if commission >= 0 and sells >= 0 :
    final = sells * commission
    print(f"{final:.2f}")

else:
    print("error")

