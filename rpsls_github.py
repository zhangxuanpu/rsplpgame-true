#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
���ڣ�2019/11/16
"""

import random
a=random.randint(0,4)
# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����
# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    if name=="ʯͷ":
        b=0
    elif name=="ʷ����":
        b=1
    elif name=="��":
        b=2
    elif name=="����":
        b=3
    elif name=="����":
        b=4
    else:
        b="Error: No Correct Name"
    return b
    """
    ����Ϸ�����Ӧ����ͬ������
    """

def number_to_name(number):
    if number == 0:
        c = "ʯͷ"
    elif number == 1:
        c = "ʷ����"
    elif number == 2:
        c = "��"
    elif number == 3:
        c = "����"
    else:
        c = "����"
    return c
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """

def rpsls(player_choice,e):
    d=name_to_number(player_choice)
    f=number_to_name(e)
    print("����ѡ���ǣ�%s\n�������ѡ���ǣ�%s"%(player_choice,f))
    if d==e:
        print("���ͼ��������һ����")
    if d==0 :
        if e == 4 or e==3:
            print("��Ӯ�ˣ�")
        if e == 1 or e==2:
            print("����Ӯ�ˣ�")
    elif d==1:
        if e == 0 or e==4:
            print("��Ӯ�ˣ�")
        if e == 2 or e==3:
            print("����Ӯ�ˣ�")
    elif d==2:
        if e == 0 or e==1:
            print("��Ӯ��")
        if e == 4 or e==3:
            print("����Ӯ�ˣ�")
    elif d==3:
        if e == 1 or e==2:
            print("��Ӯ��")
        if e == 4 or e==0:
            print("����Ӯ�ˣ�")
    elif d==4:
        if e == 3 or e==2:
            print("��Ӯ��")
        if e == 1 or e==0:
            print("����Ӯ�ˣ�")
    else:
        print(d)

    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """


    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

    #����������ʾ��дִ�д��룬������ɺ�ɾ����pass


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name,a)

