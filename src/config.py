from argparse import ArgumentParser, BooleanOptionalAction
from configparser import ConfigParser
from enum import Enum
from typing import Any


class ConfigType(Enum):
  STR = 1
  INT = 2
  BOOL = 3

class Config:
  _parser: ConfigParser = ConfigParser()
  _is_prod: bool = False
  
  def load():
    # initialize command-line argument parser
    ap: ArgumentParser = ArgumentParser()
    # declare an argument for the prod environment switch
    ap.add_argument('--prod', default = False, action = BooleanOptionalAction)
    # extract command-line arguments
    args: dict[str, Any] = vars(ap.parse_args())
    
    Config._is_prod = args['prod']
    
    # load configuration file
    Config._parser.read('config{}.ini'.format('.prod' if Config._is_prod else ''))
  
  @property
  @staticmethod
  def is_prod() -> int:
    return Config._is_prod
  
  @staticmethod
  def get(section: str, option: str, type = ConfigType.STR) -> (int | bool | str):
    if type == ConfigType.INT:
      return Config._parser.getint(section, option)
    elif type == ConfigType.BOOL:
      return Config._parser.getboolean(section, option)
    
    return Config._parser.get(section, option)
