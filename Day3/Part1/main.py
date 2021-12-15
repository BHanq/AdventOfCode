f = open("data.txt", "r")
horizontal = 0
total = 0
gamma_sum = 0
gamma_tot = 0
epsi_tot = 0
tab = []
for x in f:
    tab.append(x)

tablength = len(tab[0])-1
print(tablength)
for gamma in range(0, tablength):
    for line in tab:
        if(line[gamma] == "1"):
            gamma_sum +=1
    if(gamma_sum > 500):
        gamma_tot += 2**(tablength-1-gamma)
    else:
        epsi_tot += 2**(tablength-1-gamma)
    gamma_sum = 0

print(gamma_tot*epsi_tot)