def validate_set_result(result):
    set_winner = max(result)
    set_loser = min(result)
    set_result = f'{result[0]}:{result[1]}'

    if set_winner == set_loser \
            or set_winner not in [6, 7] \
            or set_winner == 6 and set_loser not in [0, 1, 2, 3, 4] \
            or set_winner == 7 and set_loser not in [5, 6]:
            print(f'Wrong set result: {set_result}')
    else:
        return set_result


def validate_values_in_set_result(value):
    if len(value) != 3:
        print('Incorrect format of set result')
    if ':' not in value:
        print("You didn't use ':' sign to divide number of games")
    else:
        games = value.split(':')
        if games[0].isdigit() and games[1].isdigit():
            # print('Correct values')
            return int(games[0]), int(games[1])
        else:
            print("You didn't enter proper values for number of games")


def validate_match_result(match_result: list):
    if len(match_result) < 2:
        print('Not enough sets played')
        return False

    set1_player1 = int(match_result[0][0])
    set1_player2 = int(match_result[0][2])
    set2_player1 = int(match_result[1][0])
    set2_player2 = int(match_result[1][2])

    if len(match_result) == 2:
        if set1_player1 > set1_player2 and set2_player1 > set2_player2:
            print('The first player won the match')
            return True
        if set1_player1 < set1_player2 and set2_player1 < set2_player2:
            print('The second player won the match')
            return True
        else:
            print('Match unfinished. 1:1 in sets.')
            return False



match_result = []


while True:
    user_input = input('Enter result of first set [in format 7:5] => ')
    user_input_verified = validate_values_in_set_result(user_input)

    # function validate_values_in_set_result(first_set) returns None until proper vales are input.
    if user_input_verified is not None:
        first_set_result = validate_set_result(user_input_verified)
        if first_set_result is not None:
            match_result.append(first_set_result)
            break


print(f'Verified first set result {first_set_result}')
print(f'Verified match result {match_result}')
