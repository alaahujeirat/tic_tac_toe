import TicTacToe

def bot_winning_move(game_Table, bot_Letter):
    for i in range(0, TicTacToe.TABLE_SIZE):
        if game_Table[i][0] == bot_Letter and game_Table[i][1] == bot_Letter:
            if game_Table[i][2] == '':
                return i, 2
        elif game_Table[i][1] == bot_Letter and game_Table[i][2] == bot_Letter:
            if game_Table[i][0] == '':
                return i, 0
        elif game_Table[i][0] == bot_Letter and game_Table[i][2] == bot_Letter:
            if game_Table[i][1] == '':
                return i, 1
    
    for i in range(0, TicTacToe.TABLE_SIZE):
        if game_Table[0][i] == bot_Letter and game_Table[1][i] == bot_Letter:
            if game_Table[2][i] == '':
                return 2, i
        elif game_Table[1][i] == bot_Letter and game_Table[2][i] == bot_Letter:
            if game_Table[0][i] == '':
                return 0, i
        elif game_Table[0][i] == bot_Letter and game_Table[2][i] == bot_Letter:
            if game_Table[1][i] == '':
                return 1, i

    return -1, -1


def block_player(game_Table, player_Letter):
    for i in range(0, TicTacToe.TABLE_SIZE):
        if game_Table[i][0] == player_Letter and game_Table[i][1] == player_Letter:
            if game_Table[i][2] == '':
                return i, 2
        elif game_Table[i][1] == player_Letter and game_Table[i][2] == player_Letter:
            if game_Table[i][0] == '':
                return i, 0
        elif game_Table[i][0] == player_Letter and game_Table[i][2] == player_Letter:
            if game_Table[i][1] == '':
                return i, 1
    
    for i in range(0, TicTacToe.TABLE_SIZE):
        if game_Table[0][i] == player_Letter and game_Table[1][i] == player_Letter:
            if game_Table[2][i] == '':
                return 2, i
        elif game_Table[1][i] == player_Letter and game_Table[2][i] == player_Letter:
            if game_Table[0][i] == '':
                return 0, i
        elif game_Table[0][i] == player_Letter and game_Table[2][i] == player_Letter:
            if game_Table[1][i] == '':
                return 1, i

    if game_Table[0][0] == player_Letter and game_Table[1][1] == player_Letter:
        if game_Table[2][2] == '':
                return 2, 2
    if game_Table[0][0] == player_Letter and game_Table[2][2] == player_Letter:
        if game_Table[1][1] == '':
                return 1, 1
    if game_Table[1][1] == player_Letter and game_Table[2][2] == player_Letter:
        if game_Table[0][0] == '':
                return 0, 0

    if game_Table[0][2] == player_Letter and game_Table[1][1] == player_Letter:
        if game_Table[2][0] == '':
                return 2, 0
    if game_Table[1][1] == player_Letter and game_Table[2][0] == player_Letter:
        if game_Table[0][2] == '':
                return 0, 2
    if game_Table[0][2] == player_Letter and game_Table[2][0] == player_Letter:
        if game_Table[1][1] == '':
                return 1, 1

    return -1, -1


def check_center(game_Table):
    i = TicTacToe.TABLE_SIZE//2
    if game_Table[i][i] == '':
        return i, i
    else:
        return -1, -1


def check_corners(game_Table, bot_Letter, player_Letter):
    i = 0
    j = TicTacToe.TABLE_SIZE - 1
    if game_Table[i][i] == '' and game_Table[j][j] != player_Letter:
        return i, i
    elif game_Table[j][j] == '' and game_Table[i][i] != player_Letter:
        return j, j
    elif game_Table[j][i] == '' and game_Table[i][j] != player_Letter:
        return j, i
    elif game_Table[i][j] == '' and game_Table[j][i] != player_Letter:
        return i, j
    else:
        return -1, -1


def default_move(game_Table):
    for i in range(0, TicTacToe.TABLE_SIZE):
        for j in range(0, TicTacToe.TABLE_SIZE):
            if game_Table[i][j] == '':
                return i, j
    return -1, -1


def bot_stategy(game_Table, bot_Letter, player_Letter):
    #check winning move
    l, c = bot_winning_move(game_Table, bot_Letter)
    if  (l != -1 and c != -1):
        return l, c

    #prevent player win
    l, c = block_player(game_Table, player_Letter)
    if  (l != -1 and c != -1):
        return l, c
    
    #take center if empty
    l, c = check_center(game_Table)
    if  (l != -1 and c != -1):
        return l, c
    
    #take one of the corners, if empty
    l, c = check_corners(game_Table, bot_Letter, player_Letter)
    if  (l != -1 and c != -1):
        return l, c
    
    #if strategy doesn't work, take the first empty place
    return default_move(game_Table)
    