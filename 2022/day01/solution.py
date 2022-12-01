def part1(data):
    input = parse_input(data)
    
    return input.pop()

def part2(data):
    input = parse_input(data)

    return input[len(input) - 1] + input[len(input) - 2] + input[len(input) - 3]

def calc_calories(calories):
    calories = calories.split('\n')
    calories = [int(x) for x in calories]

    return sum(calories)

def parse_input(data):
    input = data.strip()
    input = input.split('\n\n')
    input = map(calc_calories, input)
    input = list(input)
    input.sort()
    
    return input
