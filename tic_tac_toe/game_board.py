def game_board(moves):
    for row in moves:
        for move in row:
            print(f"| {move} |", end="   ")
        print("\n")