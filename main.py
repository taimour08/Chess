import threat
import movement
import attack
import random as rnd

board = [['r', 'k', 'b', 'q', 'g', 'b', 'k', 'r'],
         ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
         ['R', 'K', 'B', 'Q', 'G', 'B', 'K', 'R']
         ]


# threat.checkThreat(board, 3, 2)

# movement.pawnMovement(board, 6, 0)


def game():
    # global current

    b = False

    for y in range(0, 8):

        for x in range(0, 8):

            if 'Z' >= board[x][y] >= 'A':  # To find own piece which is capital letter
                print(board[x][y])
                current = threat.Cell(board[x][y], x, y)

                if threat.checkThreat(board, x, y):  # Check whether there a threat from opponent's piece

                    print(x, y, "At Threat")  # if the current piece is at threat, come out of both the loops

                    movement.movePiece(board, x, y)

                    b = True
                    break

        if b:
            break

    if not b:  # If no threat detected

        rnd.seed()
        y = rnd.randint(0, 7)

        for x in range(0, 8):

            if rnd.randint(0, 40) % 2 == 0:
                if 'Z' >= board[x][y] >= 'A':  # To find own piece which is capital letter
                    movement.movePiece(board, x, y)


            else:
                if board[x][y] == 'Q':  # To find own piece which is capital letter
                    movement.movePiece(board, x, y)

                # add movement and change turn

    for c in range(0, 8):
        print(board[c])


for i in range(0, 8):
    print(board[i])

game()
# movement.movePiece(board, 6, 0)
