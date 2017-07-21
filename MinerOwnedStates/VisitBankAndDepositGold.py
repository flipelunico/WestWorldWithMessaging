from MinerOwnedStates import State
from location_type import location_type
from MinerOwnedStates import GoHomeAndSleepTilRested
from MinerOwnedStates import EnterMineAndDigForNugget


class VisitBankAndDepositGold(State.StateClass):
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if VisitBankAndDepositGold.__instance == None:
            VisitBankAndDepositGold()
        return VisitBankAndDepositGold.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if VisitBankAndDepositGold.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            VisitBankAndDepositGold.__instance = self

    def Enter(self, Miner):

        if (Miner.Location() != location_type.bank):
            Miner.ChangeLocation(location_type.bank)
            print("Goin' to the bank. Yes siree")

    def Execute(self, Miner):

        #deposit the gold
        Miner.AddToWealth(Miner.GoldCarried())
        Miner.SetGoldCarried(0)
        print ("Depositing gold. Total savings now: %d" % Miner.Wealth())

        #wealthy enough to have a well earned rest?
        if (Miner.Wealth() >= Miner.ComfortLevel):
            print ("WooHoo! Rich enough for now. Back home to mah li'lle lady")
            Miner.ChangeState(GoHomeAndSleepTilRested.GoHomeAndSleepTilRested.getInstance())
        else:
            #otherwise get more gold
            Miner.ChangeState(EnterMineAndDigForNugget.EnterMineAndDigForNugget.getInstance())

    def Exit(self, Miner):
        print("Leavin' the bank")
