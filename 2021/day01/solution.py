def part1(data):
    input = data.splitlines()
    increased = 0

    for i in range(len(input)):
        if i+1 > (len(input) -1):
            break
        if int(input[i]) < int(input[i+1]):
            increased += 1
    
    return increased


def part2(data):
    input = data.splitlines()
    increased = 0

    for i in range(len(input)):
        if i+3 > (len(input) -1):
            break
        if int(input[i]) < int(input[i+3]):
            increased += 1
    
    return increased
