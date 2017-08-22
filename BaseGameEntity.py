import EntityNames

class BaseGameEntity:
    m_ID = 0
    m_iNextValidID = 0

    def __init__(self, Entitynames):
        self.SetID(Entitynames.id)

    def SetID(self,val):
        self.m_ID = val
        self.m_iNextValidID = self.m_ID + 1

    @staticmethod
    def Update():
        None
    
    def getID(self):
        return self.m_ID