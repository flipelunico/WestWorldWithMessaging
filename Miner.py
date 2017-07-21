from BaseGameEntity import BaseGameEntityClass
import EntityNames
import location_type
from MinerOwnedStates.GoHomeAndSleepTilRested import GoHomeAndSleepTilRested


class Miner(BaseGameEntityClass):
    ComFortLevel = 5
    MaxNuggets = 3
    ThirstLevel = 5
    TirednessThreshold = 5

    m_pCurrentState = None
    m_Location = None

    m_iGoldCarried = None
    m_iMoneyInBank = None
    m_iThirst = None
    m_iFatigue = None

    def __init__(self, EntityNames):
        # super(EntityNames)
        # m_Location = location_typeclass.shack
        m_Location = 0
        m_iGoldCarried = 0
        m_iMoneyInBank = 0
        m_iThirst = 0
        m_iFatigue = 0;
        m_pCurrentState = GoHomeAndSleepTilRested.Instance(self);
