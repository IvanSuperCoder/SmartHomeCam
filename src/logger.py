from datetime import datetime
import logging
import os
import sys

from config import Config


class Logger:
  _logger: logging.Logger = logging.getLogger()
  
  @staticmethod
  def init():
    # get logs folder path
    path: str = Config.get('logger.path') or '.logs'
    
    # create output folder
    if not os.path.exists(path):
      os.makedirs(path)
    
    # initialize stream handler
    stream_handler: logging.StreamHandler = logging.StreamHandler(stream=sys.stdout)
    # initialize file handler
    file_handler: logging.FileHandler = logging.FileHandler(
      filename=f"{path}/{datetime.today().strftime('%Y-%m-%dT%H%M%S.%f')}.log",
      mode='x',
      encoding='utf-8'
    )
    
    # set logging level
    level: int = logging.INFO if Config.is_prod else logging.DEBUG
    
    file_handler.setLevel(level)
    stream_handler.setLevel(level)
    
    # set logging formats
    formatter: logging.Formatter = logging.Formatter(
      fmt='[%(asctime)s] %(levelname)s: %(message)s',
      datefmt='%Y-%m-%dT%H:%M:%S%z'
    )
    
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)
    
    # add file handler to the logger
    Logger._logger.addHandler(file_handler)
    
    if not Config.is_prod:
      # add stream handler to the logger
      Logger._logger.addHandler(stream_handler)
  
  @classmethod
  @property
  def log(cls) -> logging.Logger:
    return cls._logger
