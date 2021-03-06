from random import randint

board = []

for x in range(11):
    board.append(["O"] * 11)


def print_board(board):
    for row in board:
        print(" ".join(row))


print("Let's play Battleship!")
print_board(board)


def random_row(board):
    return (randint(0, len(board) - 1))


def random_col(board):
    return (randint(0, len(board[0]) - 1))


ship_row = random_row(board)
ship_col = random_col(board)
shipA_row = random_row(board)
shipA_col = random_col(board)
shipB_row = random_row(board)
shipB_col = random_row(board)

for turn in range(10):
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 10) or (guess_col < 0 or
                                                 guess_col > 10):
            print("Oops, that's not even in the ocean.")
        elif (board[guess_row][guess_col] == "X"):
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"

            turn = turn + 1
            print("Turn", turn + 1)

        print_board(board)

    if turn > 9:
        print("Game Over")
print('Ship 1 Row:', ship_row)
print('Ship 1 Col:', ship_col)
print('Ship 2 Row:', shipA_row)
print('Ship 2 Col:', shipA_col)
print('Ship 3 Row:', shipB_row)
print('Ship 3 Col:', shipB_col)
