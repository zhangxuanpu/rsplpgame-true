#coding:gbk
#�����ϵ���ӻ�
#������

import codecs
import jieba.posseg as pseg
import jieba

names = {}
relationships = {}
lineNames = []

with codecs.open("limingpoxiaodejiedao.txt", 'r', 'gbk') as f:
    for line in f.readlines():
        poss = pseg.cut(line)
        lineNames.append([])
        for w in poss:
            if w.flag != 'nr' or len(w.word) < 2:
                continue  # ���ִʳ���С��2��ôʴ��Բ�Ϊnr��������ʱ��Ϊ�ôʲ�Ϊ����
            lineNames[-1].append(w.word)  # Ϊ��ǰ�εĻ�������һ������
            if names.get(w.word) is None:
                names[w.word] = 0
                relationships[w.word] = {}
            names[w.word] += 1

for line in lineNames:
    for name1 in line:
        for name2 in line:
            if name1 == name2:
                continue
            if relationships[name1].get(name2) is None:
                relationships[name1][name2] = 1
            else:
                relationships[name1][name2] = relationships[name1][name2] + 1

with codecs.open("People_node.txt", "w", "gbk") as f:
    f.write("ID Label Weight\r\n")
    for name, times in names.items():
        if times > 10:
            f.write(name + " " + name + " " + str(times) + "\r\n")



with codecs.open("People_edge.txt", "w", "gbk") as f:
    f.write("Source Target Weight\r\n")
    for name, edges in relationships.items():
        for v, w in edges.items():
            if w > 10:
                f.write(name + " " + v + " " + str(w) + "\r\n")