from dataclasses import dataclass
from fractions import Fraction
from typing import Self

import av
import numpy


@dataclass
class FrameData:
  content: numpy.ndarray
  format: str
  time_base: Fraction
  pts: int
  
  @classmethod
  def parse(cls, frame: av.VideoFrame, format: str = 'bgr24'):
    return cls(
      content = frame.to_ndarray(format = format),
      format = frame.format if not format else format,
      time_base = frame.time_base,
      pts = frame.pts
    )
  
  @classmethod
  def pack(cls, frame_data: Self):
    frame = av.VideoFrame.from_ndarray(frame_data.content, format = frame_data.format)
    
    # set the duration of one tick of the timescale
    frame.time_base = frame_data.time_base
    # set frame presentation time stamp
    frame.pts = frame_data.pts
    
    return frame
