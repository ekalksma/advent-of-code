def part1(data):
    input = data.split("\n\n")
    numbers = input[0].split(',')
    cards = input[1:]
    cards = [i.split() for i in cards]

    for number in numbers:
        for card in cards:
            for y in range(0, 5):
                for x in range(0,5):
                    if card[y * 5 + x] == number:
                        card[y * 5 + x] += "m"
                        if check_bingo(card):
                            return get_sum_unmarked(card) * int(number)

def part2(data):
    input = data.split("\n\n")
    numbers = input[0].split(',')
    cards = input[1:]
    cards = [i.split() for i in cards]
    score = 0

    for number in numbers:
        for card in cards:
            if check_bingo(card): continue

            for y in range(0, 5):
                for x in range(0,5):
                    if card[y * 5 + x] == number:
                        card[y * 5 + x] += "m"
                        if check_bingo(card):
                            score = get_sum_unmarked(card) * int(number)
    return score

def check_bingo(card):
    for y in range(0, 5):
        mcounter = 0
        for x in range(0,5):
            if "m" in card[y * 5 + x]:
                mcounter += 1
        if mcounter == 5:
            return True

    for x in range(0, 5):
        mcounter = 0
        for y in range(0,5):
            if "m" in card[y * 5 + x]:
                mcounter += 1
        if mcounter == 5:
            return True

    return False

def get_sum_unmarked(card):
    sum = 0
    for number in card:
        if "m" not in number:
            sum += int(number)
    return sum