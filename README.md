# 生成考勤表
![](https://img.shields.io/badge/language-Python3.6-blue.svg)
![](https://img.shields.io/github/license/mashape/apistatus.svg)

自动调用中国假期数据，排列出国家法定的节假日与工作日，外加自由设定的个人假期，最后给出符合联研院计算所标准的考勤表格。
## 安装
clone到本地即可

## 样例

### 模板：
![模板](https://github.com/4thfever/csv_for_check_in/blob/master/pics/example1.PNG)

### 使用
打开 create_check_in_csv.py，调用create_check_in_csv 函数
```python
create_check_in_csv(2018,'王某某')
```

也可以读入储存出勤事件的csv文件。文件中用'月.日'表示单个日期，'起始月.起始日-终止月.终止日'表示日期段，不填则为空
```python
create_check_in_csv(2018,'王某某'，'attendance.csv')
```
attendance.csv的样式如下：

![attendance.csv](https://github.com/4thfever/csv_for_check_in/blob/master/pics/example2.PNG)


### 生成文件：
![生成文件](https://github.com/4thfever/csv_for_check_in/blob/master/pics/example3.PNG)

## 依赖
python-docx

pandas

numpy

chinese-calendar
