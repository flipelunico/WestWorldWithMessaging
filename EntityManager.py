import BaseGameEntity

class EntityManager(object):
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if EntityManager.__instance == None:
            EntityManager()
        return EntityManager.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if EntityManager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            EntityManager.__instance = self

    ###################################################################

    m_EntityMap = dict
    m_pid = 0

    def GetEntityFromID(self,pid):
         #find the entity
         #assert isinstance(pid,self.m_EntityMap)
         #print("Get Entity PID: ", pid)
         default = "Vacio"
         print(self.m_EntityMap.get(0, default))
         print(self.m_EntityMap.get(1, default))
         return self.m_EntityMap[pid]

    def RemoveEntity(self, pEntity):
        for pid, BaseGameEntity in self.m_EntityMap.items():
            if BaseGameEntity == pEntity:
                del dict[pid]

    def RegisterEntity(self, NewEntity):
        print("Registrando entidad con PID: ", self.m_pid)
        #self.m_EntityMap = {self.m_pid: NewEntity}
        self.m_EntityMap[self.m_pid] = NewEntity
        self.m_pid += 1