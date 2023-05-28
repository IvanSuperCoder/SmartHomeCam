from src.recorder import Recorder
from .store import Store


class RecorderStore(Store[Recorder]):
  _data: dict[str, Recorder] = {}
