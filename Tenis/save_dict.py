import json

players = {'Grzegorz Kędzia': [2, 3], 'B': [4, 2], 'C': [2, 0], 'D': [1, 1], 'Andrzej Kulewik': [14, 5]}

#
# print(players)
# players['Hubert Hurkacz jr'] = [10, 0]
# print(players)

# saving data
with open(r'Tenis/players.txt', 'w', encoding='windows-1250') as file:
    json.dump(players, file)


# loading data
with open(r'Tenis/players.txt', 'r') as file:
    players = json.load(file)


#
print(players)


