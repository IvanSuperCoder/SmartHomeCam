from typing import Any, Generic, TypeVar

import yaml

from src.utils.property import deep_value


T = TypeVar('T')

class Config(Generic[T]):
  _data: dict[str, Any] = {}
  _is_prod: bool = None
  
  @classmethod
  @property
  def is_prod(cls) -> bool:
    return cls._is_prod
  
  @staticmethod
  def init(is_prod: bool = False):
    Config._is_prod = is_prod
    
    # load configuration file
    with open(f"config{'.prod' if is_prod else ''}.yaml", 'r') as fp:
      Config._data = yaml.load(fp, yaml.Loader)
  
  @classmethod
  def get(cls, path: str) -> T | None:
    return deep_value(cls._data, path)
