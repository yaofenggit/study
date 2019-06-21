#定义有两个类的库文件
class class_ywh:
    def __init__(self, units_from, units_to, factor):
        self.units_from = units_from
        self.units_to = units_to
        self.factor = factor

    def description(self):
        return self.units_from + ' 转换为 ' + self.units_to

    def convert(self, value):
        return value * self.factor

class class_ywh1(class_ywh):
    def __init__(self, units_from, units_to, factor, offset):
        class_ywh.__init__(self, units_from, units_to, factor)
        self.offset = offset

    def convert(self, value):
        return value * self.factor + self.offset