import os
from typing import Any, Self

import yaml

from utils.property import deep_value


class Config:
  _data: dict[str, Any] = {}
  
  is_prod: bool = os.environ['ENV'] == 'prod'
  
  @staticmethod
  def init():
    # load configuration file
    with open(f"config.{os.environ['ENV']}.yaml", 'r') as fp:
      Config._data = yaml.load(fp, yaml.Loader)
  
  @classmethod
  def get(cls, path: str) -> Any:
    return deep_value(cls._data, path)
