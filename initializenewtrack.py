"""This file is used for creating and initializing a new track"""

import datetime

class NewTrack:
    """This Class has function to initialize the track
    """
    def __init__(self):
        self.max1 = 180
        self.max2 = 240
        self.mrngtime = datetime.datetime.strptime("9:00", '%H:%M')
        self.evngtime = datetime.datetime.strptime("1:00", '%H:%M')
        self.mrngsession = 0
        self.eveningsession = 0
        self.flag = 0
        self.data1 = []
        self.data2 = []
