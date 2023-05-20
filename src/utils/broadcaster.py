from multiprocessing.connection import Pipe, PipeConnection
from typing import Generic, TypeVar


T = TypeVar('T')

class Broadcaster(Generic[T]):
  _pipes: set[tuple[PipeConnection, PipeConnection]] = set()
  
  def subscribe(self) -> PipeConnection:
    pipe: tuple[PipeConnection, PipeConnection] = Pipe(duplex=False)
    
    self._pipes.add(pipe)
    
    return pipe[0]
  
  def send(self, data: T):
    for pipe in self._pipes:
      if not pipe[0].closed:
        pipe[1].send(data)
  
  def unsubscribe(self, connection: PipeConnection):
    if not connection.closed:
      connection.close()
    
    for pipe in self._pipes:
      if pipe[0] == connection:
        self._pipes.remove(pipe)
        
        return
  
  def reset(self):
    for pipe in self._pipes:
      if not pipe[0].closed:
        pipe[0].close()
    
    self._pipes.clear()
