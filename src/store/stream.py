from src.stream import Stream
from .store import Store


class StreamStore(Store[Stream]):
  _store: dict[str, Stream] = {}
