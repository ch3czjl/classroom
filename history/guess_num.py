# coding gbk

from random import *
lun = 0
again = 1
pingjun = 0
ci = 0
count = 0

## again �ж��û��Ƿ������
while again:

    ## lun ��¼�û����е��ִ���
    ## count ��¼�û��µĴ���
    num = randint(1,10)
    lun = lun + 1
    ## ��һ�ֿ�ʼ��ʱ��count5�ε�
    count = 0
    print num


    ## forѭ�������û�ֻ��ÿ������5��    
    for x in range(1,6):

        count = count + 1
        ## ci ��¼�û����˼��β���
        ci = ci + 1
        print '�ܴ�����%d' %ci
        inputnum = int(input('�������ǵ�%d�֣�����5�λ��ᣡ���ǵ�%d�Σ������������֣�'%(lun,count)))
            

        ## ifѭ���ж��û����½��
        if inputnum > num:
            print 'so big'
        elif inputnum < num:
            print 'so small'
        else:
            print '��ϲ�����¶��ˣ���ʱ%d��' %count
            again = int(input('�Ƿ���������밴1�����밴0��'))
            if again:
                break

        ## �������ifѭ���������û�ѡ���Ƿ������            
        again = int(input('�Ƿ���������밴1�����밴0��'))
        if again:
            continue
        else:
            break

##��Ϸ������ͳ���û��ľ�������
print 'lun:%d' %lun
print 'ci:%d' %ci
pingjun = float(ci)/lun
print '��л���룡��һ��������%d�֣�ƽ��ÿ����%f�β��У�' %(lun,pingjun)
