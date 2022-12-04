def part1(data):
    input = data.splitlines()
    num_pairs = 0
    for line in input:
        pairs = line.replace(",","-").split("-")
        
        if (int(pairs[0]) >= int(pairs[2]) and int(pairs[1]) <= int(pairs[3])) or (int(pairs[2]) >= int(pairs[0]) and int(pairs[3]) <= int(pairs[1])):
            num_pairs += 1

    return num_pairs
    
def part2(data):
    input = data.splitlines()
    num_pairs = 0
    for line in input:
        pairs = line.replace(",","-").split("-")

        if int(pairs[2]) <= int(pairs[1]) and int(pairs[3]) >= int(pairs[0]):
            num_pairs += 1

    return num_pairs