#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：郑林涛
日期：2020年4月5
"""




#制作步骤：

    # 0 - 石头 # 1 - 史波克 # 2 - 纸 # 3 - 蜥蜴 # 4 - 剪刀

    # 输出"-------- "进行分割
    
    # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice

    # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number

    # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number

    # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象

    # 在屏幕上显示计算机选择的随机对象

    # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果

    # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”

    
    
    
    
#导入randon随机库并产生[0,4]的随机数    
import random
comp_number=random.randrange(0,5)#randon随机库产生的随机数包括下限但不包括上限





#将游戏对象对应到不同的整数
def name_to_number(player_choice):
	if player_choice=="石头":
		return 0
	elif player_choice=='史波克':
		return 1
	elif player_choice=='纸':
		return 2
	elif player_choice=='蜥蜴':
		return 3
	elif player_choice=='剪刀':
		return 4





# 将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
def number_to_name(comp_number):
	if comp_number==0:
		return '石头'
	elif comp_number==1:
		return '史波克'
	elif comp_number==2:
		return '纸'
	elif comp_number==3:
		return '蜥蜴'
	elif comp_number==4:
		return '剪刀'





#用户玩家任意给出一个选择，根据RPSLS游戏规则，判断胜负
def rpsls(player_choice):
	if (player_choice_number==0 and (comp_number==3 or comp_number==4)) or (player_choice_number== 1 and (comp_number==0 or comp_number==4)) or (player_choice_number==2 and (comp_number==0 or comp_number==1)) or (player_choice_number==3 and (comp_number==1 or comp_number==2)) or (player_choice_number==4 and (comp_number==3 or comp_number==2)):
		return '您赢了'
	elif (player_choice_number==0 and comp_number==0) or (player_choice_number==1 and comp_number==1) or (player_choice_number==2 and comp_number==2) or (player_choice_number==3 and comp_number==3) or (player_choice_number==4 and comp_number==4):
		return '平局'
	else:
		return '计算机赢了'





#结果调用和显示
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
player_choice=input()#输入玩家的选择
player_choice_number=name_to_number(player_choice)#调用函数name_to_number，得到玩家选择所对应的数字
comp_number_name=number_to_name(comp_number)#调用函数number_to_name，得到计算机产生的随机数所对应的选择
result=rpsls(player_choice)#调用函数rpsls，得到玩家和电脑选择的胜负
if player_choice==('石头' or '剪刀' or '布' or '史波克' or '蜥蜴'):#用if函数判断玩家的选择是不是石头/剪刀/布/史波克/蜥蜴中的一个
	print("----------------")
	print("您的选择为:"+player_choice)
	print("计算机的选择为:"+comp_number_name)
	print(result)
else:
	print("Error: No Correct Name")
