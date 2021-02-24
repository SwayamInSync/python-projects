def check_winner(moves):

    if moves[0][0] == moves[0][1] == moves[0][2] != " " or moves[1][0] == moves[1][1] == moves[1][2] != " " or moves[2][0] == moves[2][1] == moves[2][2] != " ":
        print("row")
        got_winner = True
        return got_winner

    elif moves[0][0] == moves[1][0] == moves[2][0] != " " or moves[0][1] == moves[1][1] == moves[2][1] != " " or moves[0][2] == moves[1][2] == moves[2][2] != " ":
        print("col")
        got_winner = True
        return got_winner

    elif moves[0][0] == moves[1][1] == moves[2][2] != " ":
        print("diagonal 1")
        got_winner = True
        return got_winner
    elif moves[0][2] == moves[1][1] == moves[2][0] != " ":
        print("diagonal 2")
        got_winner = True
        return got_winner

    return False

