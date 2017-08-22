from BaseGameEntity import BaseGameEntity
from location_type import location_type
from MinersWifeOwnedStates.DoHouseWork import DoHouseWork
from MinersWifeOwnedStates.WifesGlobalState import WifesGlobalState
from StateMachine import StateMachine


class MinersWife(BaseGameEntity):
    m_Location = None
    # an instance of the state machine class
    m_pStateMachine = None

    def __init__(self, EntityNames):
        # super(EntityNames)
        self.m_Location = location_type.shack
        self.m_pStateMachine = StateMachine(self)
        self.m_pStateMachine.SetCurrentState(DoHouseWork.getInstance())
        self.m_pStateMachine.SetGlobalState(WifesGlobalState.getInstance())

    def GetFSM(self):
        return self.m_pStateMachine

    def RevertToPreviousState(self):
        None

    def Update(self):
        self.m_pStateMachine.Update()

    def Location(self):
        return self.m_Location

    def ChangeLocation(self, location_type):
        self.m_Location = location_type
