competitions = int(input())
starting_points = int(input())

points = 0
num_winner = 0
competitions_points = 0

for _ in range(competitions):

    place = input()

    if  place == 'W':
        points = 2000
        num_winner += 1

    elif place == 'F':
         points = 1200

    elif place == 'SF':
         points = 720

    competitions_points += points

final_points = starting_points + competitions_points
average_points = competitions_points / competitions
percent_wins = (num_winner / competitions) * 100

print(f"Final points: {int(final_points)}" )
print(f"Average points: {int(average_points)}" )
print(f"{percent_wins:.2f}%" )




