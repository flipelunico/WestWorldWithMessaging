import EntityNames


class BaseGameEntityClass:
    m_ID = 0
    m_iNextValidID = 0

    def __init__(self, Entitynames):
        SetID(Entityname.id)

    def SetID(val):
        m_ID = val
        m_iNextValidID = m_ID + 1

    def Update():
        null

    def ID():
        return m_ID