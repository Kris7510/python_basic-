from math import ceil

serial_name = (input())
episode_time = int(input())
break_time = int(input())

lunch_time =  break_time * (1/8)
recreation = break_time * (1/4)
time_last = break_time - lunch_time - recreation

if time_last >= episode_time:
    time_1 = time_last - episode_time
    print(f"You have enough time to watch {serial_name} and left with {ceil(time_1):.0f} minutes free time.")

else:
     time_2 = episode_time - time_last
     print(f"You don't have enough time to watch {serial_name}, you need {ceil(time_2):.0f} more minutes.")

