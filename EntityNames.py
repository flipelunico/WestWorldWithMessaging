from enum import Enum

class EntityNames(Enum):

    ent_Miner_Bob = 0
    ent_Elsa = 1

    m_ID = 0

    def __init__(self, pID):
        m_ID = pID

    def GetNameOfEntity(n):
        print("Valor de entidad: ",n)
        if (n == 0):
            return "Miner Bob"
        elif (n == 1):
            return "ELSA"
        else:
            return "UNKNOWN!"
        
