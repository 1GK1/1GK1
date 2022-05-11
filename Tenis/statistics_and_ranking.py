def count_win_rate_ranking_points(players_stats):
    """Adds ranking points depending of number of matches won.
    Player with the greatest number of won matches gets 1 point, the second 2 points,
    the last one the number of points is equal to the number of players classified.
    If two or more players have the same number of won matches each one get same number
    of points equal to their 'ex aequo' position
    Notice:
    """


    number_of_players = len(players_stats)

    ranking_points = 1
    ranking_shift = 0

    for i in range(number_of_players - 1):
        if players_stats[i][1][0] == players_stats[i + 1][1][0]:
            players_stats[i][1].append(ranking_points)
            players_stats[i + 1][1].append(ranking_points)
            ranking_shift += 1
        else:
            players_stats[i][1].append(ranking_points)
            ranking_points = ranking_points + ranking_shift + 1
            players_stats[i + 1][1].append(ranking_points)
            ranking_shift = 0


def display_ranking(players_stats: list):
    print('-' * 63)
    print('Player'.ljust(20), 'Wins'.ljust(5), 'Losses'.ljust(7), 'Matches'.ljust(8), 'Win_rate'.ljust(8),
          'Win_rank'.ljust(10), 'Win_rate_rank')
    print('-' * 63)
    for player, stats in players_stats:
        print(player.ljust(20), str(stats[0]).rjust(4), str(stats[1]).rjust(6), str(stats[2]).rjust(8),
              str(stats[3]).rjust(9), str(stats[4]).rjust(10))


player_stats = [('Andrzej Kulewik', [14, 5, 19, 0.74]), ('B', [14, 2, 6, 0.67]), ('Grzegorz Kędzia', [2, 3, 5, 0.4]),
                ('C', [2, 0, 2, 1.0]), ('D', [2, 1, 2, 0.5]), ('E', [1, 2, 2, 0.4]), ('Z', [0,0,0,0])]
# print(player_stats)

count_win_rate_ranking_points(player_stats)
print(player_stats)
display_ranking(player_stats)
# print(player_stats[0][1][0])
# print(player_stats[1][1][0])
