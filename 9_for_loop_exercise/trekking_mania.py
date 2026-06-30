groups = int(input())

total_people = 0
musala = 0
mont_blanc = 0
kilimanjaro = 0
k2 = 0
everest = 0

for _ in range(groups):
    people = int(input())
    total_people += people

    if people <= 5:
        musala += people
    elif people <= 12:
        mont_blanc += people
    elif people <= 25:
        kilimanjaro += people
    elif people <= 40:
        k2 += people
    else:
        everest += people

precent_musala = musala / total_people * 100
precent_mont_blanc = mont_blanc / total_people * 100
precent_kilimanjaro = kilimanjaro / total_people * 100
precent_k2 = k2 / total_people * 100
precent_everest = everest / total_people * 100

print(f"{precent_musala:.2f}%")
print(f"{precent_mont_blanc:.2f}%")
print(f"{precent_kilimanjaro:.2f}%")
print(f"{precent_k2:.2f}%")
print(f"{precent_everest:.2f}%")
