def part1(data):
    input = data.splitlines()
    visible_trees = 0
    for i in range(0, len(input)):
        for h in range(0, len(input[i])):
            if check_top(input,input[i][h],i,h) or check_bot(input,input[i][h],i,h) or check_left(input,input[i][h],i,h) or check_right(input,input[i][h],i,h):
                visible_trees += 1

    return visible_trees
    
def part2(data):
    input = data.splitlines()
    highest_scenic_score = 0
    for i in range(0, len(input)):
        for h in range(0, len(input[i])):
            scenic_score = view_top(input,input[i][h],i,h) * view_bot(input,input[i][h],i,h) * view_left(input,input[i][h],i,h) * view_right(input,input[i][h],i,h)
            if scenic_score > highest_scenic_score:
                highest_scenic_score = scenic_score

    return highest_scenic_score

def check_bot(trees, tree_height, y, x):
    if y == 0 or x == 0 or y == len(trees) - 1 or x == len(trees[0]) - 1:
        return True
    if tree_height > trees[y + 1][x]:
        return check_bot(trees, tree_height, y + 1, x)
    else:
        return False

def check_top(trees, tree_height, y, x):
    if y == 0 or x == 0 or y == len(trees) - 1 or x == len(trees[0]) - 1:
        return True
    if tree_height > trees[y - 1][x]:
        return check_top(trees, tree_height, y - 1, x)
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

def view_bot(trees, tree_height, y, x):
    if y == 0 or x == 0 or y == len(trees) - 1 or x == len(trees[0]) - 1:
        return 0
    if tree_height == trees[y + 1][x]:
        return 1
    if tree_height >= trees[y + 1][x]:
        return 1 + view_bot(trees, tree_height, y + 1, x)
    else:
        return 1

def view_top(trees, tree_height, y, x):
    if y == 0 or x == 0 or y == len(trees) - 1 or x == len(trees[0]) - 1:
        return 0
    if tree_height == trees[y - 1][x]:
        return 1
    if tree_height >= trees[y - 1][x]:
        return 1 + view_top(trees, tree_height, y - 1, x)
    else:
        return 1

def view_right(trees, tree_height, y, x):
    if y == 0 or x == 0 or y == len(trees) - 1 or x == len(trees[0]) - 1:
        return 0
    if tree_height == trees[y][x + 1]:
        return 1
    if tree_height >= trees[y][x + 1]:
        return 1 + view_right(trees, tree_height, y, x + 1)
    else:
        return 1

def view_left(trees, tree_height, y, x):
    if y == 0 or x == 0 or y == len(trees) - 1 or x == len(trees[0]) - 1:
        return 0
    if tree_height == trees[y][x - 1]:
        return 1
    if tree_height >= trees[y][x - 1]:
        return 1 + view_left(trees, tree_height, y, x - 1)
    else:
        return 1