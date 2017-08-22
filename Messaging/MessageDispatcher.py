from BaseGameEntity import BaseGameEntity
from EntityManager import EntityManager
from Messaging import Telegram
from Messaging import MessageTypes
from EntityNames import  EntityNames
from Messaging.PriorityQueue import PriorityQueue
import datetime


# to make code easier to read


#to make life easier...
##MessageDispatcher Dispatch = new MessageDispatcher()
#a Set is used as the container for the delayed messages
#because of the benefit of automatic sorting and avoidance
#of duplicates. Messages are sorted by their dispatch time.
#PriorityQ = new TreeSet<Telegram>();
PriorityQ = PriorityQueue()
#
# this method is utilized by DispatchMessage or DispatchDelayedMessages.
# This method calls the message handling member function of the receiving
# entity, pReceiver, with the newly created telegram
#/

class MessageDispatcher(object):
        # Here will be the instance stored.
        __instance = None

        @staticmethod
        def getInstance():
            """ Static access method. """
            if MessageDispatcher.__instance == None:
                MessageDispatcher()
            return MessageDispatcher.__instance

        def __init__(self):
            """ Virtually private constructor. """
            if MessageDispatcher.__instance != None:
                raise Exception("This class is a singleton!")
            else:
                MessageDispatcher.__instance = self


        SEND_MSG_IMMEDIATELY = 0.0
        NO_ADDITIONAL_INFO = None

        def Discharge(self, BaseGameEntity , Telegram):
            if BaseGameEntity.HandleMessage(Telegram):
                #telegram could not be handled
                print("\nMessage not handled")



        def DispatchMessage(self,delay,sender,receiver,msg,ExtraInfo):

            #get pointers to the sender and receiver
            pSender = EntityManager.getInstance().GetEntityFromID(sender)
            pReceiver = EntityManager.getInstance().GetEntityFromID(receiver)

            #make sure the receiver is valid
            if pReceiver is None:
                print("\nWarning! No Receiver with ID of " + receiver + " found")
                return

            #create the telegram
            telegram = Telegram(0, sender, receiver, msg, ExtraInfo);

            #if there is no delay, route telegram immediately
            if delay <= 0.0:
                print("\nInstant telegram dispatched at time: " + datetime.datetime.now().time()
                        + " by " + EntityNames.GetNameOfEntity(pSender.ID()) + " for "
                        + EntityNames.GetNameOfEntity(pReceiver.ID())
                        + ". Msg is " + MessageTypes.MsgToStr(msg));

                #send the telegram to the recipient
                self.Discharge(pReceiver, Telegram)
            #else calculate the time when the telegram should be dispatched
            else:
                CurrentTime = datetime.datetime.now().time()

                telegram.DispatchTime = CurrentTime + delay

                #and put it in the queue
                self.PriorityQ.add(Telegram);

                print("\nDelayed telegram from " + EntityNames.GetNameOfEntity(pSender.ID())
                        + " recorded at time " + datetime.datetime.now().time() + " for "
                        + EntityNames.GetNameOfEntity(pReceiver.ID()) + ". Msg is " + MsgToStr(msg))


        #
        # This function dispatches any telegrams with a timestamp that has
        #  expired. Any dispatched telegrams are removed from the queue
        #
        # send out any delayed messages. This method is called each time through
        # the main game loop.
        #
        def DispatchDelayedMessages(self):
            #get current time
            CurrentTime = datetime.datetime.now().time()

            #now peek at the queue to see if any telegrams need dispatching.
            #remove all telegrams from the front of the queue that have gone
            #past their sell by date
            while (PriorityQ.isEmpty() is False) & (PriorityQ.last().DispatchTime < CurrentTime) & (PriorityQ.last().DispatchTime > 0) :
                #read the telegram from the front of the queue

                telegram = PriorityQ.last()

                #find the recipient
                pReceiver = EntityManager.getInstance().GetEntityFromID(telegram.Receiver)

                print("\nQueued telegram ready for dispatch: Sent to "
                        + EntityNames.GetNameOfEntity(pReceiver.ID()) + ". Msg is " + MessageTypes.MsgToStr(telegram.Msg))

                #send the telegram to the recipient
                self.Discharge(pReceiver, telegram)

                #remove it from the queue
                PriorityQ.remove(PriorityQ.last())
