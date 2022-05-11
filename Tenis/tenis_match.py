def validate_set_result(result: tuple) -> str:
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


def validate_super_tiebreak_result(result: tuple) -> str:
    set_winner = max(result)
    set_loser = min(result)
    tiebreak_result = f'{result[0]}:{result[1]}'

    if set_winner == set_loser \
            or set_winner < 10:
        print(f'Wrong tiebreak_result: {tiebreak_result}')
        return None

    if set_winner == 10 and set_loser not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        print(f'Wrong tiebreak_result: {tiebreak_result}')
        return None

    if set_winner > 10 and set_winner - set_loser != 2:
        print(f'Wrong tiebreak_result: {tiebreak_result}')
        return None

    return tiebreak_result


def validate_values_in_set_result(value: str) -> tuple:
    if ':' not in value:
        print("You didn't use ':' sign to divide number of games")
    else:
        games = value.split(':')
        if games[0].isdigit() and games[1].isdigit():
            return int(games[0]), int(games[1])
        else:
            print("You didn't enter proper values for number of games")


def validate_values_in_super_tiebreak_result(value: str) -> tuple:
    if ':' not in value:
        print("You didn't use ':' sign to divide number of points")
    else:
        games = value.split(':')
        if games[0].isdigit() and games[1].isdigit():
            return int(games[0]), int(games[1])
        else:
            print("You didn't enter proper values for number of points")


def validate_match_result(match_result):
    if len(match_result) < 2:
        # print('Not enough sets played')
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
            # print('Match unfinished. 1:1 in sets.')
            return False

    if len(match_result) == 3:
        set3_player1 = match_result[2][0]
        set3_player2 = match_result[2][1]
        if set3_player1 > set3_player2:
            print('The first player won the match')
        else:
            print('The second player won the match')
        return True


match_result = []
is_match_finished = False


while not is_match_finished:
    sets_played = len(match_result)
    while True:
        if sets_played == 0:
            msg = 'Enter result of first set [in format 7:5] => '
        if sets_played == 1:
            msg = 'Enter result of second set [in format 7:5] => '
        if sets_played == 2:
            msg = 'Enter result of super tie-break [in format 10:5] => '
        user_input = input(f'{msg}')

        # two sets means that the third set is super tie-break
        if sets_played == 2:
            user_input_verified = validate_values_in_super_tiebreak_result(user_input)
        else:
            user_input_verified = validate_values_in_set_result(user_input)

        # function validate_values_in_set_result(first_set) returns None until proper vales are input.
        if user_input_verified:
            if sets_played == 2:
                set_result = validate_super_tiebreak_result(user_input_verified)
            else:
                set_result = validate_set_result(user_input_verified)

            if set_result:
                match_result.append(set_result)
                is_match_finished = validate_match_result(match_result)
                break

print(f'Verified match result {match_result}')
