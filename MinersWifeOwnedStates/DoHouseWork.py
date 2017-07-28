from random import randint
import State

class DoHouseWork(State.StateClass):
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if DoHouseWork.__instance == None:
            DoHouseWork()
        return DoHouseWork.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if DoHouseWork.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            DoHouseWork.__instance = self

    def Enter(self, MinersWife):
        None

    def Execute(self, MinersWife):

        r = randint(0, 9)

        if r == 0:
            print("Wife : Moppin' the floor")
        elif r == 1:
            print("Wife : Washin' the dishes")
        elif r == 3:
            print("Wife : Makin' the bed")


    def Exit(self, MinersWife):
        None
