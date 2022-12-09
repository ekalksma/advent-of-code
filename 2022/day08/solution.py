def part1(data):
    input = data.splitlines()
    visible_trees = 0
    for i in range(0, len(input)):
        for h in range(0, len(input[i])):
            if check_top(input,input[i][h],i,h) or check_bot(input,input[i][h],i,h) or check_left(input,input[i][h],i,h) or check_right(input,input[i][h],i,h):
                visible_trees += 1

    return visible_trees
    
# def part2(data):
#     input = data
#     for i in range(14, len(input)+1):
#         sub = input[i-14:i]
#         if len(set(sub)) == len(sub):
#             return i

def check_top(trees, tree_height, y, x):
    if y == 0 or x == 0 or y == len(trees) - 1 or x == len(trees[0]) - 1:
        return True
    if tree_height > trees[y + 1][x]:
        return check_top(trees, tree_height, y + 1, x)
    else:
        return False

def check_bot(trees, tree_height, y, x):
    if y == 0 or x == 0 or y == len(trees) - 1 or x == len(trees[0]) - 1:
        return True
    if tree_height > trees[y - 1][x]:
        return check_bot(trees, tree_height, y - 1, x)
    else:
        return False

def check_right(trees, tree_height, y, x):
    if y == 0 or x == 0 or y == len(trees) - 1 or x == len(trees[0]) - 1:
        return True
    if tree_height > trees[y][x + 1]:
        return check_right(trees, tree_height, y, x + 1)
    else:
        return False

def check_left(trees, tree_height, y, x):
    if y == 0 or x == 0 or y == len(trees) - 1 or x == len(trees[0]) - 1:
        return True
    if tree_height > trees[y][x - 1]:
        return check_left(trees, tree_height, y, x - 1)
    else:
        return False