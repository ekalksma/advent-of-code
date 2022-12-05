import re

def part1(data):
    input = data.splitlines()
    del input[:10]
    stacks = (['S', 'Z', 'P', 'D', 'L', 'B', 'F', 'C'], ['N', 'V', 'G', 'P', 'H', 'W', 'B'], ['F', 'W', 'B', 'J', 'G'], 
    ['G', 'J', 'N', 'F', 'L','W', 'C', 'S'], ['W', 'J', 'L', 'T', 'P', 'M', 'S','H'], ['B', 'C', 'W', 'G', 'F', 'S'], 
    ['H', 'T', 'P', 'M', 'Q', 'B', 'W'], ['F', 'S', 'W', 'T'], ['N', 'C', 'R'])

    message = []
   
    for line in input:
        moves = re.findall(r'\d+', line)
        moves = [int(x) for x in moves]
        for i in range(moves[0]):
            stacks[moves[2]-1].append(stacks[moves[1]-1].pop())
    
    for stack in stacks:
        message.append(stack.pop())
    
    return message
    
def part2(data):
    input = data.splitlines()
    del input[:10]
    stacks = (['S', 'Z', 'P', 'D', 'L', 'B', 'F', 'C'], ['N', 'V', 'G', 'P', 'H', 'W', 'B'], ['F', 'W', 'B', 'J', 'G'], 
    ['G', 'J', 'N', 'F', 'L','W', 'C', 'S'], ['W', 'J', 'L', 'T', 'P', 'M', 'S','H'], ['B', 'C', 'W', 'G', 'F', 'S'], 
    ['H', 'T', 'P', 'M', 'Q', 'B', 'W'], ['F', 'S', 'W', 'T'], ['N', 'C', 'R'])

    message = []
   
    for line in input:
        moves = re.findall(r'\d+', line)
        moves = [int(x) for x in moves]
        temp = []
        for i in range(moves[0]):
            temp.append(stacks[moves[1]-1].pop())

        for x in reversed(temp):
                stacks[moves[2]-1].append(x)


    
    for stack in stacks:
        message.append(stack.pop())
    
    return message
