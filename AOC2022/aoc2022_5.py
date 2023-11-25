test = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

input = """
                        [R] [J] [W]
            [R] [N]     [T] [T] [C]
[R]         [P] [G]     [J] [P] [T]
[Q]     [C] [M] [V]     [F] [F] [H]
[G] [P] [M] [S] [Z]     [Z] [C] [Q]
[P] [C] [P] [Q] [J] [J] [P] [H] [Z]
[C] [T] [H] [T] [H] [P] [G] [L] [V]
[F] [W] [B] [L] [P] [D] [L] [N] [G]
 1   2   3   4   5   6   7   8   9 

move 2 from 2 to 8
move 2 from 1 to 6
move 8 from 7 to 1
move 7 from 5 to 4
move 1 from 6 to 4
move 1 from 6 to 3
move 6 from 3 to 5
move 9 from 8 to 1
move 3 from 6 to 7
move 14 from 4 to 1
move 6 from 1 to 7
move 16 from 1 to 9
move 6 from 1 to 4
move 1 from 8 to 6
move 4 from 1 to 5
move 11 from 9 to 7
move 2 from 1 to 8
move 1 from 6 to 7
move 1 from 8 to 7
move 1 from 8 to 3
move 7 from 4 to 3
move 14 from 7 to 6
move 8 from 6 to 9
move 19 from 9 to 2
move 1 from 1 to 2
move 2 from 9 to 7
move 9 from 7 to 8
move 2 from 2 to 8
move 16 from 2 to 9
move 4 from 8 to 2
move 1 from 7 to 9
move 3 from 9 to 6
move 3 from 3 to 6
move 11 from 9 to 2
move 7 from 5 to 3
move 2 from 5 to 9
move 6 from 6 to 4
move 1 from 6 to 4
move 4 from 6 to 8
move 5 from 9 to 1
move 4 from 1 to 7
move 3 from 2 to 6
move 3 from 4 to 1
move 1 from 4 to 1
move 2 from 1 to 3
move 4 from 3 to 7
move 1 from 5 to 2
move 3 from 1 to 6
move 15 from 2 to 5
move 3 from 6 to 3
move 13 from 3 to 8
move 2 from 4 to 2
move 9 from 5 to 4
move 2 from 2 to 5
move 5 from 7 to 5
move 10 from 8 to 6
move 1 from 2 to 5
move 10 from 4 to 6
move 4 from 8 to 6
move 3 from 7 to 1
move 3 from 1 to 9
move 1 from 2 to 1
move 8 from 5 to 2
move 3 from 6 to 9
move 6 from 8 to 5
move 6 from 9 to 2
move 1 from 1 to 9
move 10 from 2 to 1
move 4 from 8 to 5
move 10 from 5 to 9
move 11 from 9 to 7
move 5 from 7 to 9
move 1 from 9 to 2
move 3 from 2 to 9
move 2 from 2 to 8
move 4 from 9 to 5
move 4 from 1 to 9
move 5 from 5 to 2
move 5 from 1 to 4
move 21 from 6 to 9
move 3 from 2 to 9
move 2 from 8 to 1
move 25 from 9 to 6
move 4 from 5 to 7
move 1 from 4 to 6
move 6 from 6 to 4
move 3 from 4 to 6
move 7 from 7 to 3
move 4 from 9 to 1
move 3 from 7 to 8
move 2 from 9 to 8
move 2 from 2 to 8
move 4 from 1 to 3
move 9 from 6 to 2
move 13 from 6 to 4
move 13 from 4 to 5
move 1 from 5 to 8
move 2 from 2 to 3
move 6 from 5 to 3
move 19 from 3 to 6
move 1 from 4 to 9
move 2 from 8 to 1
move 5 from 2 to 3
move 5 from 1 to 9
move 7 from 5 to 4
move 1 from 8 to 3
move 1 from 2 to 6
move 8 from 6 to 3
move 1 from 9 to 8
move 11 from 4 to 2
move 1 from 4 to 6
move 1 from 2 to 8
move 5 from 3 to 4
move 4 from 9 to 6
move 1 from 6 to 8
move 9 from 3 to 1
move 7 from 2 to 9
move 1 from 2 to 6
move 3 from 1 to 8
move 2 from 2 to 3
move 3 from 9 to 7
move 3 from 4 to 7
move 2 from 4 to 3
move 2 from 3 to 5
move 8 from 6 to 4
move 6 from 8 to 6
move 2 from 9 to 4
move 5 from 8 to 6
move 3 from 7 to 5
move 1 from 5 to 8
move 1 from 8 to 2
move 1 from 5 to 1
move 11 from 4 to 9
move 2 from 6 to 3
move 2 from 2 to 4
move 6 from 1 to 2
move 6 from 2 to 1
move 3 from 7 to 3
move 2 from 4 to 7
move 4 from 6 to 5
move 7 from 3 to 7
move 5 from 9 to 6
move 22 from 6 to 8
move 2 from 6 to 5
move 2 from 8 to 4
move 14 from 8 to 7
move 11 from 7 to 4
move 3 from 8 to 1
move 9 from 7 to 8
move 10 from 1 to 4
move 1 from 7 to 4
move 4 from 8 to 7
move 6 from 4 to 9
move 7 from 4 to 1
move 3 from 4 to 8
move 1 from 5 to 8
move 8 from 5 to 3
move 4 from 3 to 9
move 7 from 8 to 9
move 3 from 8 to 3
move 2 from 8 to 2
move 7 from 9 to 1
move 2 from 2 to 8
move 8 from 9 to 1
move 8 from 1 to 7
move 7 from 1 to 5
move 7 from 7 to 1
move 11 from 9 to 8
move 9 from 8 to 5
move 2 from 8 to 5
move 3 from 1 to 8
move 2 from 3 to 7
move 6 from 4 to 1
move 6 from 1 to 6
move 5 from 7 to 1
move 2 from 4 to 6
move 1 from 3 to 5
move 4 from 7 to 4
move 2 from 8 to 7
move 10 from 5 to 6
move 9 from 6 to 1
move 8 from 1 to 6
move 1 from 7 to 2
move 9 from 6 to 4
move 2 from 4 to 3
move 3 from 8 to 1
move 1 from 2 to 4
move 4 from 4 to 1
move 7 from 4 to 3
move 3 from 3 to 2
move 1 from 7 to 6
move 9 from 6 to 7
move 6 from 7 to 4
move 2 from 7 to 2
move 6 from 4 to 7
move 2 from 2 to 9
move 1 from 2 to 4
move 1 from 7 to 4
move 4 from 7 to 6
move 4 from 5 to 4
move 1 from 2 to 5
move 1 from 7 to 5
move 1 from 2 to 6
move 6 from 4 to 3
move 9 from 3 to 9
move 4 from 6 to 2
move 7 from 3 to 8
move 22 from 1 to 7
move 1 from 1 to 7
move 2 from 8 to 3
move 4 from 5 to 6
move 2 from 3 to 2
move 6 from 2 to 8
move 3 from 8 to 6
move 1 from 4 to 8
move 1 from 1 to 8
move 8 from 6 to 7
move 7 from 8 to 9
move 22 from 7 to 4
move 3 from 5 to 6
move 1 from 8 to 1
move 2 from 8 to 2
move 3 from 6 to 4
move 1 from 1 to 3
move 15 from 9 to 1
move 5 from 1 to 5
move 3 from 7 to 6
move 5 from 5 to 6
move 4 from 4 to 3
move 6 from 6 to 9
move 7 from 7 to 6
move 5 from 6 to 7
move 4 from 1 to 9
move 3 from 7 to 4
move 2 from 9 to 7
move 5 from 3 to 5
move 3 from 6 to 3
move 5 from 4 to 6
move 10 from 9 to 5
move 1 from 2 to 9
move 1 from 3 to 5
move 1 from 2 to 9
move 3 from 1 to 6
move 2 from 9 to 2
move 7 from 6 to 5
move 15 from 4 to 9
move 2 from 4 to 5
move 1 from 3 to 4
move 9 from 9 to 1
move 1 from 9 to 2
move 2 from 9 to 4
move 11 from 5 to 4
move 1 from 9 to 3
move 1 from 6 to 8
move 4 from 7 to 8
move 4 from 8 to 9
move 15 from 4 to 7
move 1 from 6 to 7
move 1 from 3 to 7
move 6 from 9 to 6
move 1 from 3 to 7
move 1 from 2 to 1
move 1 from 9 to 5
move 3 from 6 to 1
move 11 from 1 to 4
move 6 from 5 to 1
move 2 from 2 to 5
move 1 from 5 to 7
move 2 from 6 to 1
move 7 from 5 to 7
move 3 from 5 to 6
move 4 from 6 to 1
move 11 from 4 to 3
move 1 from 8 to 5
move 23 from 7 to 6
move 18 from 6 to 9
move 1 from 5 to 9
move 1 from 4 to 2
move 3 from 3 to 7
move 3 from 3 to 8
move 17 from 1 to 8
move 5 from 6 to 5
move 2 from 7 to 1
move 20 from 8 to 2
move 4 from 7 to 2
move 3 from 9 to 5
move 7 from 9 to 7
move 6 from 9 to 2
move 1 from 1 to 8
move 3 from 9 to 4
move 7 from 5 to 2
move 6 from 7 to 1
move 1 from 1 to 8
move 3 from 2 to 6
move 1 from 7 to 6
move 2 from 8 to 9
move 35 from 2 to 4
move 3 from 3 to 2
move 1 from 5 to 7
move 2 from 3 to 9
move 3 from 1 to 6
move 2 from 2 to 1
move 32 from 4 to 7
move 3 from 4 to 8
move 3 from 9 to 5
move 1 from 1 to 2
move 21 from 7 to 5
move 2 from 2 to 1
move 3 from 1 to 2
move 15 from 5 to 1
move 3 from 6 to 7
move 3 from 4 to 6
move 3 from 8 to 5
move 1 from 9 to 3
move 8 from 7 to 2
move 6 from 5 to 2
move 9 from 1 to 6
move 4 from 7 to 1
move 2 from 5 to 4
move 2 from 4 to 3
move 3 from 5 to 4
move 17 from 2 to 7
move 3 from 3 to 5
move 2 from 4 to 8
move 1 from 4 to 3
move 5 from 7 to 9
move 1 from 3 to 6
move 4 from 1 to 7
move 4 from 6 to 7
move 2 from 5 to 2
move 1 from 1 to 3
move 10 from 6 to 4
move 1 from 3 to 7
move 20 from 7 to 8
move 8 from 4 to 8
move 1 from 2 to 8
move 4 from 9 to 1
move 3 from 7 to 4
move 2 from 4 to 9
move 2 from 6 to 3
move 1 from 2 to 8
move 1 from 7 to 6
move 1 from 9 to 5
move 3 from 5 to 9
move 4 from 9 to 2
move 1 from 4 to 5
move 1 from 5 to 3
move 3 from 2 to 4
move 1 from 9 to 7
move 1 from 2 to 1
move 1 from 7 to 1
move 11 from 1 to 2
move 3 from 1 to 7
move 25 from 8 to 5
move 1 from 6 to 3
move 1 from 6 to 2
move 7 from 8 to 2
move 9 from 2 to 8
move 2 from 4 to 7
move 2 from 5 to 7
move 2 from 5 to 2
move 5 from 5 to 1
move 7 from 5 to 1
move 2 from 4 to 9
move 3 from 5 to 6
move 1 from 1 to 8
move 1 from 5 to 6
move 1 from 4 to 7
move 1 from 9 to 2
move 3 from 5 to 2
move 2 from 6 to 9
move 3 from 9 to 8
move 1 from 5 to 4
move 3 from 3 to 9
move 10 from 1 to 5
move 4 from 2 to 8
move 2 from 6 to 1
move 3 from 9 to 7
move 1 from 1 to 9
move 1 from 4 to 3
move 1 from 9 to 2
move 9 from 8 to 2
move 2 from 3 to 7
move 2 from 7 to 6
move 3 from 5 to 6
move 4 from 8 to 6
move 4 from 8 to 3
move 4 from 3 to 2
move 4 from 6 to 8
move 1 from 7 to 9
move 2 from 1 to 8
move 2 from 8 to 3
move 1 from 9 to 2
move 13 from 2 to 4
move 6 from 5 to 7
move 2 from 5 to 7
move 10 from 2 to 4
move 11 from 7 to 8
move 1 from 6 to 4
move 4 from 6 to 7
move 24 from 4 to 9
move 11 from 7 to 4
move 1 from 3 to 8
move 1 from 3 to 5
move 4 from 4 to 2
move 5 from 4 to 2
move 9 from 2 to 5
move 4 from 9 to 5
move 1 from 5 to 1
move 2 from 5 to 7
move 2 from 2 to 5
move 1 from 1 to 7
move 2 from 2 to 3
move 18 from 9 to 6
move 9 from 8 to 1
move 2 from 9 to 5
move 5 from 1 to 8
move 2 from 8 to 7
move 4 from 8 to 4
move 5 from 8 to 7
move 10 from 5 to 1
move 10 from 7 to 4
move 4 from 5 to 8
move 14 from 1 to 9
move 6 from 9 to 8
move 1 from 5 to 1
move 12 from 6 to 9
move 4 from 6 to 8
move 11 from 8 to 5
move 1 from 6 to 1
move 19 from 9 to 7
move 2 from 3 to 5
move 13 from 7 to 5
move 3 from 7 to 1
move 4 from 8 to 9
move 2 from 7 to 6
move 7 from 4 to 8
move 5 from 8 to 1
move 1 from 1 to 3
move 1 from 7 to 2
move 6 from 1 to 6
move 1 from 2 to 5
move 1 from 8 to 1
move 1 from 8 to 2
move 2 from 4 to 8
move 5 from 6 to 1
move 2 from 4 to 7
move 2 from 9 to 6
move 1 from 6 to 5
move 4 from 6 to 2
move 1 from 9 to 5
move 2 from 4 to 5
move 4 from 2 to 4
move 2 from 8 to 3
move 3 from 3 to 2
move 4 from 1 to 2
move 2 from 4 to 7
move 4 from 2 to 3
move 4 from 1 to 2
move 13 from 5 to 1
move 1 from 6 to 2
move 1 from 1 to 8
move 15 from 5 to 2
move 4 from 3 to 1
move 5 from 4 to 3
move 1 from 3 to 6
move 1 from 8 to 7
move 1 from 9 to 8
move 1 from 7 to 8
move 3 from 3 to 2
move 1 from 8 to 2
move 1 from 3 to 7
move 13 from 1 to 4
move 3 from 5 to 3
move 1 from 1 to 2
move 1 from 8 to 5
move 5 from 7 to 2
move 1 from 6 to 5
move 2 from 3 to 4
move 10 from 2 to 5
move 1 from 9 to 5
move 3 from 1 to 8
move 3 from 8 to 3
move 11 from 4 to 5
move 12 from 2 to 8
move 4 from 4 to 7
move 10 from 8 to 5
move 2 from 8 to 1
move 1 from 7 to 3
move 1 from 7 to 9
move 5 from 3 to 7
move 1 from 9 to 4
move 7 from 7 to 6
move 13 from 5 to 8
move 6 from 6 to 7
move 5 from 7 to 4
move 1 from 6 to 4
move 2 from 4 to 9
move 1 from 7 to 9
move 3 from 4 to 3
move 1 from 3 to 6
move 4 from 5 to 7
"""

def move(crates,from_line, to_line):
    value = crates[from_line-1].pop()
    crates[to_line-1].append(value)
    return crates

def move_9001(crates,from_line, to_line, number):
    value = crates[from_line-1][-number:]
    for x in range(number):
        crates[from_line-1].pop()
    crates[to_line-1].extend(value)
    return crates

def get_last_char(list):
    if not list:
        return list
    return list[len(list)-1][1:-1]

def chal1():
    split_crates = True
    crate_started = False
    crates = []
    for line in input.splitlines():
        if "1" in line:
            x = line.split()
            crates = [[] for i in range(len(line.split()))]
            break
    for line in input.splitlines():
        if line != "":
            if "1" in line and "move" not in line:
                for index, x in enumerate(crates):
                    crates[index].reverse()
            elif split_crates and "1" not in line and "move" not in line:
                for index, x in  enumerate([line[i:i+4] for i in range(0, len(line), 4)]):
                    #print(crates[0])
                    x = x.rstrip()
                    if x != "":
                        crates[index].append(x)
                        crate_started=True
            elif "move" in line:
                move_split = line.split(" from ")
                repeat = move_split[0][5:]
                from_line = move_split[1].split(" to ")[0]
                to_line =  move_split[1].split(" to ")[1]
                for x in range(int(repeat)):
                    move(crates,int(from_line), int(to_line))
    string = ""
    for crate in crates:
        string += get_last_char(crate)

    print(string)


def chal2():
    split_crates = True
    crate_started = False
    crates = []
    for line in input.splitlines():
        if "1" in line:
            x = line.split()
            crates = [[] for i in range(len(line.split()))]
            break
    for line in input.splitlines():
        if line != "":
            if "1" in line and "move" not in line:
                for index, x in enumerate(crates):
                    crates[index].reverse()
            elif split_crates and "1" not in line and "move" not in line:
                for index, x in  enumerate([line[i:i+4] for i in range(0, len(line), 4)]):
                    #print(crates[0])
                    x = x.rstrip()
                    if x != "":
                        crates[index].append(x)
                        crate_started=True
            elif "move" in line:
                move_split = line.split(" from ")
                repeat = move_split[0][5:]
                from_line = move_split[1].split(" to ")[0]
                to_line =  move_split[1].split(" to ")[1]

                move_9001(crates,int(from_line), int(to_line),int(repeat))
    string = ""
    for crate in crates:
        string += get_last_char(crate)

    print(string)



chal1()
chal2()