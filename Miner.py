from BaseGameEntity import BaseGameEntityClass
from location_type import location_type
from MinerOwnedStates.GoHomeAndSleepTilRested import GoHomeAndSleepTilRested
from StateMachine import StateMachine


class Miner(BaseGameEntityClass):
    ComFortLevel = 5
    MaxNuggets = 3
    ThirstLevel = 5
    TirednessThreshold = 5

    m_Location = None

    m_iGoldCarried = None
    m_iMoneyInBank = None
    m_iThirst = None
    m_iFatigue = None

    ThirstLevel = 5
    TirednessThreshold = 5
    MaxNuggets = 3
    ComfortLevel = 5

    # an instance of the state machine class
    m_pStateMachine = None

    def __init__(self, EntityNames):
        # super(EntityNames)
        self.m_Location = location_type.shack
        self.m_iGoldCarried = 0
        self.m_iMoneyInBank = 0
        self.m_iThirst = 0
        self.m_iFatigue = 0
        self.m_pStateMachine = StateMachine(self)
        self.m_pStateMachine.SetCurrentState(GoHomeAndSleepTilRested.getInstance())

    def GetFSM(self):
        # global m_pStateMachine
        return self.m_pStateMachine

    def RevertToPreviousState(self):
        None

    def Update(self):
        # global m_iThirst, m_pStateMachine
        self.m_iThirst += 1
        self.m_pStateMachine.Update()

    def AddToGoldCarried(self, val):
        self.m_iGoldCarried += val

        if self.m_iGoldCarried < 0:
            self.m_iGoldCarried = 0

    def AddToWealth(self, val):
        self.m_iMoneyInBank += val

        if self.m_iMoneyInBank < 0:
            self.m_iMoneyInBank = 0

    def Thirsty(self):
        self.ThirstLevel = 5

        if self.m_iThirst >= self.ThirstLevel:
            return True
        else:
            return False

    def Fatigued(self):
        if self.m_iFatigue > 5:
            return True
        else:
            return False

    def Location(self):
        return self.m_Location

    def ChangeLocation(self, location_type):
        self.m_Location = location_type

    def IncreaseFatigue(self):
        self.m_iFatigue += 1

    def DecreaseFatigue(self):
        self.m_iFatigue -= 1

    def PocketsFull(self):
        self.MaxNuggets = 3
        if self.m_iGoldCarried >= self.MaxNuggets:
            return True
        else:
            return False

    def GoldCarried(self):
        return self.m_iGoldCarried

    def SetGoldCarried(self, val):
        self.m_iGoldCarried = val

    def Wealth(self):
        return self.m_iMoneyInBank

    def BuyAndDrinkAWhiskey(self):
        self.m_iThirst = 0
        self.m_iMoneyInBank -= 2
