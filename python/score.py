#!/usr/bin/env python3

import csv
from os.path import join

DATA_DIRECTORY = "../data"
DATA_FILE = "dominion-scores.csv"
DATA_FILE_PATH = join(DATA_DIRECTORY, DATA_FILE)

COLOR_GREEN = '\033[32m'
COLOR_DEFAULT = '\033[0m'


## Utility Functions #######################################

def read_csv_data(file_name):
	with open(file_name) as file:
		reader = csv.reader(file)
		header = next(reader)
		data = [row for row in reader]

	return header, data

def read_csv_header(file_name):
	with open(file_name) as file:
		reader = csv.reader(file)
		return next(reader)
	return []

def to_int(list_of_lists):
	ints = []
	for sublist in list_of_lists:
		ints.append(list(map(int, sublist)))
	return ints


## Program Functions #######################################

def print_all_scores(players, games, player_totals):

	print()

	for player in players:
		print(f'{player:>8}    ', end='')
	print()
	print()

	for scores in games:
		print_game_scores(scores)
	print()

	print_game_scores(player_totals)
	print()

def print_game_scores(scores):

	highest = max(scores)
	total = sum(scores)
	for score in scores:
		print(f'{score * 100:>8.1f}', end='')
		print(f' {COLOR_GREEN}✓{COLOR_DEFAULT}  ' if (score == highest) else '    ', end = '')
	print()

def read_games(file_name):
	headings, games = read_csv_data(file_name)
	return headings, to_int(games)


## Main ####################################################

# Read Data

players, games = read_games(DATA_FILE_PATH)
game_count = len(games)


# Calulate Game Total Points

totals = [sum(scores) for scores in games]


# Convert Scores To Proportional Scores

proportional_games = []

for scores, total in zip(games, totals):
	proportional_scores = [score / total for score in scores ]
	proportional_games.append(proportional_scores)
	

# Calculate Final Scores

player_totals = [0] * len(players)

for scores in proportional_games:
	for index, score in enumerate(scores):
		player_totals[index] = player_totals[index] + score



# Show Scores

print_all_scores(players, proportional_games, player_totals)

