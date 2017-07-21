from Miner import Miner
from EntityNames import EntityNames
import time


miner = Miner(EntityNames.ent_Miner_Bob);

for x in range(0,21):
    miner.Update()
    time.sleep(1)

