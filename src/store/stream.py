from src.store.store import Store
from src.stream import Stream


class StreamStore(Store[Stream]):
  _data: dict[str, Stream] = {}
