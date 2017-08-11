from random import randint
import State
from MinersWifeOwnedStates.VisitBathroom import VisitBathroom


class WifesGlobalState(State.StateClass):
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if WifesGlobalState.__instance == None:
            WifesGlobalState()
        return WifesGlobalState.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if WifesGlobalState.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            WifesGlobalState.__instance = self

    def Enter(self, MinersWife):
        None

    def Execute(self, MinersWife):
        if randint(1, 10) == 1:
            MinersWife.GetFSM().ChangeState(VisitBathroom.getInstance())

    def Exit(self, MinersWife):
        None
