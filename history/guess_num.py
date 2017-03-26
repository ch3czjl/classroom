# coding gbk

from random import *
lun = 0
again = 1
pingjun = 0
ci = 0
count = 0

## again 判断用户是否继续。
while again:

    ## lun 记录用户进行的轮次数
    ## count 记录用户猜的次数
    num = randint(1,10)
    lun = lun + 1
    ## 下一轮开始的时候count5次的
    count = 0
    print num


    ## for循环限制用户只能每轮最多猜5次    
    for x in range(1,6):

        count = count + 1
        ## ci 记录用户用了几次猜中
        ci = ci + 1
        print '总次数是%d' %ci
        inputnum = int(input('（现在是第%d轮！您有5次机会！这是第%d次！）请输入数字：'%(lun,count)))
            

        ## if循环判断用户竞猜结果
        if inputnum > num:
            print 'so big'
        elif inputnum < num:
            print 'so small'
        else:
            print '恭喜，您猜对了，用时%d次' %count
            again = int(input('是否继续？是请按1，否请按0：'))
            if again:
                break

        ## 下面这个if循环用来让用户选择是否继续猜            
        again = int(input('是否继续？是请按1，否请按0：'))
        if again:
            continue
        else:
            break

##游戏结束后，统计用户的竞猜数据
print 'lun:%d' %lun
print 'ci:%d' %ci
pingjun = float(ci)/lun
print '感谢参与！您一共进行了%d轮，平均每轮用%f次猜中！' %(lun,pingjun)
