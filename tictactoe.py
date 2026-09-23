import math

board = [" "] * 9

def print_board():
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("--+---+--")

def winner():
    lines = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a,b,c in lines:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None

def minimax(is_max):
    w = winner()
    if w == "O": return 10
    if w == "X": return -10
    if " " not in board: return 0

    scores = []
    for i in range(9):
        if board[i] == " ":
            board[i] = "O" if is_max else "X"
            scores.append(minimax(not is_max))
            board[i] = " "

    return max(scores) if is_max else min(scores)

def computer_move():
    best_score = -math.inf
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score, move = score, i

    board[move] = "O"

while True:
    print_board()
    move = int(input("Your move (1-9): ")) - 1

    if board[move] != " ":
        print("Invalid move!")
        continue

    board[move] = "X"

    if winner() or " " not in board:
        break

    computer_move()

    
    if winner() or " " not in board:
        break

print_board()
print("Winner:", winner() or "Draw!")
