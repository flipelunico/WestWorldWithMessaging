import State
from MinerOwnedStates import EnterMineAndDigForNugget
from location_type import location_type


class QuenchThirst(State.StateClass):
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if QuenchThirst.__instance == None:
            QuenchThirst()
        return QuenchThirst.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if QuenchThirst.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            QuenchThirst.__instance = self

    def Enter(self, Miner):

        if (Miner.Location() != location_type.saloon):
            Miner.ChangeLocation(location_type.saloon)
            print("Boy, ah sure is thusty! Walking to the saloon")

    def Execute(self, Miner):

        if (Miner.Thirsty()):

            Miner.BuyAndDrinkAWhiskey()
            print("That's mighty fine sippin liquer")

            Miner.ChangeState(EnterMineAndDigForNugget.EnterMineAndDigForNugget.getInstance());
        else:
            print("\nERROR!\nERROR!\nERROR!")

    def Exit(self, Miner):
        print("Leaving the saloon, feelin' good")
