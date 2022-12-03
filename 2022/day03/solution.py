def part1(data):
    input = data.splitlines()
    total_points = 0

    for line in input:
        first_half = set(line[:int(len(line) / 2)])
        second_half = set(line[int(len(line) / 2):])
        common = first_half.intersection(second_half)
        total_points += getPoints(list(common)[0])
    
    return total_points
    
def part2(data):
    input = data.splitlines()
    total_points = 0
    
    for x in range(3, len(input) + 1, 3):
        first = set(input[x-3])
        second = set(input[x-2])
        third = set(input[x-1])

        common = set.intersection(first, second, third)

        total_points += getPoints(list(common)[0])
    
    return total_points

def getPoints(character):
    if character.islower():
        return ord(character) - 96
    else:
        return ord(character) - 38

