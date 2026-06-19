animal = input()
result = ""

if animal == 'dog':
    result = 'mammal'
elif animal == 'tortoise' or animal == 'crocodile' or animal == 'snake' :
    result = 'reptile'
else:
    result = 'unknown'
print(result)