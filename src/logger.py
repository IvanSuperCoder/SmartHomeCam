import logging
import os
import sys
import time
from typing import TextIO

from src.config import Config
from src.utils.literals import DEFAULT_LOGS_CMD, DEFAULT_LOGS_DIR


class Logger:
  _root: logging.Logger = logging.getLogger('root')
  
  @classmethod
  @property
  def root(cls) -> logging.Logger:
    return cls._root
  
  @staticmethod
  def get(name: str):
    return logging.getLogger(name)
  
  @staticmethod
  def init():
    dir: str = Config[str].get('advanced.logs.dir') or DEFAULT_LOGS_DIR
    cmd: bool = Config[bool].get('advanced.logs.cmd') or DEFAULT_LOGS_CMD
    
    if not os.path.exists(dir):
      # create logs output folder
      os.makedirs(dir)
    
    # initialize stream handler
    stream_handler: logging.StreamHandler[TextIO] = logging.StreamHandler(stream=sys.stdout)
    # initialize file handler
    file_handler: logging.FileHandler = logging.FileHandler(
      filename=f"{dir}/{time.strftime('%Y-%m-%dT%H-%M-%S')}.{'prod' if Config.is_prod else 'debug'}.log",
      mode='x',
      encoding='utf-8'
    )
    
    # set the basic logger configuration
    logging.basicConfig(
      format='[%(asctime)s] %(levelname)s (%(name)s): %(message)s',
      datefmt='%Y-%m-%dT%H:%M:%S%z',
      level=logging.INFO if Config.is_prod else logging.DEBUG,
      handlers=[file_handler, stream_handler] if cmd else [file_handler],
      force=True,
    )
