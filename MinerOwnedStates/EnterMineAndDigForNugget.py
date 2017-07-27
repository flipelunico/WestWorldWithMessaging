import State
from MinerOwnedStates import EnterMineAndDigForNugget
from MinerOwnedStates import QuenchThirst
from MinerOwnedStates.VisitBankAndDepositGold import VisitBankAndDepositGold
from location_type import location_type


class EnterMineAndDigForNugget(State.StateClass):
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if EnterMineAndDigForNugget.__instance == None:
            EnterMineAndDigForNugget()
        return EnterMineAndDigForNugget.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if EnterMineAndDigForNugget.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            EnterMineAndDigForNugget.__instance = self

    def Enter(self, Miner):

        if (Miner.Location() != location_type.goldmine):
            Miner.ChangeLocation(location_type.goldmine)
            print("Walkin' to the goldmine")

    def Execute(self, Miner):

        #the miner digs for gold until he is carrying in excess of MaxNuggets.
        #If he gets thirsty during his digging he packs up work for a while and
        #changes state to go to the saloon for a whiskey.

        Miner.AddToGoldCarried(1)

        Miner.IncreaseFatigue()

        print ("Pickin' up a nugget")

        #if enough gold mined, go and put it in the bank
        if (Miner.PocketsFull()):
            Miner.GetFSM().ChangeState(VisitBankAndDepositGold.getInstance())


        if (Miner.Thirsty()):
            Miner.GetFSM().ChangeState(QuenchThirst.QuenchThirst.getInstance())


    def Exit(self, Miner):
        print("Ah'm leavin' the goldmine with mah pockets full o' sweet gold")
