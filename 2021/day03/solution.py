def part1(data):
    input = data.splitlines()
    input_length = len(input)
    bin_length = len(input[0])
    gamma = ""
    epsilon = ""
    ones = 0
    zeros = 0

    for i in range(0,bin_length):
        for bin in input:
            if str(bin[i]) == "1":
                ones += 1 

        zeros = input_length - ones

        if ones > zeros:
            gamma += "1"
        else:
            gamma += "0"
        ones = 0
    
    epsilon = inverse_bin(gamma)
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    return gamma * epsilon

def inverse_bin(bin):
    inverse_s = ""

    for bit in bin:

        if bit == "0":
            inverse_s += "1"

        elif bit == "1":
            inverse_s += "0"

    return inverse_s