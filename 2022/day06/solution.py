def part1(data):
    input = data
    for i in range(4, len(input)+1):
        sub = input[i-4:i]
        if len(set(sub)) == len(sub):
            return i

    
def part2(data):
    input = data
    for i in range(14, len(input)+1):
        sub = input[i-14:i]
        if len(set(sub)) == len(sub):
            return i
