from abc import ABC
from typing import Generic, TypeVar


T = TypeVar('T')

class Store(ABC, Generic[T]):
  _data: dict[str, T]
  
  @property
  @classmethod
  def data(cls) -> dict[str, T]:
    return cls._data
  
  @classmethod
  def add(cls, key: str, value: T):
    cls._data[key] = value
  
  @classmethod
  def get(cls, key: str) -> T:
    return cls._data[key]
  
  @classmethod
  def remove(cls, key: str):
    cls._data.pop(key)
  
  @classmethod
  def reset(cls):
    cls._data.clear()
