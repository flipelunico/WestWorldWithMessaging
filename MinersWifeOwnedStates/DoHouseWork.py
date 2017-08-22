from random import randint
from colorama import init
from colorama import Fore, Back, Style
import State

# Init para colorama
init()


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
            print(Fore.RED + "Wife : Moppin' the floor")
        elif r == 1:
            print(Fore.RED + "Wife : Washin' the dishes")
        elif r == 3:
            print(Fore.RED + "Wife : Makin' the bed")

        #print(Style.RESET_ALL)

    def Exit(self, MinersWife):
        None
