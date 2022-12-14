def findelf(file):
    f = open(file, "r")
    lines = f.read().splitlines()
    elves = []
    elf = 0
    # print(lines)
    for line in lines:
        if line == "":
            elves.append(elf)
            elf = 0
            # break
        else:
            # print(line)
            elf = elf + int(line)
    print(max(elves))
    
findelf("day1/input.txt")