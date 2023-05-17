from dataclasses import dataclass
from typing import Self
import uuid


@dataclass
class StreamData:
  id: str
  name: str
  source: str
  timeout: int
  
  @classmethod
  def parse(cls, stream: dict[str, str | int]) -> Self:
    return cls(
      id=str(uuid.uuid4()),
      name=stream['name'],
      source=stream['source'],
      timeout=stream['timeout']
    )
