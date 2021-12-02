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
