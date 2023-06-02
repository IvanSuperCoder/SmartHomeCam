from argparse import ArgumentParser, BooleanOptionalAction
from typing import Any, Generic, Optional, TypeVar

import pydash
import yaml


T = TypeVar('T')

class Config(Generic[T]):
  _config: dict[str, Any] = {}
  _is_prod: bool = False
  
  @staticmethod
  def init():
    # initialize command-line argument parser
    argument_parser: ArgumentParser = ArgumentParser()
    # declare an argument for the prod environment switch
    argument_parser.add_argument('--prod', default=False, action=BooleanOptionalAction)
    
    # parse command-line arguments
    arguments: dict[str, Any] = vars(argument_parser.parse_args())
    
    Config._is_prod = arguments['prod']
    
    # load configuration file
    with open(f"config{'.prod' if Config._is_prod else ''}.yaml", 'r') as fp:
      Config._config = yaml.load(fp, yaml.Loader)
  
  @classmethod
  @property
  def is_prod(cls) -> bool:
    return cls._is_prod
  
  @classmethod
  def get(cls, path: str) -> Optional[T]:
    return pydash.get(cls._config, path, None)
