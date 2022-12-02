def part1(data):
    input = data.splitlines()
    total_points = 0
    for match in input: 
        match = match.split()
        total_points += calc_points(match)
    
    return total_points

def part2(data):
    input = data.splitlines()
    total_points = 0
    for match in input:
        match = match.split()
        player_input = calc_shape(match)
        actual_input = [match[0], player_input]
        total_points += calc_points(actual_input)

    return total_points

def calc_points(input):
    points = {'X': 1, 'Y': 2, 'Z': 3, 'A': 1, 'B': 2, 'C': 3, }

    if (input[0] == 'A' and input[1] == 'X') or (input[0] == 'B' and input[1] == 'Y') or (input[0] == 'C' and input[1] == 'Z') or input[0] == input[1]:
        return 3 + points[input[1]]
    elif input[0] == 'A':
        if input[1] == 'Y':
            return 6 + points[input[1]]
        else:
            return 0 + points[input[1]]
    elif input[0] == 'B':
        if input[1] == 'Z':
            return 6 + points[input[1]]
        else:
            return 0 + points[input[1]]
    elif input[0] == 'C':
        if input[1] == 'X':
            return 6 + points[input[1]]
        else:
            return 0 + points[input[1]]

def calc_shape(input):
    lose = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    win = {'A': 'Y', 'B': 'Z', 'C': 'X'}
    
    if (input[1] == 'Y'):
        return input[0]
    elif(input[1] == 'X'):
        return lose[input[0]]
    elif(input[1] == 'Z'):
        return win[input[0]]