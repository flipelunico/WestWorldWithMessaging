import collections
from Messaging import Telegram


class PriorityQueue(object):

    sec = 0
    queue = collections.OrderedDict()

    def add(self,Telegram):
        self.sec += 1
        self.queue[self.sec] = Telegram


    def last(self):
        None
        #Determinar el valor mas alto