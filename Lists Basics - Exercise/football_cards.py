input_line = input().split()

team_A = 11
team_B = 11
sent_off_players = list()
is_terminated = False

for i in range(len(input_line)):
    if input_line[i] in sent_off_players:
        continue
    curr_player = input_line[i]
    if curr_player[0] == "A":
        team_A -= 1
        sent_off_players.append(curr_player)
    else:
        team_B -= 1
        sent_off_players.append(curr_player)
    if team_A < 7 or team_B < 7:
        is_terminated = True
        break

print(f"Team A - {team_A}; Team B - {team_B}")
if is_terminated:
    print("Game was terminated")
