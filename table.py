def print_table(game_Table):

    horizontal_idx = '{0:^9}'.format('1') + '{0:^6}'.format('2') + '{0:^6}'.format('3')
    horizontal_line = '  ' + '-'*19
    vertical_line1 = '1 ' + '|' + '{0:^5}'.format(game_Table[0][0]) + '|' + '{0:^5}'.format(game_Table[0][1]) + '|' + '{0:^5}'.format(game_Table[0][2]) + '|'
    vertical_line2 = '2 ' + '|' + '{0:^5}'.format(game_Table[1][0]) + '|' + '{0:^5}'.format(game_Table[1][1]) + '|' + '{0:^5}'.format(game_Table[1][2]) + '|'
    vertical_line3 = '3 ' + '|' + '{0:^5}'.format(game_Table[2][0]) + '|' + '{0:^5}'.format(game_Table[2][1]) + '|' + '{0:^5}'.format(game_Table[2][2]) + '|'

    print(horizontal_idx, horizontal_line, vertical_line1, horizontal_line, vertical_line2, horizontal_line,
        vertical_line3, horizontal_line, sep='\n')
