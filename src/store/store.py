from abc import ABC
from typing import Generic, TypeVar


T = TypeVar('T')

class Store(ABC, Generic[T]):
  # abstract property
  _store: dict[str, T]
  
  @classmethod
  def add(cls, key: str, value: T):
    cls._store[key] = value
  
  @classmethod
  def get(cls, key: str) -> T:
    return cls._store[key]
  
  @classmethod
  def remove(cls, key: str):
    cls._store.pop(key)
  
  @classmethod
  def items(cls) -> list[tuple[str, T]]:
    return cls._store.items()
  
  @classmethod
  def reset(cls):
    cls._store.clear()
