from typing import Any


def deep_value(obj: dict[str, Any], path: str) -> Any:
  value: Any = obj
  
  for key in path.split('.'):
    if isinstance(value, dict):
      if key in value:
        value = value[key]
      else:
        return None
    else:
      return None
  
  return value
