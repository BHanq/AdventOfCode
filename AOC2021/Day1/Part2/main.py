varPrec = 9000
sum1 = 9000
sum2 = 0
increment= 0
tab = []
f = open("data.txt", "r")
for x in f:
    tab.append(int(x))

for index in range(0, len(tab)-2):
    for triple in range(0,3):
        sum2 += tab[index+triple]


    if (sum1 < sum2):
        increment += 1
    sum1 = sum2
    sum2 = 0
print(increment)