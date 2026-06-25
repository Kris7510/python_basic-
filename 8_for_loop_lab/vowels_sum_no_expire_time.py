text  = input()
total_points = 0


for char in text:
    points = 0

    if char == 'a':
        points = 1

    if char == 'e':
        points = 2

    if char == 'i':
        points = 3

    if char == 'o':

        points = 4
    if char == 'u':

        points = 5

    total_points = total_points + points

print(total_points)





