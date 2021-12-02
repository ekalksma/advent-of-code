def part1(data):
    input = data.splitlines()
    depth = 0
    hpos = 0
    
    for direction in input:
        units = int(direction[(len(direction)-1)])

        if "forward" in direction:
            hpos += units
        elif "down" in direction:
            depth += units
        elif "up" in direction:
            depth -= units

    return hpos * depth


def part2(data):
    input = data.splitlines()
    depth = 0
    hpos = 0
    aim = 0
    
    for direction in input:
        units = int(direction[(len(direction)-1)])

        if "forward" in direction:
            hpos += units
            depth += (aim * units)
        elif "down" in direction:
            aim += units
        elif "up" in direction:
            aim -= units

    return hpos * depth
