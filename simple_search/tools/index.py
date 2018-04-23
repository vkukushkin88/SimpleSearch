
import abc


class Index:

    def __init__(self, config):
        self._cfg = config

    @abc.abstractmethod
    def add(self, key: str, value: "value, any type") -> bool:
        """Add to index."""
        raise NotImplementedError

    @abc.abstractmethod
    def get_by_key(self, key: str) -> "value, any type":
        """Get indexed value"""
        raise NotImplementedError
