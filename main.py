import asyncio
import signal
from threading import Thread
from typing import Any

from src.config import Config
from src.data import StreamData
from src.logger import Logger
from src.recorder import Recorder
from src.store import RecorderStore, StreamStore, ThreadStore
from src.stream import Stream
from src.web import Web


def ask_exit(signum: int, frame: Any):
  answer: str = input('Do you really want to exit? (y/n): ')
  
  if answer.lower() != 'y':
    return
  
  for item in RecorderStore.items():
    # close all recording services
    item[1].close()
  
  RecorderStore.reset()
  
  for item in StreamStore.items():
    # close all streaming services
    item[1].close()
  
  for item in ThreadStore.items():
    stream: Stream = StreamStore.get(item[0])
    
    # wait for threads to finish
    item[1].join(timeout=stream.data.timeout)
  
  StreamStore.reset()
  ThreadStore.reset()
  
  exit(1)

async def main(data: StreamData):
  # initialize stream service
  stream: Stream = Stream(data)
  # initialize recorder service
  recorder: Recorder = Recorder()
  
  StreamStore.add(data.id, stream)
  RecorderStore.add(data.id, recorder)
  
  # listen to thread processes
  await asyncio.gather(stream.start(), recorder.start())

if __name__ == '__main__':
  # initialize exit handler
  signal.signal(signal.SIGINT, ask_exit)
  # initialize configuration service
  Config.init()
  # initialize logger service
  Logger.init()
  
  for stream_config in Config[list[dict[str, Any]]].get('streams'):
    data: StreamData = StreamData.parse(stream_config)
    
    # initialize stream thread
    thread: Thread = Thread(
      target=asyncio.run,
      name=data.name,
      args=(main(data),),
      daemon=True
    )
    # start stream thread
    thread.start()
    
    ThreadStore.add(data.id, thread)
  
  # initialize web server
  web: Web = Web()
  # start web server
  web.start()
