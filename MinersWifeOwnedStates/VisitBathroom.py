from random import randint
import State

class VisitBathroom(State.StateClass):
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if VisitBathroom.__instance == None:
            VisitBathroom()
        return VisitBathroom.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if VisitBathroom.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            VisitBathroom.__instance = self

    def Enter(self, MinersWife):
        print("Wife : Walkin' to the can. Need to powda mah pretty li'lle nose")

    def Execute(self, MinersWife):
        print("Wife : Ahhhhhh! Sweet relief!")
        MinersWife.GetFSM().RevertToPreviousState()

    def Exit(self, MinersWife):
        print("Wife : Leavin' the Jon")
