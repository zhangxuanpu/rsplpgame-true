#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：张轩溥
日期：2019/11/16
"""

import random
a=random.randint(0,4)
# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀
# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
    if name=="石头":
        b=0
    elif name=="史波克":
        b=1
    elif name=="布":
        b=2
    elif name=="蜥蜴":
        b=3
    elif name=="剪刀":
        b=4
    else:
        b="Error: No Correct Name"
    return b
    """
    将游戏对象对应到不同的整数
    """

def number_to_name(number):
    if number == 0:
        c = "石头"
    elif number == 1:
        c = "史波克"
    elif number == 2:
        c = "布"
    elif number == 3:
        c = "蜥蜴"
    else:
        c = "剪刀"
    return c
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """

def rpsls(player_choice,e):
    d=name_to_number(player_choice)
    f=number_to_name(e)
    print("您的选择是：%s\n计算机的选择是：%s"%(player_choice,f))
    if d==e:
        print("您和计算机出的一样呢")
    if d==0 :
        if e == 4 or e==3:
            print("您赢了！")
        if e == 1 or e==2:
            print("机器赢了！")
    elif d==1:
        if e == 0 or e==4:
            print("您赢了！")
        if e == 2 or e==3:
            print("机器赢了！")
    elif d==2:
        if e == 0 or e==1:
            print("您赢了")
        if e == 4 or e==3:
            print("机器赢了！")
    elif d==3:
        if e == 1 or e==2:
            print("您赢了")
        if e == 4 or e==0:
            print("机器赢了！")
    elif d==4:
        if e == 3 or e==2:
            print("您赢了")
        if e == 1 or e==0:
            print("机器赢了！")
    else:
        print(d)

    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

    """


    # 输出"-------- "进行分割
    # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice

    # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number

    # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number

    # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象

    # 在屏幕上显示计算机选择的随机对象

    # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果

    # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”

    #根据以上提示编写执行代码，代码完成后删除掉pass


# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name,a)

