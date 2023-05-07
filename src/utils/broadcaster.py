from multiprocessing import Pipe
from multiprocessing.connection import PipeConnection
from typing import Any


Consumer = tuple[PipeConnection, PipeConnection]

class Broadcaster:
  _consumers: set[Consumer] = set()
  
  def send(self, data: Any):
    for consumer in self._consumers:
      # send data for each active consumer
      if not consumer[0].closed:
        consumer[1].send(data)
  
  def subscribe(self) -> PipeConnection:
    # create a new consumer
    consumer: Consumer = Pipe(duplex = False)
    # store the consumer on the stack
    self._consumers.add(consumer)
    
    return consumer[0]
  
  def unsubscribe(self, receiver: PipeConnection):
    # close active connection
    if not receiver.closed:
      receiver.close()
    
    for consumer in self._consumers:
      if consumer[0] == receiver:
        # remove consumer from the stack
        self._consumers.remove(consumer)
        
        return
