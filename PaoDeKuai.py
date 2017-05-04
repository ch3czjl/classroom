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
erb = (16,'er,heitao')
pai.append(erb)
#为了让A 可以形成顺子，把A当成14
ab = (14,'A,heitao')
pai.append(ab)
ac = (14,'A,fangkuai')
pai.append(ac)
ad = (14,'A,caohua')
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



# #规则1，比大小
# def BiDaXiao(a,b):
#     if b > a:
#         return b
# # print play1[0],play2[0]
# # bj = BiDaXiao(play1[0],play2[3])
# # print bj


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

#顺子,我也不知道怎么搞的，就搞出顺子了。我其实并不知道自己的思路！反正就是一直不断调试，头晕不想回头研究怎么搞出来的。
#这里就不注释了大概是这样的。
#
def Find_Shunzi(play):
    list_shun1 = []
    list_shun2 = []
    list_shun3 = []
    list_shun4 = []
    list_shun5 = []
    # list_shun6 = []
    for x in play:
        # print x[0]
        list_shun1.append(x[0])
    list_shun1.sort(reverse=True)
    # print list_shun1
    for x in range(len(list_shun1)-1):
        # print x
        for y in range(len(list_shun1)-1):
            # print list_shun1
            # print list_shun1[x]
            # print type(list_shun1[x])
            if ((int(list_shun1[x]) - int(list_shun1[y])) == 1):
                if list_shun1[x] not in list_shun2:
                    list_shun2.append(list_shun1[x])
                if list_shun1[y] not in list_shun2:
                    list_shun2.append(list_shun1[y])
                continue
    for x in range(len(list_shun2)-1):
        if ((list_shun2[x]) - (list_shun2[x+1]) == 1):
            if list_shun2[x] not in list_shun3:
                    list_shun3.append(list_shun2[x])
            if list_shun2[x+1] not in list_shun3:
                list_shun3.append(list_shun2[x+1])
        else:
            break
    if (len(list_shun3) > 4):
        list_shun4 = list_shun3
    else:
        # print 'not shunzi'
        return
    list_shun4.sort(reverse=False)

    # print list_shun4
    #加入花色，去掉重复花色。乱！
    x = 0
    z = list_shun4[x]
    for k in play:
        if k[0] == z:
            list_shun5.append(k)
            z = z + 1
            x = x + 1
        if x > len(list_shun4):
            break
    return list_shun5

# shunzi = Find_Shunzi(play1)
# print shunzi

#连对
def Find_Liandui(play):
    temp_list = []
    list_duizi = Find_DuiZi(play)
    # print list_duizi,len(list_duizi)

    if (len(list_duizi) > 5):
        for x in range(0,len(list_duizi)-4,2):
            # print list_duizi[x][0],list_duizi[x+2][0],list_duizi[x+4][0]
            if ((list_duizi[x][0] - list_duizi[x+2][0]) == (list_duizi[x+2][0] - list_duizi[x+4][0]) == -1):
                temp_list.append(list_duizi[x])
                temp_list.append(list_duizi[x+1])
                temp_list.append(list_duizi[x+2])
                temp_list.append(list_duizi[x+3])
                temp_list.append(list_duizi[x+4])
                temp_list.append(list_duizi[x+5])
    if len(temp_list) == 0:
        return
    else:
        return temp_list

# liandui = Find_Liandui(play1)
# print liandui


list_feiji = []
#飞机
def Find_feiji(play):
    temp_san = Find_San(play)
    temp_list = []
    # print temp_san
    if (len(temp_san) > 3):
        for x in range(0,len(temp_san)-3,3):
            if ((temp_san[x][0]) - (temp_san[x+3][0]) == -1):
                temp_list.append(temp_san[x])
                temp_list.append(temp_san[x+1])
                temp_list.append(temp_san[x + 2])
                temp_list.append(temp_san[x + 3])
                temp_list.append(temp_san[x + 4])
                temp_list.append(temp_san[x + 5])
                return temp_list

# play4 = [(3,'hongtao'),(3,'heitao'),(3,'ho_fangkuai'),(4,'heitao'),(4,'hongtao'),(4,'ho_fangkuai'),(5,'heitao'),(6,'heitao')]
# feiji = Find_feiji(play4)
# print feiji


##吃牌规则，针对单对子三等不同的出牌进行吃牌。

def ChiPai(temp_list_chu,play):
    temp_list = []
    temp_zha = Find_Zha(play)
    if temp_zha:
        len_zha = len(temp_zha)
        # print 'youzha!'
    else:
        len_zha = 0
    if temp_list_chu:
        len_chudepai = len(temp_list_chu)
    else:
        len_chudepai = 0
    if (len_chudepai) == 0:
        return
    # print 'zha',temp_zha
    # print temp_list_chu[0][0]
    #len(temp_list_chu) == 1 时代表 要吃的牌是 单牌
    elif (len_chudepai == 1 ):
        #从单的列表中找一个大过的牌出
        temp_play = Find_Dan(play)
        # print temp_play
        if (len(temp_play) > 0):
            for i in temp_play:
                if i[0] > temp_list_chu[0][0]:
                    # print i
                    temp_list.append(i)
                    play.remove(i)
                    return temp_list

        #单牌列表里没有大过的，就从整副牌找个能大过的牌吃他
        for i in play:
            if i[0] > temp_list_chu[0][0]:
                play.remove(i)
                return i

        #单牌里也没能大过他，如果有炸，就炸他！
        if (len(temp_zha) != 0):
            # print 'youzha!!!'
            for x in temp_zha:
                play.remove(x)
                break
            return temp_zha
        else:
            return


    #len(temp_list_chu) == 2 时代表 要吃的牌是 对子
    elif (len_chudepai == 2):
        # print 2,temp_list_chu[0][0],len(Find_DuiZi(play)),Find_DuiZi(play)
        # print 'panduan chulai shi duizi'
        temp_list_duizi = Find_DuiZi(play)
        temp_list_San = Find_San(play)
        ##print 'duizi liebiao:',temp_list_duizi
        # print temp_list_chu[0][0],temp_list_duizi

        if (len(temp_list_duizi) != 0):
            for x in range(0,(len(temp_list_duizi)-2),2):
                temp_list_duizi_a = temp_list_duizi[x]
                # print temp_list_chu[0]
                # print temp_list_duizi_a

                if ((temp_list_duizi_a) > temp_list_chu[0]):
                    temp_list.append(temp_list_duizi[x])
                    temp_list.append(temp_list_duizi[x+1])
                    for x in temp_list:
                        play.remove(x)
                    return temp_list
        if (len(temp_list_San) != 0):
            for x in range(0,len(temp_list_San),3):
                if (temp_list_San[x][0] > temp_list_chu[0]):
                    temp_list.append(temp_list_San[x])
                    temp_list.append(temp_list_San[x+1])
                    print 'chai san',temp_list_San[x][0],temp_list_San[x+1][0]
                    for y in temp_list:
                        play.remove(y)
                    return temp_list
        if temp_zha:
            len_zha = len(temp_zha)
        else:
            len_zha = 0
        if ((len_zha) != 0):
            for x in temp_zha:
                play.remove(x)
            return temp_zha
        else:
            return



    ## 炸
    elif ((len_chudepai == 4) and (temp_list_chu[0][0] == temp_list_chu[1][0] == temp_list_chu[2][0] == temp_list_chu[3][0])):
        if (len(temp_zha) != 0):
            if ((temp_zha[0][0]) > (temp_list_chu[0][0])):
                for x in temp_zha:
                    play.remove(x)
                return temp_zha
            else:
                return
        else:
            return

    # #三带一
    elif (len_chudepai == 4) and (temp_list_chu[0][0] == temp_list_chu[1][0] == temp_list_chu[2][0] != temp_list_chu[3][0]):
        temp_list_San = Find_San(play)
        temp_dan = Find_Dan(play)
        if (len(temp_list_San) != 0):
            for x in range(0,len(temp_list_San),3):
                if (temp_list_San[x][0] > temp_list_chu[x][0]):
                    temp_list.append(temp_list_San[x])
                    temp_list.append(temp_list_San[x+1])
                    temp_list.append(temp_list_San[x+2])
                    temp_list.append(temp_dan[0])
                    for y in temp_list:
                        play.remove(y)
                    return temp_list
        elif (len(temp_zha) != 0):
            temp_list = temp_zha
            for x in temp_list:
                play.remove(x)
            return temp_list
        else:
            return
    #三带二
    elif (len_chudepai == 5) and (temp_list_chu[0][0] == temp_list_chu[1][0] == temp_list_chu[2][0] != temp_list_chu[3][0]):
        temp_list_San = Find_San(play)
        temp_duizi = Find_DuiZi(play)
        if (len(temp_list_San) != 0):
            for x in range(0,len(temp_list_San),3):
                if (temp_list_San[x][0] > temp_list_chu[x][0]):
                    temp_list.append(temp_list_San[x])
                    temp_list.append(temp_list_San[x+1])
                    temp_list.append(temp_list_San[x+2])
                    temp_list.append(temp_duizi[0])
                    temp_list.append(temp_duizi[1])
                    for y in temp_list:
                        play.remove(y)
                    return temp_list
        elif (len(temp_zha) != 0):
            temp_list = temp_zha
            for x in temp_list:
                play.remove(x)
            return temp_list
        else:
            return


    #四带二。四带二可以被炸吃。
    elif ((len_chudepai == 6) and (temp_list_chu[0][0] == temp_list_chu[1][0] == temp_list_chu[2][0] == temp_list_chu[3][0])):
        temp_dan = Find_Dan(play)
        print 'yunxing1'
        if((len(temp_zha) != 0) and (len(temp_dan) > 1)):
            print 'yunxing2'
            for x in range(0,len(temp_zha),4):
                if ((temp_zha[x][0]) > (temp_list_chu[0][0])):
                    print 'yunxing3'
                    temp_list.append(temp_zha[x])
                    temp_list.append(temp_zha[x+1])
                    temp_list.append(temp_zha[x+2])
                    temp_list.append(temp_zha[x+3])
                    temp_list.append(temp_dan[0])
                    temp_list.append(temp_dan[1])
                    for y in temp_list:
                        play.remove(y)
                    return temp_list

                #如果四带二不比他大，就直接炸他
                else:
                    print 'yunxing4'
                    temp_list.append(temp_zha[0])
                    temp_list.append(temp_zha[1])
                    temp_list.append(temp_zha[2])
                    temp_list.append(temp_zha[3])
                    for y in temp_list:
                            play.remove(y)
                    return temp_list

        #如果单牌不够，直接炸他
        elif((temp_zha != 0 ) and (len(temp_dan) <= 1)):
            print 'yunxing5'
            temp_list.append(temp_zha[0])
            temp_list.append(temp_zha[1])
            temp_list.append(temp_zha[2])
            temp_list.append(temp_zha[3])
            for y in temp_list:
                    play.remove(y)
            return temp_list
        else:
            return

    #四带两对子。四带两对子可以被炸吃。
    elif ((len_chudepai == 8) and (temp_list_chu[0][0] == temp_list_chu[1][0] == temp_list_chu[2][0] == temp_list_chu[3][0])):
        temp_duizi = Find_DuiZi(play)
        print 'yunxing1'
        if((len(temp_zha) != 0) and (len(temp_duizi) > 3)):
            print 'yunxing2'
            for x in range(0,len(temp_zha),4):
                if ((temp_zha[x][0]) > (temp_list_chu[0][0])):
                    print 'yunxing3'
                    temp_list.append(temp_zha[x])
                    temp_list.append(temp_zha[x+1])
                    temp_list.append(temp_zha[x+2])
                    temp_list.append(temp_zha[x+3])
                    temp_list.append(temp_duizi[0])
                    temp_list.append(temp_duizi[1])
                    temp_list.append(temp_duizi[2])
                    temp_list.append(temp_duizi[3])
                    for y in temp_list:
                        play.remove(y)
                    return temp_list

                #如果四带两对不比他大，就直接炸他
                else:
                    print 'yunxing4'
                    temp_list.append(temp_zha[0])
                    temp_list.append(temp_zha[1])
                    temp_list.append(temp_zha[2])
                    temp_list.append(temp_zha[3])
                    for y in temp_list:
                            play.remove(y)
                    return temp_list

        #如果对子不够，直接炸他
        elif((len(temp_zha) != 0 ) and (len(temp_duizi) <= 3)):
            print 'duizi bugou!'
            temp_list.append(temp_zha[0])
            temp_list.append(temp_zha[1])
            temp_list.append(temp_zha[2])
            temp_list.append(temp_zha[3])
            for y in temp_list:
                    play.remove(y)
            return temp_list
        else:
            return
    #顺子
    elif ((len_chudepai > 4) and ((temp_list_chu[0][0]) - (temp_list_chu[1][0]) == -1)):
        temp_shun = Find_Shunzi(play)
        # len_Chu = len(temp_list_chu)
        temp_list = []
        len_shun = 0
        if temp_shun:
            len_shun = len(temp_shun)
        else:
            len_shun = 0
        if (len_shun >= len_chudepai):
            for x in range(0,len(temp_shun)):
                if (((temp_shun[x][0]) > (temp_list_chu[0][0])) and ((len(temp_shun))-x+1) > len_chudepai):
                    for y in range(x,len_shun-1):
                        temp_list.append(temp_shun[y])

                    # print temp_list
                    for z in temp_list:
                        # print z
                        play.remove(z)
                    return temp_list
        elif (len(temp_zha) != 0):
            # print 'youzha!1'
            for t in temp_zha:
                play.remove(t)
            # print temp_zha
            return temp_zha
        else:
            return

    #连队
    elif ((len_chudepai > 5) and ((temp_list_chu[0][0]) - (temp_list_chu[2][0]) == -1)):
        temp_liandui = Find_Liandui(play)
        temp_list = []
        if temp_liandui:
            len_liandui = len(temp_liandui)
        else:
            len_liandui = 0
        if len_liandui:
            if ((temp_liandui[0][0]) > (temp_list_chu[0][0])):
                temp_list = temp_liandui
                # print temp_list
                # print play
                for x in temp_list:
                    # print x
                    play.remove(x)
                return temp_list
        elif len_zha:
            for x in temp_zha:
                play.remove(x)
            return temp_zha
        else:
            return

    #飞机带两个单
    elif ((len_chudepai == 8) and ((temp_list_chu[0][0]) - (temp_list_chu[3][0]) == -1)):
        temp_feiji = Find_feiji(play)
        temp_dan = Find_Dan(play)
        temp_list = []
        if temp_feiji:
            len_feiji = len(temp_feiji)
        else:
            len_feiji = 0
        if temp_dan:
            len_dan = len(temp_dan)
        else:
            len_dan = 0
        if ((len_feiji) and (len_dan > 1)):
            if ((temp_feiji[0][0]) > (temp_list_chu[0][0])):
                temp_list = temp_feiji
                temp_list.append(temp_dan[0])
                temp_list.append(temp_dan[1])
                # print temp_list
                # print play
                for x in temp_list:
                    # print x
                    play.remove(x)
                return temp_list
        elif len_zha:
            for x in temp_zha:
                play.remove(x)
            return temp_zha
        else:
            return

    #飞机带两对子
    elif ((len_chudepai == 10) and ((temp_list_chu[0][0]) - (temp_list_chu[3][0]) == -1)):
        temp_feiji = Find_feiji(play)
        temp_duizi = Find_DuiZi(play)
        temp_list = []
        if temp_feiji:
            len_feiji = len(temp_feiji)
        else:
            len_feiji = 0
        if temp_duizi:
            len_duizi = len(temp_duizi)
        else:
            len_duizi = 0
        if ((len_feiji) and (len_duizi > 1)):
            if ((temp_feiji[0][0]) > (temp_list_chu[0][0])):
                temp_list = temp_feiji
                temp_list.append(temp_duizi[0])
                temp_list.append(temp_duizi[1])
                temp_list.append(temp_duizi[2])
                temp_list.append(temp_duizi[3])
                # print temp_list
                # print play
                for x in temp_list:
                    # print x
                    play.remove(x)
                return temp_list
        elif len_zha:
            for x in temp_zha:
                play.remove(x)
            return temp_zha
        else:
            return


# 测试吃牌规则
# play5 = [(4,'heitao'),(4,'hongtao'),(4,'heitao'),(5,'heitao'),(5,'hongtao'),(5,'heitao'),(8,'heitao'),(8,'heitao'),(10,'heitao'),(10,'hongtao')]

# print play1
# print Find_DuiZi(play1)
# #调试吃牌
# # zha = Find_Zha(play1)
# # if zha:
# #     print 'youzha!',zha
# # else:
# #     print 'meiyouzha!'
# # print play5
# temp_list_chu = [(6,'heitao'),(6,'heitao')]
# chi = ChiPai(temp_list_chu,play5)
# print play5
# print chi
# # print play1


#出牌规则

def ChuPai(temp_list_chu,play):
    for x in temp_list_chu:
        play.remove(x)
    return play
# print play1
# play1 = ChuPai(play1[0],play1)
# print play1
# play1_duizi = Find_DuiZi(play1)
# print play1,play1_duizi


# print play1

# if (3,'heitao') in play1:
#     print 1
#     temp_list_chu = (3,'heitao')
#     play1 = ChuPai(temp_list_chu,play1)
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

#管不上以后随机出牌，或者首次出牌(本来想用random随机的，时间关系，先这样吧)
def Suiji_chupai(play):
    temp_list_chu = []
    temp_dan = Find_Dan(play)
    if temp_dan:
        len_dan = len(temp_dan)
    else:
        len_dan = 0
    temp_duizi = Find_DuiZi(play)
    if temp_duizi:
            len_duizi = len(temp_duizi)
    else:
        len_duizi = 0
    temp_san = Find_San(play)
    if temp_san:
        len_san = len(temp_san)
    else:
        len_san = 0
    temp_zha = Find_Zha(play)
    if temp_zha:
        len_zha = len(temp_zha)
    else:
        len_zha = 0
    temp_shun = Find_Shunzi(play)
    if temp_shun:
        len_shun = len(temp_shun)
    else:
        len_shun = 0
    temp_liandui = Find_Liandui(play)
    if temp_liandui:
        len_liandui = len(temp_liandui)
    else:
        len_liandui = 0
    temp_feiji = Find_feiji(play)
    if temp_feiji:
        len_feiji = len(temp_feiji)
    else:
        len_feiji = 0
    if (3,'heitao') in play:
        #时间紧急，先不考虑大于5张的顺子
        if ((len_shun) and ((3,'heitao') in temp_shun)):
            temp_list_chu.append(temp_shun[0])
            temp_list_chu.append(temp_shun[1])
            temp_list_chu.append(temp_shun[2])
            temp_list_chu.append(temp_shun[3])
            temp_list_chu.append(temp_shun[4])
            for x in temp_list_chu:
                play.remove(x)
            return temp_list_chu
        elif (3,'heitao') in temp_dan:
            temp_list_chu.append((3,'heitao'))
            for x in temp_list_chu:
                play.remove(x)
            return temp_list_chu
        elif (3,'heitao') in temp_duizi:
            if ((len_liandui) and ((3,'heitao') in temp_liandui)):
                temp_list_chu.append(temp_liandui[0])
                temp_list_chu.append(temp_liandui[1])
                temp_list_chu.append(temp_liandui[2])
                temp_list_chu.append(temp_liandui[3])
                temp_list_chu.append(temp_liandui[4])
                temp_list_chu.append(temp_liandui[5])
                for x in temp_list_chu:
                    play.remove(x)
                return temp_list_chu
            else:
                temp_list_chu.append(temp_duizi[0])
                temp_list_chu.append(temp_duizi[1])
                for x in temp_list_chu:
                    play.remove(x)
                return temp_list_chu
        elif (3,'heitao') in temp_san:
            if len_feiji:
                if (3,'heitao') in temp_feiji:
                    temp_list_chu.append(temp_san[0])
                    temp_list_chu.append(temp_san[1])
                    temp_list_chu.append(temp_san[2])
                    temp_list_chu.append(temp_san[3])
                    temp_list_chu.append(temp_san[4])
                    temp_list_chu.append(temp_san[5])
                    if len_dan > 1:
                        temp_list_chu.append(temp_dan[0])
                        temp_list_chu.append(temp_dan[1])
                        for x in temp_list_chu:
                            play.remove(x)
                        return temp_list_chu
                    elif len_duizi > 2:
                        temp_list_chu.append(temp_duizi[0])
                        temp_list_chu.append(temp_duizi[1])
                        temp_list_chu.append(temp_duizi[2])
                        temp_list_chu.append(temp_duizi[3])
                        for x in temp_list_chu:
                            play.remove(x)
                        return temp_list_chu
                else:
                    if (((3,'heitao') in temp_dan) and (len_dan > 1)):
                        temp_list_chu.append(temp_feiji[0])
                        temp_list_chu.append(temp_feiji[1])
                        temp_list_chu.append(temp_feiji[2])
                        temp_list_chu.append(temp_feiji[3])
                        temp_list_chu.append(temp_feiji[4])
                        temp_list_chu.append(temp_feiji[5])
                        temp_list_chu.append(temp_dan[0])
                        temp_list_chu.append(temp_dan[1])
                        for x in temp_list_chu:
                            play.remove(x)
                        return temp_list_chu
                    elif (((3,'heitao') in temp_duizi) and (len_duizi > 2)):
                        temp_list_chu.append(temp_feiji[0])
                        temp_list_chu.append(temp_feiji[1])
                        temp_list_chu.append(temp_feiji[2])
                        temp_list_chu.append(temp_feiji[3])
                        temp_list_chu.append(temp_feiji[4])
                        temp_list_chu.append(temp_feiji[5])
                        temp_list_chu.append(temp_duizi[0])
                        temp_list_chu.append(temp_duizi[1])
                        temp_list_chu.append(temp_duizi[2])
                        temp_list_chu.append(temp_duizi[3])
                        for x in temp_list_chu:
                            play.remove(x)
                        return temp_list_chu
            else:
                temp_list_chu.append(temp_san[0])
                temp_list_chu.append(temp_san[1])
                temp_list_chu.append(temp_san[2])
                if len_dan:
                    temp_list_chu.append(temp_dan[0])
                    for x in temp_list_chu:
                        play.remove(x)
                    return temp_list_chu
                elif len_duizi:
                    temp_list_chu.append(temp_duizi[0])
                    temp_list_chu.append(temp_duizi[1])
                    for x in temp_list_chu:
                        play.remove(x)
                    return temp_list_chu
        elif ((len_san) and ((3,'heitao') in temp_dan)):
            temp_list_chu.append(temp_san[0])
            temp_list_chu.append(temp_san[1])
            temp_list_chu.append(temp_san[2])
            temp_list_chu.append(temp_dan[0])
            for x in temp_list_chu:
                play.remove(x)
            return temp_list_chu
        elif((len_san) and ((3,'heitao') in temp_duizi)):
            temp_list_chu.append(temp_san[0])
            temp_list_chu.append(temp_san[1])
            temp_list_chu.append(temp_san[2])
            temp_list_chu.append(temp_duizi[0])
            temp_list_chu.append(temp_duizi[1])
            for x in temp_list_chu:
                play.remove(x)
            return temp_list_chu
        elif temp_zha:
            if (3,'heitao') in temp_zha:
                temp_list_chu.append(temp_zha[0])
                temp_list_chu.append(temp_zha[1])
                temp_list_chu.append(temp_zha[2])
                temp_list_chu.append(temp_zha[3])
                if len_dan > 1:
                    temp_list_chu.append(temp_dan[0])
                    temp_list_chu.append(temp_dan[1])
                    for x in temp_list_chu:
                        play.remove(x)
                    return temp_list_chu
                elif len_duizi > 2:
                    temp_list_chu.append(temp_duizi[0])
                    temp_list_chu.append(temp_duizi[1])
                    temp_list_chu.append(temp_duizi[2])
                    temp_list_chu.append(temp_duizi[3])
                    for x in temp_list_chu:
                        play.remove(x)
                    return temp_list_chu


    else:
        temp_list_chu = []
        if len_shun:
            temp_list_chu.append(temp_shun[0])
            temp_list_chu.append(temp_shun[1])
            temp_list_chu.append(temp_shun[2])
            temp_list_chu.append(temp_shun[3])
            temp_list_chu.append(temp_shun[4])
            for x in temp_list_chu:
                play.remove(x)
            return temp_list_chu
        elif len_san:
            if len_dan:
                temp_list_chu.append(temp_san[0])
                temp_list_chu.append(temp_san[1])
                temp_list_chu.append(temp_san[2])
                temp_list_chu.append(temp_dan[0])
                for x in temp_list_chu:
                    # print x
                    play.remove(x)
                return temp_list_chu
            elif len_duizi:
                temp_list_chu.append(temp_san[0])
                temp_list_chu.append(temp_san[1])
                temp_list_chu.append(temp_san[2])
                temp_list_chu.append(temp_duizi[0])
                temp_list_chu.append(temp_duizi[1])
                for x in temp_list_chu:
                    play.remove(x)
                return temp_list_chu
            else:
                for x in temp_list_chu:
                    play.remove(x)
                return temp_list_chu
        elif len_feiji:
            temp_list_chu.append(temp_feiji[0])
            temp_list_chu.append(temp_feiji[1])
            temp_list_chu.append(temp_feiji[2])
            temp_list_chu.append(temp_feiji[3])
            temp_list_chu.append(temp_feiji[4])
            temp_list_chu.append(temp_feiji[5])
            if len_dan > 1:
                temp_list_chu.append(temp_dan[0])
                temp_list_chu.append(temp_dan[1])
                for x in temp_list_chu:
                    play.remove(x)
                return temp_list_chu
            elif len_duizi > 2:
                temp_list_chu.append(temp_duizi[0])
                temp_list_chu.append(temp_duizi[1])
                temp_list_chu.append(temp_duizi[2])
                temp_list_chu.append(temp_duizi[3])
                for x in temp_list_chu:
                    play.remove(x)
                return temp_list_chu
            else:
                for x in temp_list_chu:
                    play.remove(x)
                return temp_list_chu
        elif len_zha:
            temp_list_chu.append(temp_zha[0])
            temp_list_chu.append(temp_zha[1])
            temp_list_chu.append(temp_zha[2])
            temp_list_chu.append(temp_zha[3])
            if len_dan > 1:
                temp_list_chu.append(temp_dan[0])
                temp_list_chu.append(temp_dan[1])
                for x in temp_list_chu:
                    play.remove(x)
                return temp_list_chu
            elif len_duizi > 2:
                temp_list_chu.append(temp_duizi[0])
                temp_list_chu.append(temp_duizi[1])
                temp_list_chu.append(temp_duizi[2])
                temp_list_chu.append(temp_duizi[3])
                for x in temp_list_chu:
                    play.remove(x)
                return temp_list_chu
            else:
                for x in temp_list_chu:
                    play.remove(x)
                return temp_list_chu
        elif len_dan:
            temp_list_chu.append(temp_dan[0])
            play.remove(temp_dan[0])
            return temp_list_chu
        elif len_duizi:
            if len_liandui:
                temp_list_chu.append(temp_liandui[0])
                temp_list_chu.append(temp_liandui[1])
                temp_list_chu.append(temp_liandui[2])
                temp_list_chu.append(temp_liandui[3])
                temp_list_chu.append(temp_liandui[4])
                temp_list_chu.append(temp_liandui[5])
                for x in temp_list_chu:
                    play.remove(x)
                return temp_list_chu
            else:
                temp_list_chu.append(temp_duizi[0])
                temp_list_chu.append(temp_duizi[1])
                for x in temp_list_chu:
                    play.remove(x)
                return temp_list_chu
#测试随机出牌

# print play1
#
# suiji = Suiji_chupai(play1)
#
# print suiji
# print play1


#出牌顺序循环

def Shunxu_chupai(play1,play2,play3):
    temp_list_chu = []
    if play1:
        len_play1 = len(play1)
    else:
        len_play1 = 0
    if play2:
        len_play2 = len(play2)
    else:
        len_play2 = 0
    if play3:
        len_play3 = len(play3)
    else:
        len_play3 = 0
    print play1
    print play2
    print play3

    if (3,'heitao') in (play1):
        while play1 or play2 or play3:
            temp_list_chu = Suiji_chupai(play1)
            print temp_list_chu
            temp_list_chu = ChiPai(temp_list_chu,play2)
            print temp_list_chu

            if len_Chudepai:
                temp_list_chu = ChiPai(temp_list_chu,play3)
            print temp_list_chu
    # elif(3,'heitao') in (play2):
    #     while play1 or play2 or play3:
    #         temp_list_chu = Suiji_chupai(play2)
    #         print temp_list_chu
    #         temp_list_chu = ChiPai(temp_list_chu,play3)
    #         print temp_list_chu
    #         temp_list_chu = ChiPai(temp_list_chu,play1)
    #         print temp_list_chu
    # else:
    #     while play1 or play2 or play3:
    #         temp_list_chu = Suiji_chupai(play3)
    #         print temp_list_chu
    #         temp_list_chu = ChiPai(temp_list_chu,play1)
    #         print temp_list_chu
    #         temp_list_chu = ChiPai(temp_list_chu,play2)
    #         print temp_list_chu






#测试顺序
# shunxu = Shunxu_chupai(play1,play2,play3)
# print shunxu
# print play1
# print play2
# print play3


# if play3:
#     len_play3 = len(play3)
# else:
#     len_play3 = 0




if (3,'heitao') in (play1):
    # print play1
    print play1
    print play2
    print play3

    chudepai1 = []
    chudepai2 = []
    chudepai3 = []

    chudepai1 = Suiji_chupai(play1)
    chudepai = chudepai1
    if chudepai:
        len_chudepai = len(chudepai)
    else:
        len_chudepai = 0
    print 'play1 have heitao3,play1 chu de pai:',chudepai1
    # print len(play1)
    if play1:
        len_play1 = len(play1)
    else:
        len_play1 = 0
    # print len_play1
    if play2:
        len_play2 = len(play2)
    else:
        len_play2 = 0
    if play3:
        len_play3 = len(play3)
    else:
        len_play3 = 0

    while (play1) and (play2) and (play3) and (chudepai):
        if chudepai == chudepai2:
            chudepai2 = Suiji_chupai(play2)
            chudepai = chudepai2
            print 'nimelia dou yaobuqi play2 chude pai is:',chudepai2
            # print chudepai,chudepai1,chudepai2,chudepai3
        else:
            chudepai2 = ChiPai(chudepai, play2)
            if chudepai2:
                print 'play2 chu de pai:', chudepai2
                chudepai = chudepai2
            else:
                print 'play2 yaobuqi'
        print 'play2 is:',play2



        if chudepai == chudepai3:
            chudepai3 = Suiji_chupai(play3)
            chudepai = chudepai3
            print 'nimelia dou yaobuqi play3 chude pai is:', chudepai3
            # print chudepai, chudepai1, chudepai2, chudepai3
        else:
            chudepai3 = ChiPai(chudepai, play3)
            if chudepai3:
                print 'play3 chu de pai:', chudepai3
                chudepai = chudepai3
            else:
                print 'play3 yaobuqi'
        print 'play3 is:',play3





        if chudepai == chudepai1:
            chudepai1 = Suiji_chupai(play1)
            chudepai = chudepai1
            print 'nimelia dou yaobuqi play1 chude pai is:', chudepai1
            # print chudepai,chudepai1,chudepai2,chudepai3
        else:
            chudepai1 = ChiPai(chudepai3, play1)
            if chudepai1:
                print 'play1 chu de pai:', chudepai1
                chudepai = chudepai1
            else:
                print 'play1 yaobuqi'
        print 'play1 is:',play1

    print len_play1,len_play2,len_play3
    print play1
    print play2
    print play3
    if len_play1 == 0:
        print 'winner is play1'
    elif len_play2 == 0:
        print 'winner is play2'
    else:
        print 'winner is play3'



        #
        # # print play2,len_play2
        #
        # chudepai3 = ChiPai(chudepai2,play3)
        #
        # if chudepai3:
        #     len_play3 == len(chudepai3)
        # else:
        #     len_play3 == 0
        # if len_play3 == 0:
        #     print 'play3 yaobuqi'
        #     chudepai3 = chudepai2
        #
        # else:
        #     print 'play3 chu de pai:',chudepai3
        #
        # if chudepai3 == chudepai1:
        #     chudepai1 = Suiji_chupai(play1)
        #     print 'nimalia dou yaobuqi ,play1 chu de pai is:'chudepai1
        # else:
        #     chudepai1 = ChiPai(chudepai3,play1)
        #     print 'play1 chu de pai is:',chudepai1

#

    #判断是不是自己刚刚出的那张牌（意思是刚刚出的那张牌，另外两个人都要不起）
        #不是刚刚那张拍
            # 判断能不能吃
                #能吃  吃
                #不能吃 输出要不起
        #是刚刚那张拍
            #随机出牌


        # print play1,len_play1

        # print 'play2 chu de pai:',chudepai
        # print play2
        # if play2:
        #     len_play2 = len(play2)
        # else:
        #     len_play2 = 0
        # print len_play2
        #
        # chudepai = ChiPai(chudepai,play3)
        # print 'play3 chu de pai:',chudepai
        # print play3
        # if play3:
        #     len_play3 = len(play3)
        # else:
        #     len_play3 = 0
        # print len_play3
        #
        # chudepai = ChiPai(chudepai,play1)
        # print 'play1 chu de pai:',chudepai
        # if play1:
        #     len_play1 = len(play1)
        # else:
        #     len_play1 = 0
        # print len_play1
    #     chudepai = ChiPai(chudepai,play3,play2)
    #     print 'play3 chu de pai:',chudepai
    #     print play3,len_play3
    #     chudepai = ChiPai(chudepai,play1,play3)
    #     print 'play1 chu de pai:',chudepai
    #     print play1,len_play1
    #
    # if len_play1 == 0:
    #     print 'play1 win'
    # if len_play2 == 0:
    #     print 'play2 win'
    # if len_play3 == 0:
    #     print 'play3 win'




##问题1、如何控制出牌方循环出牌

##问题2、出牌的时候，如何输入多个数字代表多个牌

##问题３、


























