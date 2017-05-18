class JiangPai(object):

    def __init__(self,Guo,Jin,Yin,Tong):
        # print 'initing'

        self.Guo = Guo
        self.Jin = Jin
        self.Yin = Yin
        self.Tong = Tong
        # JiangPai = Jin + Yin + Tong
        # print '%s de jiangpaishu is:%d' % (Guo,JiangPai)

    def get_place(self,pai):
        if pai == 'Jin':
            self.Guo += 1
        elif pai == 'Yin':
            self.Yin += 1
        elif pai == 'Tong':
            self.Tong += 1
    @property
    def get_Jin(self):
        return self.Jin

    @property
    def get_count(self):
        sum_pai = self.Jin + self.Yin + self.Tong
        return sum_pai

    # sum_pai = get_count(self)
    def __str__(self):

        return 'guojia: %s\t\tJin: %d\tYin: %d\tTong: %d' % (self.Guo,self.Jin,self.Yin,self.Tong)

china = JiangPai('china',51,21,28)
meiguo = JiangPai('meiguo',36,38,36)
eluosi = JiangPai('eluosi',23,21,23)
english = JiangPai('english',19,13,15)
deguo = JiangPai('deguo',16,10,15)

print china
print meiguo
print eluosi
print english
print deguo

guojia_list = [china,english,deguo,eluosi,meiguo]

# print guojia_list

# j = JiangPai('china',0,0,0)
print '\n'
for i in guojia_list:
    print i
print '\n\n\n'
print ' yong jinpaishu pailie: '
guojia_list = sorted(guojia_list,key = lambda Guo: Guo.get_Jin,reverse = True)

print '\n'
for i in guojia_list:
    print i
print '\n'
print 'yong jiangpaishu pailie: '


guojia_list = sorted(guojia_list,key = lambda Guo: Guo.get_count,reverse = True)

print '\n'
for i in guojia_list:
    print i