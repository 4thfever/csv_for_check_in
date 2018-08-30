from chinese_calendar import get_workdays,get_holidays
import datetime
import pandas as pd
import numpy as np

class DaysInfo(object):
	"""
	docstring for DaysInfo
	读取一年中的全部数据，建立一年的日程表
	"""
	#可以选择是否输入其他类型假期，不输入则为无
	def __init__(self, year, chuchai =[],zhuwai =[],nianjia =[],shijia =[],bingjia =[],
				hunjia = [],chanjia =[],tanqin =[],sangjia =[],gongshang =[],kuanggong =[]):
		super(DaysInfo, self).__init__()
		self.year = year
		self.chuchai = chuchai
		self.zhuwai =zhuwai
		self.nianjia =nianjia
		self.shijia =shijia
		self.bingjia =bingjia
		self.hunjia =hunjia
		self.chanjia =chanjia
		self.tanqin =tanqin
		self.sangjia =sangjia
		self.gongshang =gongshang
		self.kuanggong =kuanggong

		self.get_input()
		self.find_holidays()
		self.find_workdays()
		# print(self.workdays)
		self.days_info()
		self.create_df()

	#一年的开头结尾
	def get_input(self):
		self.start = datetime.date(self.year,1,1)
		self.end = datetime.date(self.year,12,31)

	#调用chinese calendar，输出工作日和休息日
	def find_workdays(self):
		self.workdays = get_workdays(self.start,self.end)
		self.workdays = [[workday.month,workday.day] for workday in self.workdays]

	def find_holidays(self):
		self.holidays = get_holidays(self.start,self.end)
		self.holidays = [[holiday.month,holiday.day] for holiday in self.holidays]

	#读入每个日程的数据
	#0代表不存在这一天，1workday，-1holiday，3出差，4 驻外工作，5年休假，6事假，7病假，8婚假，9产假，10探亲假，11丧假，12工伤假，13旷工
	def days_info(self):
		self.list_days = np.zeros([12,31])
		for i in range(1,13):
			for j in range(1,32):
				# 第0行代表一月，第0列代表1日

				if [i,j] in self.workdays:
					self.list_days[i-1,j-1] = 1
				if [i,j] in self.holidays:
					self.list_days[i-1,j-1] = -1

				#如果有额外的假，就替换掉之前的
				if [i,j] in self.chuchai:      
					self.list_days[i-1,j-1] = 3
				if [i,j] in self.zhuwai:
					self.list_days[i-1,j-1] = 4
				if [i,j] in self.nianjia:
					self.list_days[i-1,j-1] = 5
				if [i,j] in self.shijia:
					self.list_days[i-1,j-1] = 6
				if [i,j] in self.bingjia:
					self.list_days[i-1,j-1] = 7
				if [i,j] in self.hunjia:
					self.list_days[i-1,j-1] = 8
				if [i,j] in self.chanjia:
					self.list_days[i-1,j-1] = 9
				if [i,j] in self.tanqin:
					self.list_days[i-1,j-1] = 10
				if [i,j] in self.sangjia:
					self.list_days[i-1,j-1] = 11
				if [i,j] in self.gongshang:
					self.list_days[i-1,j-1] = 12
				if [i,j] in self.kuanggong:
					self.list_days[i-1,j-1] = 13

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
	c = DaysInfo(2018,chuchai = [[1,1],[12,31]],zhuwai = [[1,4]],kuanggong = [[1,2]])
	print(c.df_days)
