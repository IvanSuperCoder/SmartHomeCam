import json
from typing import Any

from utils.property import deep_value


class Config:
  _data: dict[str, Any] = {}
  
  @staticmethod
  def load(file: str):
    # load configuration file
    with open(file, 'r') as fp:
      Config._data = dict(json.load(fp))
  
  @staticmethod
  def get(path: str) -> Any:
    return deep_value(Config._data, path)
