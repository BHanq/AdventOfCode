f = open("data.txt", "r")
horizontal = 0
vertical = 0
aim = 0
for x in f:
    tab = x.split(" ")
    value = int(tab[1])
    if tab[0]== "forward":
        horizontal += value
        vertical += aim * value
    elif tab[0] == "up":
        aim -= value
    else:
        aim += value
mult = horizontal * vertical
print(mult)