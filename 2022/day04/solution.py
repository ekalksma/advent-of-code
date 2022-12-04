def part1(data):
    input = data.splitlines()
    num_pairs = 0
    for line in input:
        pairs = line.split(",")
        pair_one = pairs[0].split("-")
        pair_two = pairs[1].split("-")
        
        if (int(pair_one[0]) >= int(pair_two[0]) and int(pair_one[1]) <= int(pair_two[1])) or (int(pair_two[0]) >= int(pair_one[0]) and int(pair_two[1]) <= int(pair_one[1])):
            num_pairs += 1

    return num_pairs
    
def part2(data):
    input = data.splitlines()
    num_pairs = 0
    for line in input:
        pairs = line.split(",")
        pair_one = pairs[0].split("-")
        pair_two = pairs[1].split("-")
        
        if ((int(pair_one[0]) >= int(pair_two[0]) and int(pair_one[0]) <= int(pair_two[1])) or
         (int(pair_one[1]) >= int(pair_two[0]) and int(pair_one[0]) <= int(pair_two[1])) or 
         (int(pair_two[0]) >= int(pair_one[0]) and int(pair_two[0]) <= int(pair_one[1])) or 
         (int(pair_two[1]) >= int(pair_one[0]) and int(pair_two[0]) <= int(pair_one[1]))):
            num_pairs += 1

    return num_pairs