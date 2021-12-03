def part1(data):
    input = data.splitlines()
    bin_length = len(input[0])
    gamma = ""
    epsilon = ""

    for i in range(0,bin_length):
        if most_common(input, i) == "one":
            gamma += "1"
        else:
            gamma += "0"
    
    epsilon = inverse_bin(gamma)
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    return gamma * epsilon

def part2(data):
    oxy_gen_rating = data.splitlines()
    scrubber_rating = data.splitlines()
    bin_length = len(oxy_gen_rating[0])

    for i in range(0,bin_length):
        if len(oxy_gen_rating) == 1:
            break
        if most_common(oxy_gen_rating, i) == "one":
            for bin in oxy_gen_rating:
                if bin[i] == "0":
                    oxy_gen_rating = [ i for i in oxy_gen_rating if i!=bin ]
        elif most_common(oxy_gen_rating, i) == "zero":
            for bin in oxy_gen_rating:
                if bin[i] == "1":
                    oxy_gen_rating = [ i for i in oxy_gen_rating if i!=bin ]
        elif most_common(oxy_gen_rating, i) == "equal":
            for bin in oxy_gen_rating:
                if bin[i] == "0":
                    oxy_gen_rating = [ i for i in oxy_gen_rating if i!=bin ]

    for i in range(0,bin_length):
        if len(scrubber_rating) == 1:
            break
        if most_common(scrubber_rating, i) == "one":
            for bin in scrubber_rating:
                if bin[i] == "1":
                    scrubber_rating = [ i for i in scrubber_rating if i!=bin ]
        elif most_common(scrubber_rating, i) == "zero":
            for bin in scrubber_rating:
                if bin[i] == "0":
                    scrubber_rating = [ i for i in scrubber_rating if i!=bin ]
        elif most_common(scrubber_rating, i) == "equal":
            for bin in scrubber_rating:
                if bin[i] == "1":
                    scrubber_rating = [ i for i in scrubber_rating if i!=bin ]
    

    return int(str(scrubber_rating[0]), 2) * int(str(oxy_gen_rating[0]), 2)

def most_common(input, i):
    ones = 0
    input_length = len(input)

    for bin in input:
        if str(bin[i]) == "1":
            ones += 1 

    zeros = input_length - ones    
    
    if ones > zeros:
        return "one"
    if ones < zeros:
        return "zero"
    if ones == zeros:
        return "equal"

def inverse_bin(bin):
    inverse_s = ""

    for bit in bin:

        if bit == "0":
            inverse_s += "1"

        elif bit == "1":
            inverse_s += "0"

    return inverse_s