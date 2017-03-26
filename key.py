# -*- coding:GBK -*-
import os

def dirlist(key, path):
    all_info = os.walk(path)
    file_all_name = []
    keylist1 = []
    keylist2 = []
    for roots, dirs, files in all_info:
        for i in files:     #获取每个文件的名，及完整路径
            file_all_name.append(roots +'\\' + i)
    #print file_all_name
        
    for i in file_all_name:     #处理文件名有关键字的文件
        #print i
        if key in i:
            keylist1.append(i)
    try:
        for file in file_all_name:  #处理文件内容有关键字的文件
            for line in open(file):
                if line == None:
                    break
                else:
                    if key in line:
                        keylist2.append(file)
    except Exception:
        print 'error'
    #print '所有文件：%s' %file_all_name
    #print '文件名包含%s的文件：' %key
    print keylist1
    print '文件内容里包含%s的文件：' %key
    print keylist2


key = raw_input('输入关键字：')
path = raw_input('输入文件夹路径：')

dirlist(key, path)
