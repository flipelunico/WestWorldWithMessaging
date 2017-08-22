class Telegram(object):
    # the entity that sent this telegram
    Sender = -1

    # the entity that is to receive this telegram
    Reciever = -1

    # the message itself. These are all enumerated in the file
    Msg = -1

    # messages can be dispatched immediately or delayed for a specified amount
    # of time. If a delay is necessary, this field is stamped with the time //the message should be dispatched.
    DispatchTime = -1

    #    ExtraInfo = None
    ExtraInfo = None

    # these telegrams will be stored in a priority queue. Therefore the >
    # operator needs to be overloaded so that the PQ can sort the telegrams
    # by time priority. Note how the times must be smaller than
    # SmallestDelay apart before two Telegrams are considered unique.
    SmallestDelay = 0.25

    def __init__(self):
        self.DispatchTime = -1
        self.Sender = -1
        self.Receiver = -1
        self.Msg = None

    def __init__(self, ptime, psender, preceiver, pmsg, pinfo):
        None

    def equals(self, Telegram):
        if ((self.DispatchTime - Telegram.DispatchTime) < self.SmallestDelay) & (self.Sender == Telegram.Sender) & (
                    self.Receiver == Telegram.Receiver) & (self.Msg == Telegram.Msg):
            salida = True
        else:
            salida = False

        return salida
