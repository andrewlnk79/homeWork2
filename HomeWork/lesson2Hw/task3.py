import random
spisok = list(map(int, input().split()))
num = 0
while num != 10:
    randomONE = random.randint(0, 9)
    randomTWO = random.randint(0, 9)
    if randomONE != randomTWO:
        spisok[randomONE], spisok[randomTWO] = spisok[randomTWO], spisok[randomONE]
        num += 1
print(spisok)