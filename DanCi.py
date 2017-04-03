import re

with open('from.txt','r') as fin:
    lines = fin.readlines()
##    print lines,type(lines)
    lines_str = ''.join(lines)
##    print lines_str,type(lines_str)
    pattern = r'[A-z]+'

    result = re.findall(pattern,lines_str)
##    print result
    result.sort()
##    print result,type(result)
    r_list = '\n'.join(result)
##    print r_list,type(r_list)

with open ('to.txt','w') as fout:
    fout.write(r_list)
