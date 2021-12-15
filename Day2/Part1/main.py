f = open("data.txt", "r")
horizontal = 0
vertical = 0
for x in f:
    tab = x.split(" ")
    value = int(tab[1])
    if tab[0]== "forward":
        horizontal += value
    elif tab[0] == "up":
        vertical -= value
    else:
        vertical += value
mult = horizontal * vertical
print(mult)