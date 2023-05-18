from src.recorder import Recorder
from src.store.store import Store


class RecorderStore(Store[Recorder]):
  _data: dict[str, Recorder] = {}
