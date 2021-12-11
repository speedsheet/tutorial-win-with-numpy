#!/usr/bin/env python3

import numpy as np

from os.path import join
import csv

DATA_DIRECTORY = "../data"
DATA_FILE = "dominion-scores.csv"
DATA_FILE_PATH = join(DATA_DIRECTORY, DATA_FILE)

COLOR_GREEN = '\033[32m'
COLOR_DEFAULT = '\033[0m'

# stop scan


## Utility Functions #######################################

def read_csv_data(file_name):
	return np.genfromtxt(file_name, delimiter = ',', skip_header = 1)

def read_csv_header(file_name):
	with open(file_name) as file:
		reader = csv.reader(file)
		return next(reader)
	return []


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
	for score in scores:
		print(f'{score * 100:>8.1f}', end='')
		print(f' {COLOR_GREEN}✓{COLOR_DEFAULT}  ' if (score == highest) else '    ', end = '')
	print()

def read_games(file_name):
	return (read_csv_header(file_name),
			read_csv_data(file_name))


## Main ####################################################

# Read Data

players, games = read_games(DATA_FILE_PATH)
game_count = len(games)


# Calulate Game Total Points

totals = games.sum(axis = 1).reshape(-1, 1)


# Convert Scores To Proportional Scores

proportional_games = (games / totals)


# Calculate Final Scores

proportional_totals = proportional_games.sum(axis = 0) / game_count


# Show Scores

print_all_scores(players, proportional_games, proportional_totals)

