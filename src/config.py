from argparse import ArgumentParser, BooleanOptionalAction
from typing import Any, Generic, Optional, TypeVar

import yaml

from src.utils.helpers import deep_value


T = TypeVar('T')

class Config(Generic[T]):
  _data: dict[str, Any] = {}
  _is_prod: bool = None
  
  @classmethod
  @property
  def is_prod(cls) -> bool:
    return cls._is_prod
  
  @staticmethod
  def init():
    # initialize command-line argument parser
    argument_parser: ArgumentParser = ArgumentParser()
    # declare an argument for the prod environment switch
    argument_parser.add_argument('--prod', default=False, action=BooleanOptionalAction)
    
    # extract command-line arguments
    arguments: dict[str, Any] = vars(argument_parser.parse_args())
    
    Config._is_prod = arguments['prod']
    
    # load configuration file
    with open(f"config{'.prod' if Config._is_prod else ''}.yaml", 'r') as fp:
      Config._data = yaml.load(fp, yaml.Loader)
  
  @classmethod
  def get(cls, path: str) -> Optional[T]:
    return deep_value(cls._data, path)
