#coding:utf-8
import re
from random import *


def shengchengpai(s):
    list_hua = []
    for x in range(3,14):
        list_hua.append((x,s))
    return list_hua
hongtao = shengchengpai('heitao')
heitao = shengchengpai('hongtao')
fangkuai = shengchengpai('ho_fangkuai')
hua = shengchengpai('ho_caohua')
pai = hongtao + heitao + fangkuai + hua
erb = ('er','heitao')
pai.append(erb)
ab = ('a','heitao')
pai.append(ab)
ac = ('a','fangkuai')
pai.append(ac)
ad = ('a','caohua')
pai.append(ad)
# print pai,len(pai)

#发牌
shuffle(pai)
# pai.sort()
# print pai
play1 = sorted(pai[:16])
play2 = sorted(pai[16:32])
play3 = sorted(pai[32:])
# print 'dipai is %s' %dipai
# print len(play1),len(play2),len(play3)
# print play1,len(play1)
# print 'play2 is %s' %play2
# print 'play3 is %s' %play3

Chu_De_Pai = []

#规则1，比大小
def BiDaXiao(a,b):
    if b > a:
        return b
# print play1[0],play2[0]
# bj = BiDaXiao(play1[0],play2[3])
# print bj


#规则2，单，对子，三带一，三带一对，炸，四带一，四带二
#通过list.count()函数判断一副牌的列表，只出现一次的就是单，出现2次是对子，依此类推。
#细分为以下几步：
#第一步，把每张牌的数字取出，形成新的列表1
#第二步，统计列表1里面的数字出现的次数，判断次数，1次==单，2次==对子，依此类推，把这些单/对子/三/等合并形成列表2
#第三步，因为第二步生成的列表2是只有数字没有花色的，所以现在把新的列表还原成play列表里带有花色的那种列表

def Find_Dan(play):
    list_Dan = []
    list_dan = []
    list_DDan = []
    for x in play:
        list_Dan.append(x[0])
    # print list_Dan
    for y in list_Dan:
        # print y
        # print list_Dan.count(y)
        if list_Dan.count(y) < 2:
            list_dan.append(y)
    for z in list_dan:
        # print z
        for t in play:
            if t[0] == z:
                list_DDan.append(t)
    return list_DDan



# print play1
# dan = Find_Dan(play1)
# print dan
#
# for x in dan:
#     # print x
#     play1.remove(x)
# print play1

def Find_DuiZi(play):
    list_Duizi = []
    list_Duizi2 = []
    list_duizi3 = []
    for x in play:
        list_Duizi.append(x[0])
    # print list_Duizi
    for y in list_Duizi:
        if list_Duizi.count(y) == 2:
            # print y
            list_Duizi2.append(y)
    # print list_Duizi2,len(list_Duizi2)
    for z in range(0,len(list_Duizi2),2):
        # print list_Duizi2[z]
        for t in play:
            # print z
            if t[0] == list_Duizi2[z]:
                list_duizi3.append(t)
    return list_duizi3


# print play1
# aa = Find_DuiZi(play1)
# print aa

def Find_San(play):
    list_san = []
    list_san2 = []
    list_san3 = []
    for x in play:
        list_san.append(x[0])
    # print list_san
    for y in list_san:
        if list_san.count(y) == 3:
            # print y
            list_san2.append(y)
    # print list_Duizi2,len(list_Duizi2)
    for z in range(0,len(list_san2),3):
        # print list_Duizi2[z]
        for t in play:
            # print z
            if t[0] == list_san2[z]:
                list_san3.append(t)
    return list_san3

# san = Find_San(play1)
# print san

def Find_Zha(play):
    list_zha = []
    list_zha2 = []
    list_zha3 = []
    for x in play:
        list_zha.append(x[0])
    # print list_zha
    for y in list_zha:
        if list_zha.count(y) == 4:
            # print y
            list_zha2.append(y)
    # print list_Duizi2,len(list_Duizi2)
    for z in range(0,len(list_zha2),4):
        # print list_Duizi2[z]
        for t in play:
            # print z
            if t[0] == list_zha2[z]:
                list_zha3.append(t)
    return list_zha3

# zha = Find_Zha(play1)
# print zha

##吃牌规则，针对单对子三等不同的出牌进行吃牌。

def ChiPai(Chu_De_pai,play):
    temp_list = []
    # print Chu_De_Pai[0][0]
    #len(Chu_De_pai) == 1 时代表 要吃的牌是 单牌
    if (len(Chu_De_Pai) == 1 ):
        temp_play = Find_Dan(play)
        # print temp_play
        if (len(temp_play) > 1):
            for i in temp_play:
                if i[0] > Chu_De_Pai[0][0]:
                    # print i
                    return i
                    play.remove(i)
                    break
                else:
                    temp_play = Find_Zha(play)
                    return temp_play
                    for x in temp_play:
                        play.remove(x)
        else:
            for i in play:
                if i[0] > Chu_De_Pai[0][0]:
                    return i
                    play.remove(i)
                    break
                else:
                    temp_play = Find_Zha(play)
                    return temp_play
                    for x in temp_play:
                        play.remove(x)




    #len(Chu_De_pai) == 2 时代表 要吃的牌是 对子
    elif (len(Chu_De_Pai) == 2):
        # print 2,Chu_De_Pai[0][0],len(Find_DuiZi(play)),Find_DuiZi(play)
        temp_list_duizi = Find_DuiZi(play)
        # print Chu_De_Pai[0][0],temp_list_duizi
        for x in range(0,len(temp_list_duizi),2):
            if (temp_list_duizi[x][0] > Chu_De_Pai[0][0]):
                temp_list.append(temp_list_duizi[x])
                temp_list.append(temp_list_duizi[x+1])
                return temp_list
                for x in temp_list:
                    play.remove(x)
                break



    elif (len(Chu_De_Pai) == 3):
        for t in Find_San(play):
            if t[0] > Chu_De_Pai:
                temp_list.append(t)
                temp_list.append(t+1)
                temp_list.append(t+2)
                return temp_list
                play.remove(temp_list)
                break
    else:
        for t in Find_Zha(play):
            if t[0] > Chu_De_Pai:
                temp_list.append(t)
                temp_list.append(t+1)
                temp_list.append(t+2)
                temp_list.append(t+3)
                return temp_list
                play.remove(temp_list)
                break

    # print 'pass chibuliao'



print play1
# print Find_DuiZi(play1)
Chu_De_Pai = [(3,'heitao'),(3,'hongtao')]
chi = ChiPai(Chu_De_Pai,play1)
you = Find_Zha(play1)
print you
print chi
print play1


#出牌规则

def ChuPai(Chu_De_Pai,play):
    play.remove(Chu_De_Pai)
    return play
# print play1
# play1 = ChuPai(play1[0],play1)
# print play1
# play1_duizi = Find_DuiZi(play1)
# print play1,play1_duizi


# print play1

# if (3,'heitao') in play1:
#     print 1
#     Chu_De_Pai = (3,'heitao')
#     play1 = ChuPai(Chu_De_Pai,play1)
#     print play1
# else:
#     print 'not heitao 3'
# print '你的牌是：',play1
# if (3,'heitao') in play1:
#     player_list = input ('黑桃三在你手上，请首先出牌(输入牌的序号)：').split()
#     print '你出的牌是：',play1[player-1]
#     print '现在轮到机器人2出牌'
#     print '机器人2出的牌是：',play[1]
# elif (3,'heitao') in play2:
#     print '黑桃三不在你手上，现在由机器人2首先出牌'
#     print '机器人2出的牌是：',play2[0]
# else:
#     print '黑桃三不在你的受伤，现在由机器人3首先出牌'
#     print '机器人3出的牌是：',play2[0]
#








##问题1、如何控制出牌方循环出牌

##问题2、出牌的时候，如何输入多个数字代表多个牌

##问题３、


























