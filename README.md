# 生成考勤表
自动调用中国假期数据，排列出国家法定的节假日与工作日，外加自由设定的个人假期，最后给出符合联研院计算所标准的考勤表格。
## 安装
clone到本地即可

## 样例

### 模板：
![模板](https://github.com/4thfever/csv_for_check_in/blob/master/pics/example1.PNG)

### 使用
打开 create_check_in_csv.py，调用create_check_in_csv 函数
```
create_check_in_csv(2018,'王某某',chuchai = [[1,1],[12,31]],zhuwai = [[1,4]],kuanggong = [[1,2]])
```

### 生成文件：
![生成文件](https://github.com/4thfever/csv_for_check_in/blob/master/pics/example2.PNG)

# 参数：

# 依赖：
