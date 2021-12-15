varPrec = 9000
sum = 0
f = open("data.txt", "r")
for x in f:
    if (varPrec < int(x)):
        sum = sum + 1
    varPrec = int(x)
print(sum)