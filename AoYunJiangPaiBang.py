class JiangPai(object):

    def __init__(self,Guo,Jin,Yin,Tong):
        print 'initing'

        self.Guo = Guo
        self.Jin = Jin
        self.Yin = Yin
        self.Tong = Tong
        JiangPai = Jin + Yin + Tong
        print '%s de jiangpaishu is:%d' % (Guo,JiangPai)

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

    def __str__(self):
        return 'guojia: %sttJin: %dt'

j = JiangPai('china',0,0,0)


