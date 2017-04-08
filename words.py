import re
def words(filename):
    with open(filename,'r') as fin:
        lines = fin.readlines()
        # print lines,type(lines)
        lines_str = ','.join(lines)
        # print lines_str,type(lines_str)
        word_list = re.findall(r'\b\w+\b',lines_str)
        return 'there are %d words' %len(word_list)
filename = 'words.txt'
a = words(filename)
print a