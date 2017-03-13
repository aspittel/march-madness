import json 
from numpy.random import choice

def percentage_to_float(percentage):
	"""Converts a percentage string to a float"""
	return float(percentage.strip('%'))/100


def read_historic_data():
	"""Reads in historic seeding win percentages and parses"""
	historic_results = open('records.txt')
	historic_results = historic_results.read()
	historic_results = json.loads(historic_results)

	for seed_num, results in historic_results.items():
		for second_seed_num, result in results.items():
			results[second_seed_num] = percentage_to_float(result)
	return historic_results


def nest_games(data):
	"""Takes March Madness seeds and re-nests to Python dictionaries"""
	data = data.split('\n\n')
	nested_data = []
	for game in data:
		game = game.split('\n')
		game_teams = {}
		for team in game:
			if team != '':
				team = team.split(' ')
				game_teams[team[0]] = team[1]
		if game_teams:
			nested_data.append(game_teams)
	return nested_data


def make_predictions(data, file_name):
	"""Matches historical to current data to make predictions""" 
	write_file = open(file_name, 'w+')
	global historic_results
	n = 1
	for game in data:
		teams = game.values()
		seeds = game.keys()
		try:
			chance_favorite = historic_results[seeds[0]][seeds[1]]
		except:
			print(seeds)
			print(historic_results[seeds[0]])
		winner = choice(seeds, 1, p=[chance_favorite, 1-chance_favorite])
		write_file.write('{} {}\n'.format(winner[0], game[winner[0]]))
		if n % 2 == 0:
			write_file.write('\n')
		n += 1

historic_results = read_historic_data()

for round in range(1, 7):
	games = open('predictions/round_{}.txt'.format(round), 'r+')
	games = games.read()
	games = nest_games(games)

	make_predictions(games, 'predictions/round_{}.txt'.format(round + 1))