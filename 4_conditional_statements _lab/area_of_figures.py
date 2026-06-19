from math import pi

figures = input()

if figures == "square":

    sidea = float(input())
    area = sidea * sidea
    print(f"{area:.3f}")     # zapomni


elif figures == "rectangle":
    sidea = float(input())
    sideb = float(input())
    area = sidea * sideb
    print(f"{area:.3f}")

elif figures == "circle":
    radius = float(input())

    area =   pi * radius ** 2
    print(f"{area:.3f}")


elif figures == "triangle":
    sidea = float(input())
    high = float(input())

    area = (sidea * high) / 2
    print(f"{area:.3f}")

else :
    print ("The figures are not found")
