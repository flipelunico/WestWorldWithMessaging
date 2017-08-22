from State import StateClass
from EntityNames import EntityNames


class StateMachine(object):
    m_pOwner = None
    m_pCurrentState = None
    # a record of the last state the agent was in
    m_pPreviousState = None
    # this is called every time the FSM is updated
    m_pGlobalState = None

    def __init__(self, owner):
        self.m_pOwner = owner
        self.m_pCurrentState = None
        self.m_pPreviousState = None
        self.m_pGlobalState = None

    def SetGlobalState(self, StateClass):
        self.m_pGlobalState = StateClass

    def SetCurrentState(self, StateClass):
        self.m_pCurrentState = StateClass

    def SetPreviousState(self, StateClass):
        self.m_pPreviousState = StateClass

    def Update(self):
        # if a global state exists, call its execute method, else do nothing
        if self.m_pGlobalState is not None:
            self.m_pGlobalState.Execute(self.m_pOwner)

        # same for the current state
        if self.m_pCurrentState is not None:
            self.m_pCurrentState.Execute(self.m_pOwner)

    def HandleMessage(self, Telegram):
        # first see if the current state is valid and that it can handle
        # the message
        if self.m_pCurrentState != None & self.m_pCurrentState.OnMessage(self.m_pOwner, Telegram):
            return True

        # if not, and if a global state has been implemented, send
        # the message to the global state
        if self.m_pGlobalState != None & self.m_pGlobalState.OnMessage(self.m_pOwner, Telegram):
            return True

        return False

    def ChangeState(self, StateClass):
        # keep a record of the previous state
        self.m_pPreviousState = self.m_pCurrentState

        # call the exit method of the existing state
        self.m_pCurrentState.Exit(self.m_pOwner)

        # change state to the new state
        self.m_pCurrentState = StateClass

        # call the entry method of the new state
        self.m_pCurrentState.Enter(self.m_pOwner)

    def RevertToPreviousState(self):
        self.ChangeState(self.m_pPreviousState)

    # returns true if the current state's type is equal to the type of the
    # class passed as a parameter.
    def isInState(self, State):
        return self.m_pCurrentState.__name__ == State.__name__
