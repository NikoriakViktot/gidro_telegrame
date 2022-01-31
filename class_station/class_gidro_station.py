
from class_station.class_station import Station


class GidroStation(Station):


    def __init__(self, index):
        print('classGidroStation')
        Station.__init__(self,index)




class GidroGauges(GidroStation):


    def __init__(self, date, time):
        self.time = time
        self.date = date



    @property








