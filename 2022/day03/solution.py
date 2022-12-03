def part1(data):
    input = data.splitlines()
    total_points = 0

    for line in input:
        total_points += ord(list(set(line[:int(len(line) / 2)]).intersection(set(line[int(len(line) / 2):])))[0]) - 96 if list(set(line[:int(len(line) / 2)]).intersection(set(line[int(len(line) / 2):])))[0].islower() else ord(list(set(line[:int(len(line) / 2)]).intersection(set(line[int(len(line) / 2):])))[0]) - 38
    
    return total_points
    
def part2(data):
    input = data.splitlines()
    total_points = 0
    
    for x in range(3, len(input) + 1, 3):
        total_points += ord(list(set.intersection(set(input[x-3]), set(input[x-2]), set(input[x-1])))[0]) - 96 if list(set.intersection(set(input[x-3]), set(input[x-2]), set(input[x-1])))[0].islower() else ord(list(set.intersection(set(input[x-3]), set(input[x-2]), set(input[x-1])))[0]) - 38
    
    return total_points