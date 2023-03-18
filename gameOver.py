from pickle import FALSE
import TicTacToe


def check_line(game_Table, line_Num):
    for i in range(1, TicTacToe.TABLE_SIZE):
        if game_Table[line_Num][i] == '' or game_Table[line_Num][i-1] != game_Table[line_Num][i]:
            return False
    return True

def check_column(game_Table, column_Num):
    for i in range(1, TicTacToe.TABLE_SIZE):
        if game_Table[i][column_Num] == '' or game_Table[i-1][column_Num] != game_Table[i][column_Num]:
            return False
    return True


def check_diagonal(game_Table):
    if game_Table[1][1] == '':
        return False
    if game_Table[0][0] == game_Table[1][1] and game_Table[1][1] == game_Table[2][2]:
        return True
    elif game_Table[1][1] == game_Table[0][2] and game_Table[1][1] == game_Table[2][0]:
        return True
    
    return False


def is_table_full(game_Table):
    for i in range(0, TicTacToe.TABLE_SIZE):
        for j in range(0, TicTacToe.TABLE_SIZE):
            if game_Table[i][j] == '':
                return FALSE
    return True


def is_game_over(game_Table, line_Num, column_Num):
    if check_line(game_Table, line_Num): return game_Table[line_Num][0]
    elif check_column(game_Table, column_Num): return game_Table[0][column_Num]
    elif check_diagonal(game_Table): return game_Table[1][1]
    elif is_table_full(game_Table) == True: return "Draw"
    else: return False