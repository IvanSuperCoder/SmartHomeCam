from aiortc import VideoStreamTrack

from src.data import FrameData
from src.utils.types import Transform


class FrameDataTrack(VideoStreamTrack):
  _track: VideoStreamTrack = None
  _transformers: list[Transform] = []
  
  def __init__(self, track: VideoStreamTrack, transformers: list[Transform] = []):
    super().__init__()
    
    self._track = track
    self._transformers = transformers
  
  async def recv(self) -> FrameData:
    data: FrameData = FrameData.parse(await self._track.recv())
    
    for transform in self._transformers:
      # transform frame data before emitting
      data = await transform(data)
    
    return data
