from enum import Enum
import time
from typing import Callable

from aiortc.contrib.media import MediaPlayer
from aiortc import VideoStreamTrack
import av

from src.data.frame import FrameData
from src.data.stream import StreamData
from src.logger import Logger
from src.utils.broadcaster import Broadcaster


Transform = Callable[[FrameData], FrameData]

class StreamStatus(Enum):
  INIT = 0
  OPENED = 1
  CLOSED = 2

class Stream:
  _data: StreamData = None
  _transform: Transform = None
  _stream: VideoStreamTrack = None
  _broadcaster: Broadcaster = Broadcaster()
  _status: StreamStatus = StreamStatus.INIT
  
  def __init__(self, data: StreamData, transform: Transform = None):
    self._data = data
    self._transform = transform
    
    # connect to the stream
    self._connect()
  
  @property
  def data(self) -> StreamData:
    return self._data
  
  @property
  def broadcaster(self) -> Broadcaster:
    return self._broadcaster
  
  async def start(self):
    if self._status != StreamStatus.INIT:
      return
    
    self._status = StreamStatus.OPENED
    
    frame: av.VideoFrame = None
    frame_data: FrameData = None
    
    while True:
      if self._status == StreamStatus.CLOSED:
        return
      
      try:
        # get current frame from the stream
        frame = await self._stream.recv()
      except Exception as exc_info:
        Logger.log.warning(f'Lost connection to stream "{self._data.name}". Reconnecting...', exc_info=exc_info)
        
        # reconnect to the stream
        self._connect()
        
        continue
      
      frame_data = FrameData.parse(frame)
      
      if self._transform:
        # transform frame data
        frame_data = await self._transform(frame_data)
      
      # send frame data to broadcaster consumers
      self._broadcaster.send(frame_data)
  
  def close(self):
    if self._status != StreamStatus.OPENED:
      return
    
    self._status = StreamStatus.CLOSED
    
    # reset broadcaster consumers
    self._broadcaster.reset()
    # reset stream connection
    self._reset()
  
  def _connect(self):
    # close previous connection (if any)
    self._reset()
    
    while True:
      if self._status == StreamStatus.CLOSED:
        return
      
      try:
        self._stream = MediaPlayer(self._data.source, timeout=self._data.timeout).video
        
        Logger.log.info(f'Successfully connected to stream "{self._data.name}"!')
        
        break
      except Exception as exc_info:
        Logger.log.warning(f'Failed to connect to stream "{self._data.name}". Reconnecting...', exc_info=exc_info)
        
        # reset stream connection
        self._reset()
        # wait before next connection attempt
        time.sleep(self._data.timeout)
        
        continue
  
  def _reset(self):
    if not self._stream:
      return
    
    self._stream.stop()
    self._stream = None
