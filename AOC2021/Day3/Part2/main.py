import math

horizontal = 0
total = 0


# Find most common bits
def mostCommon(tab):
    gamma_sum = 0
    mostcommon = ""
    tablength = len(tab[0]) - 1
    remainingline = float(float(len(tab)) / 2.0)
    print(remainingline)
    for gamma in range(0, tablength):
        for line in tab:
            if (line[gamma] == "1"):
                gamma_sum += 1
        if gamma_sum >= remainingline:
            mostcommon += "1"
        else:
            mostcommon += "0"
        gamma_sum = 0
    # Print most commons
    return mostcommon


# Rating value function definintion
def findRatingValue(list, criteria, index):
    if len(list) == 1:
        return list[0]
    else:
        print(list)
        mostcommon = mostCommon(list)
        print("Mostcommon", mostcommon)
        newList = []
        for line in list:
            if criteria == 1:
                comparison = line[index] == mostcommon[index]
            else:
                comparison = line[index] != mostcommon[index]
            if comparison:
                newList.append(line)
        return findRatingValue(newList, criteria, index + 1)


f = open("data.txt", "r")
tab = []
for x in f:
    tab.append(x)
beginTab = mostCommon(tab)
print(beginTab)
# Oxygen generator rating
oxygen = findRatingValue(tab, 1, 0)

scrub = findRatingValue(tab, 0, 0)
print(oxygen, "&", scrub)
print(int(oxygen, 2), "&", int(scrub, 2))
print(int(oxygen, 2) * int(scrub, 2))
