#!/usr/bin/env python3

import numpy as np

from os.path import exists
from os.path import join
from sys import argv
import csv
import sys

# Color: Use Form '\033[xxm'
# Full Color Chart: https://speedsheet.io/s/bash?search=color&select=upmb

COLOR_GREEN = '\033[32m'
COLOR_DEFAULT = '\033[0m'


## Utility Functions #######################################

def get_file_name_parameter():
	return argv[1]

def no_parameters():
	return len(argv) <= 1

def read_csv_data(file_name):
	return np.genfromtxt(file_name, delimiter = ',', skip_header = 1)

def read_csv_header(file_name):
	with open(file_name) as file:
		reader = csv.reader(file)
		return next(reader)
	return []


## Program Functions #######################################

def calculate_and_show_scores(file_name):

	players, games = read_game_data(file_name)
	proportional_games, proportional_totals = caluclate_scores(games)
	print_all_scores(players, proportional_games, proportional_totals)

def caluclate_scores(games):

	totals = games.sum(axis = 1).reshape (-1, 1)
	game_count = len(games)

	proportional_games = (games / totals)
	proportional_totals = proportional_games.sum(axis = 0) / game_count

	return proportional_games, proportional_totals


def print_all_scores(players, games, player_totals):

	print()

	print_players(players)
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

def print_players(players):

	for player in players:
		print(f'{player:>8}    ', end='')
	print()

def read_game_data(file_name):

	players = read_csv_header(file_name)
	games = read_csv_data(file_name)

	return players, games

def show_file_not_found(file_name):
	print()
	print(f'Could not find file: {file_name}')
	print()

def show_help():

	print('''
score.py [ game_scores_file.csv ]

Converts game scores to proportional scores,
and shows all and final scores as percentages.

File Format:

    name 1, name 2, ...
    score, score, ...
    score, score, ...''')

def verify_file(name):
	if not exists(name):
		show_file_not_found(name)
		sys.exit(2)


## Main ####################################################

if no_parameters():
	show_help()
else:
	file_name = get_file_name_parameter()
	verify_file(file_name)
	calculate_and_show_scores(file_name)

