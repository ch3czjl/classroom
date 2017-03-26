# with open('FaQiu_XiaoYouXi.py') as fin:
#     lines = fin.readlines()
#     print lines
#     # i = 0
#     # for line in lines:
#     #     print line
#     #     i += 1
#     #     filename = 'out_%d' %i
#     with open('filename.txt','w') as fout:
#             fout.writelines(lines)

# import os
# for i in range(1,13):
#     filename = 'out_%d' %i
#     print filename
#     os.remove(filename)
#
# try:
#     a = input('inputsomething:')
#     int(a)
# except:
#     print ValueError

# with open('output3.txt','w') as fout:
#     fout.write('niubi')
# with open('output3.txt') as fin:
#     output3 = fin.readlines()
#     print output3
#
# with open('output3.txt','a+') as fappend:
#     fappend.write('\nniniubi\nniteniubi')
# with open('output3.txt') as fin:
#     output3 = fin.readlines()
#     print output3

#
# # coding:utf-8
f = file('scores.txt')
lines = f.readlines()
print lines
f.close()

results = []

for line in lines:
   print line
   data = line.split()
   print data

   sum = 0
   for score in data[1:]:
       sum += int(score)
   result = '%s \t: %d\n' % (data[0], sum)
   print result

   results.append(result)

print results
output = file('result.txt', 'w')
output.writelines(results)
output.close()


