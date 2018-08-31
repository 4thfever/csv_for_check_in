# 生成考勤表
自动调用中国假期数据，排列出国家法定的节假日与工作日，外加自由设定的个人假期，最后给出符合联研院计算所标准的考勤表格。
## 安装
clone到本地即可

## 样例

### 模板：
![模板](https://github.com/4thfever/csv_for_check_in/blob/master/pics/example1.PNG)

### 使用
打开 create_check_in_csv.py，调用create_check_in_csv 函数
```python
create_check_in_csv(2018,'王某某',chuchai = [[1,1],[12,31]],zhuwai = [[1,4]],kuanggong = [[1,2]])
```

### 生成文件：
![生成文件](https://github.com/4thfever/csv_for_check_in/blob/master/pics/example2.PNG)

# 参数

```python
create_check_in_csv(year,name,**args)
year#要生成考勤表的年份，目前支持2004-2018年
name#考勤对象姓名，不写的话用空格 ' '填充
args = [#其他假期数据
chuchai,# 出差日期，用[[m1,d1],[m2,d2],...,[mn,dn]]表示，m，d为出差的月份与日。出差的每一天需分开写入
zhuwai,# 驻外，表达方式同上
nianjia,# 年假
shijia,# 事假
bingjia,# 病假
hunjia,# 婚假
chanjia,# 产假
tanqin,# 探亲假
sangjia,# 丧假
gongshang,# 工伤
kuanggong]# 旷工
```
## 依赖
python-docx
chinese-calendar
