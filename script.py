import sys
import os.path
import requests
import csv

csv_filename = 'users.csv'

if not os.path.exists(csv_filename):
	print('O arquivo nao pode ser encontrado')
	sys.exit()

with open(csv_filename) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter = ',')
	line_count = 0
	for row in csv_reader:
		if line_count > 0:
			print('user_id:', row[0])
		line_count += 1
	print('Processed', line_count, 'lines.')
