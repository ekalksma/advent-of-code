def part1(data):
    input = list(map(int, data.splitlines()))
    return num_depth_increased(input, 1)


def part2(data):
    input = list(map(int, data.splitlines()))
    return num_depth_increased(input, 3)


def num_depth_increased(input, window_size):
    increased = 0
    window_size = window_size
    input_length = len(input)

    for i in range(input_length):
        if i + window_size > (input_length -1):
            break
        if input[i] < input[i + window_size]:
            increased += 1
    
    return increased
