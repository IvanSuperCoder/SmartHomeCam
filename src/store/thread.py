from threading import Thread

from .store import Store


class ThreadStore(Store[Thread]):
  _store: dict[str, Thread] = {}
