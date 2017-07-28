from BaseGameEntity import BaseGameEntityClass
from location_type import location_type
from MinersWifeOwnedStates.DoHouseWork import DoHouseWork
from MinersWifeOwnedStates.WifesGlobalState import WifesGlobalState
from StateMachine import StateMachine

class MinersWife(BaseGameEntityClass):
    m_Location = None
    #an instance of the state machine class
    m_pStateMachine = None

    def __init__(self, EntityNames):
        # super(EntityNames)
        global m_pCurrentState, m_Location, m_pStateMachine
        m_Location = location_type.shack
        m_pStateMachine = StateMachine(self)
        m_pStateMachine.SetCurrentState(DoHouseWork.getInstance())
        m_pStateMachine.SetGlobalState(WifesGlobalState.getInstance())

    def GetFSM(self):
        global m_pStateMachine
        return m_pStateMachine

    def RevertToPreviousState(self):
        None

    def Update(self):
        global m_pStateMachine
        m_pStateMachine.Update()

    def Location(self):
        global m_Location
        return m_Location

    def ChangeLocation(self, location_type):
        global m_Location
        m_Location = location_type
