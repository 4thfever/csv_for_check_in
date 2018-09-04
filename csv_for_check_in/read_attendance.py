'''
从attendance的csv表格中读入一个人某年的出勤信息
'''

import pandas as pd 
import numpy as np
from datetime import timedelta,date

#csv转换成list形式
def read_attendance(csv_file):
	df_atte = pd.read_csv(csv_file,encoding = 'gbk',header = None)
	len_columns = len(df_atte.columns)
	len_row = 11
	return df_atte.drop(columns = 0).values

#str转成月日
def str2int(date_str):
	date_int = date_str.split('.')
	return [int(date_int[0]),int(date_int[1])]

#划定范围内的日期信息，主要用在跨月的时候
def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

#读入某个cell的信息。一个cell可能有如下三种情况：
# 1.没有信息
# 2.某个日期，如1.1
# 3.某个时间段，如1.1-2.3
# 其他形式的输入将不会支持
def read_cell(year,date_input):
	if type(date_input) != str:
		date_input = str(date_input)

	if '-' in date_input:
		days = date_input.split('-')
		days_start = str2int(days[0])
		days_end = str2int(days[1])

		date_start = date(year,days_start[0],days_start[1])
		date_end = date(year,days_end[0],days_end[1])
		dates = daterange(date_start,date_end)

		days = [ [date.month,date.day] for date in dates]
		return days

	elif '.' in date_input :
		return [str2int(date_input)]

#主程序
def read_csv(year,csv_file):
	list_input = read_attendance(csv_file)
	input_read = [None]*11
	for i,row in enumerate(list_input):
		input_read[i] =  [read_cell(year,cell) for cell in row if read_cell(year,cell) is not None ]
		input_read[i] =  [b  for a in input_read[i] for b in a]
	input_read = np.array(input_read)
	return input_read

if __name__ == '__main__':
	csv_file = 'attendance.csv'
	result = read_csv(2018,csv_file)
	print(result)

