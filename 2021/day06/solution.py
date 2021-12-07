def part1(data):
    input = data.split(',')
    input = list(map(int, input))
    days = 80

    for day in range(0,days):
        for i in range (0, len(input)):
            if input[i] == 0:
                input[i] = 6
                input.append(8)

            else:
                input[i] -= 1

    print(len(input))

def part2(data):
    input = data.split(',')
    input = list(map(int, input))
    days = 256
    fish = { 0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0 }

    for num in input:
         fish[num] += 1

    for day in range(0,days):
        for i in range(0,10):
            if i == 0:
                fish[7] += fish[0]
                fish[9] += fish[0]
                fish[0] = 0
            else:
                fish[i-1] += fish[i]
                fish[i] = 0

    return sum(fish.values())
