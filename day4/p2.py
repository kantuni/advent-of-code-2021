from sys import stdin

numbers = list(map(int, input().split(",")))

lines = []
for line in stdin:
    if line.strip():
        lines.append(line.strip())

raw_boards = [lines[i : i + 5] for i in range(0, len(lines), 5)]

boards = []
for raw_board in raw_boards:
    board = []
    for raw_row in raw_board:
        row = [int(x) for x in raw_row.split()]
        board.append(row)

    boards.append(board)


def make_step(number, boards):
    for board in boards:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == number:
                    board[i][j] = "*"

    return boards


def check_for_win(board) -> bool:
    for row in board:
        str_row = "".join([str(x) for x in row])
        if str_row == "*****":
            return True

    # transpose matrix
    transposed_board = [[board[j][i] for j in range(5)] for i in range(5)]

    for row in transposed_board:
        str_row = "".join([str(x) for x in row])
        if str_row == "*****":
            return True

    return False


def calculate_board_sum(board) -> int:
    result = 0
    for row in board:
        result += sum(filter(lambda x: x != "*", row))

    return result


result = 0
already_won = [False] * len(boards)

for number in numbers:
    boards = make_step(number, boards)
    for i, board in enumerate(boards):
        if not already_won[i] and check_for_win(board):
            result = calculate_board_sum(board) * number
            already_won[i] = True

print(result)
