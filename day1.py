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
    elvessorted = sorted(elves, reverse=True)
    top3elves = elvessorted[0]+elvessorted[1]+elvessorted[2]
    return elvessorted[0], top3elves
    
top1, top3 = findelf("day1/input.txt")
print("Total calories first elf is carrying: " + str(top1))
print("Total calories top3 elves are carrying: " + str(top3))