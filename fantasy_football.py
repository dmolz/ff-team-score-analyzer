from espnff import League 

league_id = 926261
year = 2018
league = League(league_id,year)
# teams = league.teams

team_dict = {}
all_teams = []
for team in league.teams:
	team_dict[team.team_abbrev] = team.scores
	# all_teams.append()

print("\nChoose a team:")
i = 0
for key in team_dict.keys():
	print("{}\t".format(key),end='')
	i += 1
	if (i % 4 == 0):
		print()

# print(team_dict)

print()
team1 = input("Team 1: ")
team2 = input("Team 2: ")
print()

team1_wins = 0
team2_wins = 0
all_teams = team_dict.keys()
for i in range(0,13):
	team1_score = team_dict[team1][i]
	team2_score = team_dict[team2][i]

	if team1_score > team2_score:
		winner = team1
		team1_wins += 1
	else:
		winner = team2
		team2_wins += 1

	print("Week {:2}: {}-{}\t{} wins".format(i+1,team1_score,team2_score,winner))

print()
print("{} would be {}-{} if they played {} every week".format(team1,team1_wins,team2_wins,team2))