from State import StateClass

class StateMachine:

    m_pOwner = None

    m_pCurrentState = None
    #a record of the last state the agent was in
    m_pPreviousState = None
    #this is called every time the FSM is updated
    m_pGlobalState = None

    def __init__(self,owner):
        global  m_pOwner,m_pCurrentState,m_pPreviousState,m_pGlobalState

        m_pOwner = owner
        m_pCurrentState = None
        m_pPreviousState = None
        m_pGlobalState = None

    def SetGlobalState(self,StateClass):
        global  m_pGlobalState
        m_pGlobalState = StateClass

    def SetCurrentState(self, StateClass):
        global m_pCurrentState
        m_pCurrentState = StateClass

    def SetPreviousState(self,StateClass):
        global m_pPreviousState
        m_pPreviousState = StateClass

    def Update(self):
        global m_pGlobalState,m_pCurrentState

        #if a global state exists, call its execute method, else do nothing
        if (m_pGlobalState != None):
            m_pGlobalState.Execute(m_pOwner)

        #same for the current state
        if (m_pCurrentState != None):
            m_pCurrentState.Execute(m_pOwner)

    def ChangeState(self,StateClass):
        global m_pPreviousState, m_pCurrentState

        #keep a record of the previous state
        m_pPreviousState = m_pCurrentState

        #call the exit method of the existing state
        m_pCurrentState.Exit(m_pOwner)

        #change state to the new state
        m_pCurrentState = StateClass

        #call the entry method of the new state
        m_pCurrentState.Enter(m_pOwner)

    def RevertToPreviousState(self):
        global m_pPreviousState
        self.ChangeState(m_pPreviousState)

    #returns true if the current state's type is equal to the type of the
    #class passed as a parameter.
    def isInState(State):
        #System.out.println(m_pCurrentState.getClass())
        return m_pCurrentState.__name__ == State.__name__



