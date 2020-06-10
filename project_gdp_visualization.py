#coding:utf-8
"""
世行历史数据基本分类及其可视化
Erguan(郑林涛)
2020/6/14
"""


import csv
import math
import pygal
import pygal.maps.world  #导入需要使用的库


# 读取数据
def read_csv_as_nested_dict(filename, keyfield): #读取原始csv文件的数据，格式为嵌套字典
	"""
	输入参数:
	filename:csv文件名
	keyfield:键名
	separator:分隔符
	quote:引用符
	输出:
	读取csv文件数据，返回嵌套字典格式，其中外层字典的键对应参数keyfiled，内层字典对应每行在各列所对应的具体值
	"""
	result = {}
	with open(filename,newline = "")as csvfile:
		csvreader = csv.DictReader(csvfile)
		for row in csvreader:
			rowid = row[keyfield]
			result[rowid] = row
	return result


gdp_countries = read_csv_as_nested_dict("isp_gdp.csv","Country Name")
# print(gdp_countries)


pygal_countries = pygal.maps.world.COUNTRIES #读取pygal.maps.world中国家代码信息（为字典格式），其中键为pygal中各国代码，值为对应的具体国名(建议将其显示在屏幕上了解具体格式和数据内容）
# print(pygal_countries)


# 返回在世行有GDP数据的绘图库国家代码字典，以及没有世行GDP数据的国家代码集合
def reconcile_countries_by_name(plot_countries, gdp_countries): #返回在世行有GDP数据的绘图库国家代码字典，以及没有世行GDP数据的国家代码集合
	"""
	输入参数:
	plot_countries: 绘图库国家代码数据，字典格式，其中键为绘图库国家代码，值为对应的具体国名
	gdp_countries:世行各国数据，嵌套字典格式，其中外部字典的键为世行国家代码，值为该国在世行文件中的行数据（字典格式)
	输出：
	返回元组格式，包括一个字典和一个集合。其中字典内容为在世行有GDP数据的绘图库国家信息（键为绘图库各国家代码，值为对应的具体国名),
	集合内容为在世行无GDP数据的绘图库国家代码
	"""
	dict1 = {}
	set1 = set()
	for i in plot_countries:
		country_name = plot_countries[i] 
		result  =  country_name in gdp_countries
		if result == True:
			dict1[i] = country_name
		if result == False:
			set1.add(i)
	tuple1 = (dict1,set1)
	# print(tuple1)
	return tuple1 

# 筛选出某一给定年份各国及其在世行对应的GDP值、没有世行GDP数据的国家以及只是该年没有GDP数据的国家
def build_map_dict_by_name(gdpinfo, plot_countries, year):
	"""
	输入参数:
	gdpinfo: 
	plot_countries: 绘图库国家代码数据，字典格式，其中键为绘图库国家代码，值为对应的具体国名
	year: 具体年份值
	输出：
	输出包含一个字典和二个集合的元组数据。其中字典数据为绘图库各国家代码及对应的在某具体年份GDP产值（键为绘图库中各国家代码，值为在具体年份（由year参数确定）所对应的世行GDP数据值。为
	后续显示方便，GDP结果需转换为以10为基数的对数格式，如GDP原始值为2500，则应为log2500，ps:利用math.log()完成)
	2个集合一个为在世行GDP数据中完全没有记录的绘图库国家代码，另一个集合为只是没有某特定年（由year参数确定）世行GDP数据的绘图库国家代码
	"""
	tuple1 = reconcile_countries_by_name(plot_countries, gdp_countries)
	dict2 = tuple1[0]
	set1 = tuple1[1]
	set2 = set()
	dict3 = {}
	for i in dict2:
		countryname = dict2[i]
		dictt = gdp_countries[countryname]
		value1 = dictt[year]
		if value1 == "":
			set2.add(i)
		else:
			value1 = float(value1)
			value1 = math.log10(value1)
			dict3[i] = value1
	tuple2 = (dict3,set1,set2)
	print(tuple2)
	return(tuple2)


# 将具体某年世界各国的GDP数据(包括缺少GDP数据以及只是在该年缺少GDP数据的国家)以地图形式可视化
def render_world_map(gdpinfo, plot_countries, year, map_file):
	"""
	Inputs:
	gdpinfo:gdp信息字典
	plot_countires:绘图库国家代码数据，字典格式，其中键为绘图库国家代码，值为对应的具体国名
	year:具体年份数据，以字符串格式程序，如"1970"
	map_file:输出的图片文件名
	目标：将指定某年的世界各国GDP数据在世界地图上显示，并将结果输出为具体的的图片文件
	提示：本函数可视化需要利用pygal.maps.world.World()方法
	"""
	tuple2 = build_map_dict_by_name(gdpinfo, plot_countries, year)
	dict3 = tuple2[0]
	set1 = tuple2[1]
	set2 = tuple2[2]
	gdp_world_map = pygal.maps.world.World()
	gdp_world_map.title = "全球GDP分布图"
	gdp_world_map.add(year,dict3)
	gdp_world_map.add("missing from world bank",set1)
	gdp_world_map.add("no data at this year",set2)
	gdp_world_map.render_to_file(map_file)


# 测试函数
def test_render_world_map(year):
	"""
	对各功能函数进行测试
	"""
	gdpinfo = {
		"gdpfile": "isp_gdp.csv",
		"separator": ",",
		"quote": '"',
		"min_year": 1960,
		"max_year": 2015,
		"country_name": "Country Name",
		"country_code": "Country Code"
	}
	pygal_countries = pygal.maps.world.COUNTRIES#获得绘图库pygal国家代码字典
	render_world_map(gdpinfo, pygal_countries, year, "郑林涛.svg")


# 程序测试和运行
print("欢迎使用世行GDP数据可视化查询")
print("----------------------")
year = input("请输入需查询的具体年份:")
test_render_world_map(year)
