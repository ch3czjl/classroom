##shengao = float(input('shengao:'))
##
##tizhong = float(input('tizhong:'))
##
##bmi = tizhong/(shengao*shengao)
##
##if bmi < 18.5:
##    print 'your bmi is %d,'%bmi
##    print 'your tizhong so qing'
##elif bmi >= 24:
##    print 'your bmi is %d,' %bmi
##    print 'your tizhong so zhong'
##else:
##    print 'your bmi is %d,' %bmi
##    print 'your tizhong is zhengchang'


##from random import *
##
##num = randint(1,100)
##
##print num

## �������һ��1~100֮�������
##import random
##
##num = random.randint(1,100)
##
##print num


# math ģ���е� pi ������Բ���ʦ�


# Բ�����ʽ S = �� * r * r
##from math import *
##
##r = 20
##
### ����뾶Ϊ r ��Բ���
##S = pi*r*r
##print S
##import random
##
##a = random.seed(2)
##print a

##
##import time  
##starttime = time.time()
##print 'start:%f' % starttime
##for i in range(10):
##    print i
##endtime = time.time()  
##print 'end:%f' % endtime
##print 'total time:%f' % (endtime-starttime)

##import time
##print 1
##time.sleep(3)
##print 2

##
##if inputnum != num:
##    while count < 5:
##        if inputnum < num:
##            print 'so small'
##            inputnum = int(input('please input:'))
##            count = count + 1
##        else:
##            print 'so big'
##            inputnum = int(input('please input:'))
##            count = count + 1
##    print 'count more than 5 ,you lose! please again!'
##    count = 1
##    inputnum = int(input('please input:'))
##     
##print 'bingo ,you use %d' %count
##inputnum = int(input('please input:'))

##num = randint(1,100)

##print num

##inputnum = int(input('please input:'))

##count = count + 1

##print inputnum

### coding:gbk
##from random import *
##
##count = 0
##
##lun = 0
#### �����ú����÷���
#### ������5�֣�ÿ��5�Σ�
##for x in range(1,6):  #5��
##    num = randint(1,100)
##    print num
##    inputnum = int(input('please input:'))
##    count = 1
##    if inputnum != num:
##        for x in range(1,6):
##            if inputnum < num:
##                print 'so small'
##                inputnum = int(input('please input:'))
##                count = count + 1
##            elif inputnum > num:
##                print 'so big'
##                inputnum = int(input('please input:'))
##                count = count + 1
##        print 'count more than 5 ,you lose! please again!'
##        count = 1
##        inputnum = int(input('please input:'))
##    else:
##        print 'bingo,you win!you use %d' %count
##        lun = count + lun
##        count =0
##        print 'please enter again!'
##ci = lun/5
##print 'ƽ����%d�β��У�' %ci
##
##
##
##    

##for x in range(1,6):  #5��
##    num = randint(1,100)
##    count = 0
##    lun = 0
##    print num
##    inputnum = int(input('please input:'))
##    count = count +1 
##    for x in range(1,6):
##
##            if inputnum < num:
##                print 'so small'
##                inputnum = int(input('please input:'))
##                count = count + 1
##            elif inputnum > num:
##                print 'so big'
##                inputnum = int(input('please input:'))
##                count = count + 1
##            else:
##                print 'bingo,you win!you use %d' %count
##                lun = count + lun
##                
##    print 'count more than 5 ,you lose! please again!'


 coding:gbk
from random import *
lun = 0
ci = 0

for x in range(1,6):
    num = randint(1,100)
    print num
    lun = lun + 1
    ci = ci + 1
    inputnum = int(input('��%d�ֵ�%d������:'%(lun,ci)))
    for y in range(1,6):
        if inputnum > num:
            print 'so big'
            inputnum = int(input('��%d�ֵ�%d������:'%(lun,ci)))
            ci = ci + 1
            break
##        elif inputnum < num:
##            pirnt 'so small'
##            break
        else:
            print 'bingo'
            break
        

        



























