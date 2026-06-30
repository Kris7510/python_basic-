actor_name = input()
academy_points = float(input())
judges = int(input())

result = academy_points

for _ in range(judges):
    judges_name =input()
    judges_points = float(input())
    result = result + (len(judges_name) * judges_points) / 2

    if result > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {result:.1f}!")
        break

else:
    print(f"Sorry, {actor_name} you need {1250.5 - result:.1f} more!")
