from typing import Any


# get deep value from dictionary by passing path to it as a string
def deep_value(data: dict[str, Any], path: str) -> Any:
  value: dict[str, Any] = data
  
  for key in path.split('.'):
    if isinstance(value, dict):
      if key in value:
        value = value[key]
      else:
        return None
  
  return value
