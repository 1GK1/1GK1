def count_statistics(players_won_loss: dict):
    """Takes dictionary with player name as key and number of won and lost matches as value.
    Adds number of total matches won and win rate to the values"""

    for player, results in players_won_loss.items():
        won_matches = results[0]
        lost_matches = results[1]
        matches_played = won_matches + lost_matches

        try:
            win_rate = round(won_matches / matches_played, 2)
        except ZeroDivisionError:
            win_rate = 0

        player = results.append(matches_played)
        player = results.append(win_rate)


def count_ranking_points(players: dict, sort_by_wins=True) -> list:
    """Adds ranking points depending of number of matches won/percentage of matches won (win_rate).
    Player with the greatest number of won matches/percentage of matches won gets 1 point, the second 2 points,
    the last one the number of points is equal to the number of players classified.
    If two or more players have the same number of won matches/percentage of matches won each one get same number
    of points equal to their 'ex aequo' position
    """
    # print('input:', players, sort_by_wins)

    if sort_by_wins:
        position = 0
        players_stats = sorted(players.items(), key=lambda x: x[1][position], reverse=True)
    else:
        position = 3
        players_stats = sorted(players, key=lambda x: x[1][position], reverse=True)

    # print('sorted input', players_stats)

    number_of_players = len(players_stats)

    ranking_points = 1
    ranking_shift = 0

    players_stats[0][1].append(ranking_points)

    # TODO: consider if for win_rate BigDecimal is needed
    for i in range(number_of_players - 1):
        if players_stats[i][1][position] == players_stats[i + 1][1][position]:
            # players_stats[i][1].append(ranking_points)
            players_stats[i + 1][1].append(ranking_points)
            ranking_shift += 1
        else:
            # players_stats[i][1].append(ranking_points)
            ranking_points = ranking_points + ranking_shift + 1
            players_stats[i + 1][1].append(ranking_points)
            ranking_shift = 0

    return players_stats


# potential place where weights for win rank and win rate can be applied
def count_total_rank(players: list) -> list:
    for player, stats in players:
        win_rank = stats[4]
        win_rate_rank = stats[5]
        total_rank = win_rank + win_rate_rank
        stats.append(total_rank)

    # sorting by total rank
    players = sorted(players, key=lambda x: x[1][6])

    print(players)
    return players


def display_ranking(players_stats: list):
    print('-' * 88)
    print('Player'.ljust(20), 'Wins'.ljust(5), 'Losses'.ljust(7), 'Matches'.ljust(8), 'Win_rate'.ljust(8),
          'Win_rank'.ljust(10), 'Win_rate_rank'.ljust(12), 'Total_rank'.ljust(10))
    print('-' * 88)
    for player, stats in players_stats:
        print(player.ljust(20), str(stats[0]).rjust(4), str(stats[1]).rjust(6), str(stats[2]).rjust(8),
              str(stats[3]).rjust(9), str(stats[4]).rjust(10), str(stats[5]).rjust(12), str(stats[6]).rjust(10))


players = {'Grzegorz Kędzia': [6, 3], 'B': [1, 3], 'C': [2, 3], 'D': [1, 1], 'Andrzej Kulewik': [5, 5],
           'Kuba': [10, 1], 'Master': [20, 3], 'Loser': [0, 12]}



# counting total number of matches played and win rate
count_statistics(players)
# counting ranking points for won matches
players = count_ranking_points(players, sort_by_wins=True)
# counting ranking points for win rate
players = count_ranking_points(players, sort_by_wins=False)
print(players)
# counting total ranking
players = count_total_rank(players)

display_ranking(players)


