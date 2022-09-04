def find_winner(n, m):

    players = [p for p in range(1, n+1)]
    index = -1
    while len(players) > 1:
        tmp = m
        while tmp >= len(players):
            tmp -= len(players)
        index += tmp
        if index >= len(players):
            index -= len(players)

        players.pop(index)
        index -= 1
    print(players[0])


find_winner()
