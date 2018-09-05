from chinese_calendar import get_workdays,get_holidays
from read_attendance import read_csv
import datetime
import pandas as pd
import numpy as np

class DaysInfo(object):
	"""
	docstring for DaysInfo
	读取一年中的全部数据，建立一年的日程表
	"""
	#可以选择是否输入其他类型假期的csv，不输入则为无
	def __init__(self, year, csv_file = ''):
		if csv_file != '':
			self.atte = read_csv(year,csv_file)
		else:
			self.atte = [[]]
		self.year = year
		self.get_days_in_year()
		self.find_holidays()
		self.find_workdays()
		self.days_info(self.atte)
		self.create_df()

	#一年的开头结尾
	def get_days_in_year(self):
		self.year_start = datetime.date(self.year,1,1)
		self.year_end = datetime.date(self.year,12,31)

	#调用chinese calendar，输出工作日和休息日
	def find_workdays(self):
		self.workdays = get_workdays(self.year_start,self.year_end)
		self.workdays = [[workday.month,workday.day] for workday in self.workdays]

	def find_holidays(self):
		self.holidays = get_holidays(self.year_start,self.year_end)
		self.holidays = [[holiday.month,holiday.day] for holiday in self.holidays]

	#读入每个日程的数据
	#0代表不存在这一天，1workday，2holiday，3出差，4 驻外工作，5年休假，6事假，7病假，8婚假，9产假，10探亲假，11丧假，12工伤假，13旷工
	def days_info(self,atte):
		self.list_days = np.zeros([12,31])
		for i in range(1,13):
			for j in range(1,32):
				# 第0行代表一月，第0列代表1日

				if [i,j] in self.workdays:
					self.list_days[i-1,j-1] = 1
				if [i,j] in self.holidays:
					self.list_days[i-1,j-1] = 2

		for i,absence in enumerate(self.atte):
			for j,the_date in enumerate(absence):
				#默认跳过周六日
				if self.list_days[the_date[0] - 1,the_date[1] - 1 ] != 2:
					if self.list_days[the_date[0] - 1,the_date[1] - 1 ] > 2:
						raise TypeError('出勤信息重复！')
					else:	
						self.list_days[the_date[0] - 1,the_date[1] - 1 ] = i + 3

	#建立pandas的dataframe，给之后生成表格做准备
	def create_df(self):
		self.df_days = pd.DataFrame(self.list_days,columns = list(range(1,32)),index = list(range(1,13)))
		#统计出勤，缺勤和在外
		count_chuqin = np.sum(self.list_days == 1,axis =1)
		count_zaiwai = np.sum(self.list_days == 3,axis =1) + np.sum(self.list_days == 4,axis =1) 
		count_queqin = np.sum(self.list_days == 13,axis =1)
		self.df_days['chuqin'] = count_chuqin
		self.df_days['zaiwai'] = count_zaiwai
		self.df_days['queqin'] = count_queqin

if __name__ == '__main__':
	c = DaysInfo(2018,'attendance.csv')
	print(c.df_days)
