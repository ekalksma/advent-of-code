def part1(data):
    input = data.splitlines()
    lowest = []

    for y in range(0,len(input)):
        for x in range(0,len(input[0])):
            if x == 0:
                if y == 0:
                    if input[y][x] < input[y][x + 1] and input[y][x] < input[y + 1][x]:
                        lowest.append(input[y][x])
                if y == (len(input) - 1):
                    if input[y][x] < input[y][x + 1] and input[y][x] < input[y - 1][x] :
                        lowest.append(input[y][x])
                else:
                    if input[y][x] < input[y][x + 1] and input[y][x] < input[y - 1][x] and input[y][x] < input[y + 1][x]:
                        lowest.append(input[y][x])
            elif y == 0:
                if x == (len(input[0]) - 1):
                    if input[y][x] < input[y][x-1] and input[y][x] < input[y + 1][x]:
                        lowest.append(input[y][x])
                else:
                    if input[y][x] < input[y][x - 1] and input[y][x] < input[y][x + 1] and input[y][x] < input[y + 1][x]:
                        lowest.append(input[y][x])
            elif y == (len(input) - 1):
                if x == (len(input[0]) - 1):
                    if input[y][x] < input[y][x-1] and input[y][x] < input[y - 1][x]:
                        lowest.append(input[y][x])
                else:
                    if input[y][x] < input[y][x - 1] and input[y][x] < input[y][x + 1] and input[y][x] < input[y - 1][x]:
                        lowest.append(input[y][x])
            elif x == (len(input[0]) - 1):
                    if input[y][x] < input[y][x - 1] and input[y][x] < input[y - 1][x] and input[y][x] < input[y + 1][x]:
                        lowest.append(input[y][x])

            elif input[y][x] < input[y][x + 1] and  input[y][x] < input[y][x - 1] and input[y][x] < input[y + 1][x] and input[y][x] < input[y - 1][x]:
                lowest.append(input[y][x])

    lowest = list(map(int, lowest))

    return sum(lowest) + len(lowest)