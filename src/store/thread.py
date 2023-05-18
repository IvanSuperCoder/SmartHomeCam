from threading import Thread

from src.store.store import Store


class ThreadStore(Store[Thread]):
  _data: dict[str, Thread] = {}
