#coding:utf-8
## 求列表和、平均
def sum_list(l_list):
    sum_list = 0
    for i in range(1,len(l_list)):
        sum_list = float(l_list[i]) + sum_list
    return '%.1f' %sum_list
def avg_list(sum_list,l_list):
    avg_list = float(sum_list)/(len(l_list))
    return '%.1f' %avg_list

with open('report.txt','r') as fin:
    line_fin = fin.readlines()
##    print line_fin
    
##    print type(line_new)
    avg_kemu = []

    for l in range(1,12):
        line_ke = []
        line_new = []
    
        for line in line_fin:
    ##        print type(line)
            line_list = line.split()
    ##        print line_list[1:]
            sum_one = sum_list(line_list[1:])
    ##        print sum_one
            avg_one = avg_list(sum_one,line_list[1:])
    ##        print avg_one
            line_list.append(sum_one)
            line_list.append(avg_one)
            line_new.append(line_list)
            
    ##        print len(line_list[1:])
            line_ke.append(line_list[l])
        
        sum_ke = sum_list(line_ke)
        avg_ke = avg_list(sum_ke,line_ke)
        avg_kemu.append(avg_ke)
##    print avg_kemu
    line_new_sort =sorted(line_new,key=lambda x:float(x[-1]),reverse=True)
##    print line_new_sort
    for k in range(1,len(line_new_sort)+1):
        line_new_sort[k-1].insert(0,str(k))
##    print line_new_sort
    first_line = ['名次','语文','数学','英语','物理','化学','生物','政治','历史','地理','总分','平均分']
    second_line =['0','平均']
    for m in range(len(avg_kemu)):
        second_line.append(avg_kemu[m])
##    print second_line
    line_new_sort.insert(0,second_line)
    line_new_sort.insert(0,first_line)
    # print line_new_sort[11]
##    line_new_sort_str = ','.join(line_new_sort)
##    print line_new_sort_str
    for ls in line_new_sort[1:]:
        # print ls[2:]
        for lss in range(2,13):
            # print ls[lss]
            if float(ls[lss]) < 60 :
                ls[lss] = '不及格'


    with open('report_new.txt','w') as fout:
        for t in line_new_sort:
            str1 = '\t'.join(t)
            fout.write(str1)
            fout.write('\n')

        
        
        
        
