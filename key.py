# -*- coding:GBK -*-
import os

def dirlist(key, path):
    all_info = os.walk(path)
    file_all_name = []
    keylist1 = []
    keylist2 = []
    for roots, dirs, files in all_info:
        for i in files:     #��ȡÿ���ļ�������������·��
            file_all_name.append(roots +'\\' + i)
    #print file_all_name
        
    for i in file_all_name:     #�����ļ����йؼ��ֵ��ļ�
        #print i
        if key in i:
            keylist1.append(i)
    try:
        for file in file_all_name:  #�����ļ������йؼ��ֵ��ļ�
            for line in open(file):
                if line == None:
                    break
                else:
                    if key in line:
                        keylist2.append(file)
    except Exception:
        print 'error'
    #print '�����ļ���%s' %file_all_name
    #print '�ļ�������%s���ļ���' %key
    print keylist1
    print '�ļ����������%s���ļ���' %key
    print keylist2


key = raw_input('����ؼ��֣�')
path = raw_input('�����ļ���·����')

dirlist(key, path)
