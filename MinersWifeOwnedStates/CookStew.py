from EntityNames import  EntityNames
from State import StateClass
from Messaging import MessageDispatcher
from Messaging import MessageTypes
from MinersWifeOwnedStates import DoHouseWork
import datetime

class CookStew(StateClass):
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if CookStew.__instance == None:
            CookStew()
        return CookStew.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if CookStew.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            CookStew.__instance = self

    def enter(self,MinersWife):
        #if not already cooking put the stew in the oven
        if MinersWife.Cooking() is False:
        print("\n" + EntityNames.GetNameOfEntity(MinersWife.ID()) + ": Putting the stew in the oven")

        #send a delayed message myself so that I know when to take the stew
        #out of the oven
        MessageDispatcher.getInstance().DispatchMessage(1.5, #time delay
            MinersWife.ID(), # sender ID
            MinersWife.ID(), # receiver ID
            MessageTypes.Msg_StewReady, # msg
            MessageDispatcher.getInstance().NO_ADDITIONAL_INFO);

        MinersWife.SetCooking(True)

    def execute(self,MinersWife):
        print("\n" + EntityNames.GetNameOfEntity(MinersWife.ID()) + ": Fussin' over food")

    def OnMessage(self,MinersWife, Telegram):
        if Telegram.Msg == MessageTypes.Msg_StewReady:
            print("\nMessage received by " + EntityNames.GetNameOfEntity(MinersWife.ID())
                 + " at time: " + datetime.datetime.now().time())

            print("\n" + EntityNames.GetNameOfEntity(MinersWife.ID()) + ": StewReady! Lets eat")

            #let hubby know the stew is ready
            MessageDispatcher.getInstance().DispatchMessage(MessageDispatcher.getInstance().SEND_MSG_IMMEDIATELY,
                                                            MinersWife.ID(),
                                                            EntityNames.ent_Miner_Bob.id,
                                                            MessageDispatcher.getInstance().MessageTypes.Msg_StewReady,
                                                            MessageDispatcher.getInstance().NO_ADDITIONAL_INFO)

            MinersWife.SetCooking(False)

            MinersWife.GetFSM().ChangeState(DoHouseWork.Instance())