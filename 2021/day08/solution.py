def part1(data):
    input = data.splitlines()
    input = [i.split(" | ") for i in input]
    numbers = 0
    for row in input:
        digits = row[1].split(" ")
        for digit in digits:
            if len(digit) == 2 or len(digit) == 4 or len(digit) == 3 or len(digit) == 7:
                numbers += 1

    return numbers

def part2(data):
    input = data.splitlines()
    input = [i.split(" | ") for i in input]
    segments = [" "] * 10
    outputs = []

    for row in input:
        entry = row[0].split(" ")
        output = row[1].split(" ")
        temp = ""
        entry.sort(key=len)

        segments[1] = entry[0]
        segments[7] = entry[1]
        segments[4] = entry[2]
        segments[8] = entry[9]


        for i in range(3,6):
            if contains(segments[1], entry[i]):
                segments[3] = entry[i]

        for i in range(3,6):
            if matching_segments(entry[i], segments[4], 3) and entry[i] != segments[3]:
                segments[5] = entry[i]

        for i in range(3,6):
            if entry[i] != segments[5] and entry[i] != segments[3]:
                segments[2] = entry[i]

        for i in range(6,9):
            if not contains(segments[5], entry[i]):
                segments[0] = entry[i]

            if contains(segments[3], entry[i]):
                segments[9] = entry[i]

        for i in range(6,9):
            if entry[i] != segments[0] and entry[i] != segments[9]:
                segments[6] = entry[i]

        for number in output:
            for i in range(0, len(segments)):
                if len(number) == len(segments[i]):
                    if contains(number, segments[i]):
                        temp += str(i)

        outputs.append(int(temp))

    return sum(outputs)

def contains(str, str2):
    for letter in str:
        if letter not in str2:
            return False
    return True

def matching_segments(str, str2, number_of_segments):
    matching = 0
    for letter in str:
        if letter in str2:
            matching +=1
    return matching == number_of_segments