from threading import Thread

from .store import Store


class ThreadStore(Store[Thread]):
  _data: dict[str, Thread] = {}
