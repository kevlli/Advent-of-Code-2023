def part1():
    file = open("input.txt", "r")
    lines = file.readlines()
    symbols = ["@", "#", "$", "%", "&", "*", "-", "+", "/", "="]
    indices = []
    moves = [-1, 0, 1]
    sum = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] in symbols:
                for horizontal in moves:
                    for vertical in moves:
                        if horizontal or vertical: # excludes 0,0
                            indices.append((i+horizontal, j+vertical))
    # this double for loop finds all the indices we have to check for valid numbers
    alreadyDone = []
    for index in indices:
        i = index[0]
        j = index[1]
        if lines[i][j].isnumeric() and index not in alreadyDone:
            start = j
            end = j
            while end < len(lines[i]) and lines[i][end].isnumeric():
                alreadyDone.append((i,end))
                end += 1
            while start > -1 and lines[i][start].isnumeric():
                alreadyDone.append((i,start))
                start -= 1
            # these two while loops move pointers left and right to find the entire number. 
            # It also adds indices it has searched to a list, to prevent duplicate entries
            sum += int(lines[i][start + 1: end])
    print(sum)

def part2():
    file = open("input.txt", "r")
    lines = file.readlines()
    symbols = ["@", "#", "$", "%", "&", "*", "-", "+", "/", "="]
    indices = []
    moves = [-1, 0, 1]
    sum = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] in symbols:
                checked = []
                nums = []
                for horizontal in moves:
                    for vertical in moves:
                        if horizontal or vertical:
                            if lines[i + horizontal][j + vertical].isnumeric() and (i + horizontal,j + vertical) not in checked:
                                start = j + vertical
                                end = j + vertical
                                while end < len(lines[i + horizontal]) and lines[i + horizontal][end].isnumeric():
                                    checked.append((i + horizontal,end))
                                    end += 1
                                while start > -1 and lines[i + horizontal][start].isnumeric():
                                    checked.append((i + horizontal,start))
                                    start -= 1
                                nums.append(int(lines[i + horizontal][start + 1: end]))
                if len(nums) == 2:
                    sum += nums[0] * nums[1]
    print(sum)
part2()