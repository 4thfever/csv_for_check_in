import pandas as pd 
import datetime
from chinese_calendar import is_workday, is_holiday
import numpy as np

df_days = pd.DataFrame(columns = ['year','month','day','is_work'])

# start = datetime.datetime.strptime("01-01-2015", "%d-%m-%Y")
# end = datetime.datetime.strptime("31-08-2018", "%d-%m-%Y")
# date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

# for i,date in enumerate(date_generated):
#     print(date.strftime("%d-%m-%Y"),is_workday(date))
#     df_days.loc[i] = [date.year,date.month,date.day,is_workday(date)]

# days_route = 'D:\\联研院\\程序\\日历\\'
# df_days.to_csv(days_route + 'days.csv',index = False)

df_days = pd.read_csv('D:\\联研院\\程序\\日历\\days.csv', engine='python')
# print(df_days.loc[(df_days['year'] == 2015) & (df_days['month'] == 1 )]['is_work'].tolist())

days_ranged = []
for i in range(2015,2019):
	for j in range(1,13):
		days_ranged.append(df_days.loc[(df_days['year'] == i) & (df_days['month'] == j )]['is_work'].tolist())
# print(days_ranged)

for i in range(0,48):
	print(i,len(days_ranged[i]))
	day_in_month = len(days_ranged[i])
	days_ranged[i] += ['None']*(31 - day_in_month)

df_days_ranged = pd.DataFrame(days_ranged)
print(df_days_ranged)
df_days_ranged.to_csv('D:\\联研院\\程序\\日历\\days_ranged.csv')
