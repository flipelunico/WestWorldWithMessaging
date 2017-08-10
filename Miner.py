from BaseGameEntity import BaseGameEntityClass
import EntityNames
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

    #an instance of the state machine class
    m_pStateMachine = None

    def __init__(self, EntityNames):
        # super(EntityNames)
        global m_Location, m_iGoldCarried, m_iMoneyInBank, m_iThirst, m_iFatigue
        m_Location = location_type.shack
        m_iGoldCarried = 0
        m_iMoneyInBank = 0
        m_iThirst = 0
        m_iFatigue = 0
        global m_pStateMachine
        m_pStateMachine = StateMachine(self)
        print("Statemachine para miner: ", m_pStateMachine)
        m_pStateMachine.SetCurrentState(GoHomeAndSleepTilRested.getInstance()) 

    def GetFSM(self):
        global m_pStateMachine
        return m_pStateMachine

    def RevertToPreviousState(self):
        None

    def Update(self):
        global m_iThirst, m_pStateMachine
        m_iThirst += 1
        print("Llamando a Update StateMachine Instancia: ", m_pStateMachine)
        m_pStateMachine.Update()

    def AddToGoldCarried(self, val):
        global m_iGoldCarried
        m_iGoldCarried += val

        if (m_iGoldCarried < 0):
            m_iGoldCarried = 0

    def AddToWealth(self, val):
        global m_iMoneyInBank
        m_iMoneyInBank += val

        if (m_iMoneyInBank < 0):
            m_iMoneyInBank = 0

    def Thirsty(self):
        global m_iThirst
        global ThirstLevel
        ThirstLevel = 5

        if (m_iThirst >= ThirstLevel):
            return True
        else:
            return False

    def Fatigued(self):
        global m_iFatigue, TirednessThreshold

        if (m_iFatigue > 5):
            return True
        else:
            return False

    def Location(self):
        global m_Location
        return m_Location

    def ChangeLocation(self, location_type):
        global m_Location
        m_Location = location_type

    def IncreaseFatigue(self):
        global m_iFatigue
        m_iFatigue += 1

    def DecreaseFatigue(self):
        global m_iFatigue
        m_iFatigue -= 1

    def PocketsFull(self):
        global m_iGoldCarried, MaxNuggets
        MaxNuggets = 3
        if (m_iGoldCarried >= MaxNuggets):
            return True
        else:
            return False

    def GoldCarried(self):
        global m_iGoldCarried
        return m_iGoldCarried

    def SetGoldCarried(self, val):
        global m_iGoldCarried
        m_iGoldCarried = val

    def Wealth(self):
        global m_iMoneyInBank
        return m_iMoneyInBank

    def BuyAndDrinkAWhiskey(self):
        global m_iThirst, m_iMoneyInBank
        m_iThirst = 0
        m_iMoneyInBank -= 2