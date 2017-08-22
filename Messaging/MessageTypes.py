from enum import Enum


class MessageTypes(Enum):
    Msg_HiHoneyImHome = 0
    Msg_StewReady = 1
    m_id = None

    def __init__(self, pid):
        self.m_id = pid

    def toString(self):
        return self.MsgToStr(self.m_id)

    def MsgToStr(self, MessageTypes):
        return self.MsgToStr(MessageTypes.m_id)

    def MsgToStr(msg):
        if msg == 0:
            return "HiHoneyImHome"
        elif msg == 1:
            return "StewReady"
        else:
            return "Not recognized!"
