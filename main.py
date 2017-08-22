from Miner import Miner
from MinersWife import MinersWife
from EntityNames import EntityNames
from EntityManager import EntityManager
import time

# create a miner
Bob = Miner(EntityNames.ent_Miner_Bob)

# create his wife
Elsa = MinersWife(EntityNames.ent_Elsa)


#register them with the entity manager
EntityMgr = EntityManager()
EntityMgr.RegisterEntity(Bob)
EntityMgr.RegisterEntity(Elsa)

for x in range(0, 20):
    Bob.Update()
    Elsa.Update()
    time.sleep(1)
