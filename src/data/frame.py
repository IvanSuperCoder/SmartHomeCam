from dataclasses import dataclass
from fractions import Fraction
from typing import Self

import av
import numpy


RGB24: str = 'rgb24'

@dataclass
class FrameData:
  content: numpy.ndarray
  format: str
  time_base: Fraction
  pts: int
  
  @classmethod
  def parse(cls, frame: av.VideoFrame, format: str = RGB24) -> Self:
    return cls(
      content=frame.to_ndarray(format=format),
      format=frame.format if not format else format,
      time_base=frame.time_base,
      pts=frame.pts
    )
  
  @classmethod
  def pack(cls, data: Self) -> av.VideoFrame:
    frame: av.VideoFrame = av.VideoFrame.from_ndarray(data.content, format=data.format)
    
    # set the tick duration of the timescale
    frame.time_base = data.time_base
    # set frame presentation timestamp
    frame.pts = data.pts
    
    return frame
