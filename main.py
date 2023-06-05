import asyncio
import signal
from threading import Thread
from typing import Any

from src.config import Config
from src.data import StreamData
from src.logger import Logger
from src.store import StreamStore, ThreadStore
from src.stream import Stream
from src.web import Web


def exit_handler(*_: tuple[Any, ...]):
  response: str = input('Do you really want to exit? (y/n): ')
  
  if response.lower() != 'y':
    return
  
  for item in StreamStore.items():
    # close all streams
    item[1].close()
  
  for item in ThreadStore.items():
    stream: Stream = StreamStore.get(item[0])
    
    # wait for threads to finish
    item[1].join(timeout=stream.data.timeout)
  
  StreamStore.reset()
  ThreadStore.reset()
  
  exit(1)

if __name__ == '__main__':
  # initialize exit handler
  signal.signal(signal.SIGINT, exit_handler)
  # initialize configuration service
  Config.init()
  # initialize logger service
  Logger.init()
  
  for config in Config[list[dict[str, Any]]].get('streams'):
    data: StreamData = StreamData.parse(config)
    # initialize stream service
    stream: Stream = Stream(data, [])
    
    StreamStore.add(data.id, stream)
    
    # initialize stream thread
    thread: Thread = Thread(
      target=asyncio.run,
      name=data.name,
      args=(stream.start(),),
      daemon=True
    )
    
    ThreadStore.add(data.id, thread)
    
    # start stream thread
    thread.start()
  
  # initialize web server
  web: Web = Web()
  # start web server
  web.start()
