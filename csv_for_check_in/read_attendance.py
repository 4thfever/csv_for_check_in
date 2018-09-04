import pandas as pd 
import numpy as np
from datetime import timedelta,date


def read_attendance(csv_file):
	df_atte = pd.read_csv(csv_file,encoding = 'gbk',header = None)
	len_columns = len(df_atte.columns)
	len_row = 11
	# print(len_columns)
	return df_atte.drop(columns = 0).values

def str2int(date_str):
	date_int = date_str.split('.')
	return [int(date_int[0]),int(date_int[1])]

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

def read_input(year,date_input):
	if type(date_input) != str:
		date_input = str(date_input)

	if '-' in date_input:
		# print(date_input)

		days = date_input.split('-')
		days_start = str2int(days[0])
		days_end = str2int(days[1])

		date_start = date(year,days_start[0],days_start[1])
		date_end = date(year,days_end[0],days_end[1])
		dates = daterange(date_start,date_end)

		days = [ [date.month,date.day] for date in dates]
		return days

	# elif date_input == 'nan':
	# 	return None
	elif '.' in date_input :
		return [str2int(date_input)]

def read_csv(year,csv_file):
	list_input = read_attendance(csv_file)
	list_input_read = [None]*11
	for i,row in enumerate(list_input):
		list_input_read[i] =  [read_input(year,cell) for cell in row if read_input(year,cell) is not None ]
		list_input_read[i] =  [b  for a in list_input_read[i] for b in a]
	list_input_read = np.array(list_input_read)
	# a[a != np.array(None)]
		# list_input_read[i] = [n for m in list_input_read[i] for n in m]
	return list_input_read



if __name__ == '__main__':
	csv_file = 'attendance.csv'
	result = read_csv(2018,csv_file)
	print(result)

