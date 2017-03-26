# inputstr = raw_input('inputplease:')
# list_input = inputstr.split()
# strlong = len(list_input)
#
# with open('PingBiCi.txt','r') as f:
#     list_1 = f.read().split()
#     # print str1
# for x in list_1:
#     for y in range(strlong):
#         if list_input[y] == x:
#             list_input[y] = '*'
# new_input = ','.join(list_input)
# print new_input

inputstr = raw_input('inputplease:')
list_input = inputstr.split()
strlong = len(list_input)

def PingBi(file = ''):
    global list_1
    with open(file,'r') as f:
        list_1 = f.read().split()
    return list_1
inputPingbi = raw_input('inputfile:')
a = PingBi(inputPingbi)
print a
for x in list_1:
    for y in range(strlong):
        if list_input[y] == x:
            list_input[y] = '*'
new_input = ','.join(list_input)
print new_input