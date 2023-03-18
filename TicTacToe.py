import gameOver
import table
import strategy
TABLE_SIZE = 3


def assign_players():
    while True:
        player_letter = (input("Are you the X or the O? ")).upper()
        if player_letter == 'X' or player_letter == 'O':
            break
        print("Wrong input. Try again.")
    
    if player_letter == 'X':
        bot_letter = 'O'
    else:
        bot_letter = 'X'
    return player_letter, bot_letter


def player_move(game_Table):
    while True:
        line_num = int(input("Choose a line: ")) -1
        column_num = int(input("Choose a column: ")) -1
        if line_num < 0 or line_num > 2 or column_num < 0 or column_num > 2:
            print("Wrong indexes. Try again")
            continue

        elif game_Table[line_num][column_num] != '':
            print("Square is taken. Try again")
            continue

        else:
            break

    return line_num, column_num


def bot_move(game_Table, bot_letter, player_Letter):
        i, j = strategy.bot_stategy(game_Table, bot_letter, player_Letter)
        return i, j


def fill_square(game_Table, line_Num, column_Num, player_Letter):
    game_Table[line_Num][column_Num] = player_Letter
    table.print_table(game_Table)
    return game_Table


def declare_result(status):
    if status == 'X' or status == 'O':
        print("GAME OVER.\nWinner is:", status)
    elif status == 'Draw':
        print("GAME OVER.\nResult:", status)
    else:
        print("GAME OVER.")



if __name__ == "__main__":
    
    play_again = ''
    while True:
        #create game table
        game_table = [['']*TABLE_SIZE, ['']*TABLE_SIZE, ['']*TABLE_SIZE]
        print("\nLet's play Tic-Tac-Toe!")
        player_letter, bot_letter = assign_players()
        table.print_table(game_table)

        status = False
        while status == False:
            #player turn
            line_num, column_num = player_move(game_table)
            game_table = fill_square(game_table, line_num, column_num, player_letter)
            status = gameOver.is_game_over(game_table, line_num, column_num)
            if status != False:
                break
            
            #bot turn
            line_num, column_num = bot_move(game_table, bot_letter, player_letter)
            if line_num != -1 and column_num != -1:
                game_table = fill_square(game_table, line_num, column_num, bot_letter)
            status = gameOver.is_game_over(game_table, line_num, column_num)
        
        declare_result(status)
        play_again = input("Would you like to play again? y/n: ")
        if play_again == 'n':
            break

