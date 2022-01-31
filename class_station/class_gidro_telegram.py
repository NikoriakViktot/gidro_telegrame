
from class_station.class_gidro_station import GidroStation


class GidroTelegame(GidroStation):

    def __init__(self):
        pass




class ReadReport:
    # def __init__(self, index):
    #     # self.date = date
    #     self.index = index

    def __get__(self, instance, owner):
        if self.index not in instance.__dict__:
            raise AttributeError(self)
        print('get')
        return instance.__dict__[self.index]

    def __set__(self, instance, value):
        print('set')
        print(value)
        data = value
        patern_1grup = re.compile('(1\d{4})')
        I_grup = [re.findall('(1\d{4})', str(i)) for i in data]

        instance.__dict__[self.index] = I_grup



d = GidroTelegame()

d.index= '42134'
print(d.__getattribute__('index'))

# print(d.__dict__['index'])
