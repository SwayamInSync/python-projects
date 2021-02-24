from game_board import game_board
from check_winner import check_winner

moves = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
print("Player 1: X\nPlayer 2: O\n")

game_board(moves)

is_game_over = False

game_on = 0


def place_move(player, move):
    row = int(move / 3)
    if player == 1:
        symbol = "X"
    else:
        symbol = "O"
    if 0 <= row < 1:
        moves[row][move] = symbol
    elif 1 <= row < 2:
        moves[row][move - 3] = symbol
    elif 2 <= row < 3:
        moves[row][move - 6] = symbol


while not is_game_over:
    game_on += 1
    if game_on % 2 != 0:
        player_one_move = int(input("player one: "))
        place_move(1, player_one_move - 1)
        game_board(moves)
    else:
        player_two_move = int(input("player two: "))
        place_move(2, player_two_move - 1)
        game_board(moves)

    if check_winner(moves):
        print("Game Over")
        # print(f"{check_winner()} wins")
        is_game_over = True
