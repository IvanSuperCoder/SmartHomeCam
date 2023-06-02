from typing import Awaitable, Callable

from src.data import FrameData


Transform = Callable[[FrameData], Awaitable[FrameData]]
