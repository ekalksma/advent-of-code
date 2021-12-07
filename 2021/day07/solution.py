def part1(data):
    input = data.split(',')
    input = list(map(int, input))

    print(get_least(input, 1))

def part1(data):
    input = data.split(',')
    input = list(map(int, input))

    print(get_least(input, 2))


def get_least(positions, part):
    least_fuel = 9999999999999
    start = min(positions)
    end = max(positions)

    for i in range(start, end):
        fuel = 0
        fuel = calc_fuel(positions, i, part)

        if fuel < least_fuel:
            least_fuel = fuel

    return least_fuel

def calc_fuel(positions, target, part):
    fuel = 0
    if part == 1:
        for i in range(0, len(positions)):
            fuel += abs(positions[i] - target)

    if part == 2:
        for i in range(0, len(positions)):
            steps = abs(positions[i] - target)
            for j in range(1, steps + 1):
                fuel += j

    return fuel