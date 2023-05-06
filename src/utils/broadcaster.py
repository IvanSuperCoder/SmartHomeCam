from multiprocessing import Pipe
from multiprocessing.connection import PipeConnection


class Broadcaster:
  _consumers: set[tuple[PipeConnection, PipeConnection]] = set()
  
  def send(self, data):
    for consumer in self._consumers:
      # send data for each consumer
      consumer[1].send(data)
  
  def subscribe(self):
    # create a new consumer
    consumer = Pipe(duplex=False)
    # store the consumer in the set of active consumers
    self._consumers.add(consumer)
    
    return consumer[0]
  
  def unsubscribe(self, receiver: PipeConnection):
    for consumer in self._consumers:
      if consumer[0] == receiver:
        # remove the consumer from the set of active consumers
        self._consumers.remove(consumer)
        
        return
