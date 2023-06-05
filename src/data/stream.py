from dataclasses import dataclass
from hashlib import md5
from typing import Any, Self
from uuid import UUID

from src.utils.literals import DEFAULT_STREAM_TIMEOUT, DEFAULT_STREAM_WEB


@dataclass
class StreamData:
  id: str
  name: str
  source: str
  timeout: int
  web: bool
  
  @classmethod
  def parse(cls, config: dict[str, Any]) -> Self:
    name: str = str(config['name']).title()
    hex: str = md5(name.encode()).hexdigest()
    id: str = str(UUID(hex=hex))
    
    return cls(
      id=id,
      name=name or f'Stream {id}',
      source=str(config['source']),
      timeout=int(config['timeout']) or DEFAULT_STREAM_TIMEOUT,
      web=bool(config['web']) or DEFAULT_STREAM_WEB
    )
