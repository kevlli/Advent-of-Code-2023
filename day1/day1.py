def extractNum(string):
    left = 0
    right = len(string) - 1
    while (not string[left].isnumeric()):
        left += 1
    while (not string[right].isnumeric()):
        right -= 1
    return int(string[left] + string[right])

def part1():
    sum = 0
    file = open("day1.txt", "r")
    lines = file.readlines()

    for line in lines:
        sum += extractNum(line)
    print(sum)

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def extractNum2(string):
    minIndex = 9999999
    minNum = 0
    maxIndex = -1
    maxNum = 0
    for digit in digits:
        index = string.find(digit)
        if (index != -1 and index < minIndex):
            minIndex = index
            minNum = digits.index(digit) + 1
        index = string.rfind(digit)
        if (index > maxIndex):
            maxIndex = index
            maxNum = digits.index(digit) + 1
    # this loop finds first and last occurrence of string digits, if present
    left = 0
    right = len(string) - 1
    while (not string[left].isnumeric()):
        left += 1
    while (not string[right].isnumeric()):
        right -= 1
    # finds first and last occurrence of numerical digits
    value = 0
    value += (minNum if minIndex < left else int(string[left])) * 10
    value += maxNum if maxIndex > right else int(string[right])
    # compares index values to see if first string digit precedes first numerical digit, and vice versa
    return value

def part2():
    sum = 0
    file = open("day1.txt", "r")
    lines = file.readlines()
    extractNum2(lines[0])
    for line in lines:
        sum += extractNum2(line)
    print(sum)
        
part2()
