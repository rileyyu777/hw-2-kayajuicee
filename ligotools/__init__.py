
import importlib

__all__ = ["readligo"]

def __getattr__(name):
    if name == "readligo":
        return importlib.import_module(".readligo", __name__)
    raise AttributeError(name)
