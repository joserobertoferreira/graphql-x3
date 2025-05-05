from typing import Any


def to_dict(obj: Any) -> dict:
    """
    Convert an object to a dictionary, including nested objects.
    :param obj: The object to convert
    :return: A dictionary representation of the object
    """
    if hasattr(obj, '__annotations__'):
        return {field: to_dict(getattr(obj, field)) for field in obj.__annotations__}
    elif hasattr(obj, '__dict__'):
        return {key: to_dict(value) for key, value in obj.__dict__.items() if not key.startswith('_')}
    elif isinstance(obj, list):
        return [to_dict(item) for item in obj]
    else:
        return obj
