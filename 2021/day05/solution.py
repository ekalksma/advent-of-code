def part1(data):
    input = data.splitlines()
    input = [i.split("->") for i in input]
    size = 999
    board = [ [ 0 for y in range( size ) ]
             for x in range( size ) ]

    for i in range(0, len(input)):
        input[i] = list(map(str.strip, input[i]))

    for element in input:
        start_line = element[0].split(',')
        end_line = element[1].split(',')

        x1 = int(start_line[0])
        x2 = int(end_line[0])

        y1 = int(start_line[1])
        y2 = int(end_line[1])

        if y1 == y2:
            if (x1 - x2) < 0:
                for x in range(x1, x2 + 1):
                    if board[y1][x] < 2:
                        board[y1][x] += 1
            elif (x1 - x2) > 0:
                for x in range(x1, x2 - 1, -1):
                    if board[y1][x] < 2:
                        board[y1][x] += 1

        if x1 == x2:
            if (y1 - y2) < 0:
                for y in range(y1, y2 + 1):
                    if board[y][x1] < 2:
                        board[y][x1] += 1
            elif (y1 - y2) > 0:
                for y in range(y1, y2 - 1, -1):
                    if board[y][x1] < 2:
                        board[y][x1] += 1

    return count_twos(board)


def print_board(board):
    for line in board:
        print(line)


def count_twos(board):
    counter = 0

    for row in board:
        for num in row:
            if num == 2:
                counter += 1

    return counter