import State
# from MinerOwnedStates import GoHomeAndSleepTilRested
from MinerOwnedStates.EnterMineAndDigForNugget import EnterMineAndDigForNugget
from location_type import location_type


class GoHomeAndSleepTilRested(State.StateClass):
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if GoHomeAndSleepTilRested.__instance == None:
            GoHomeAndSleepTilRested()
        return GoHomeAndSleepTilRested.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if GoHomeAndSleepTilRested.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            GoHomeAndSleepTilRested.__instance = self

    def Enter(self, Miner):

        if (Miner.Location() != location_type.shack):
            Miner.ChangeLocation(location_type.shack)
            print("Walkin' home")

    def Execute(self, Miner):

        #if miner is not fatigued start to dig for nuggets again.

        if (Miner.Fatigued()):
            # sleep
            Miner.DecreaseFatigue()
            print("ZZZZ... ")
        else:
            print("What a God darn fantastic nap! Time to find more gold")
            Miner.GetFSM().ChangeState(EnterMineAndDigForNugget.getInstance())

    def Exit(self, Miner):
        print("Leaving the house")
