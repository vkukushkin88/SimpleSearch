
import abc
import logging


logger = logging.getLogger(__name__)


class Storage:

    def __init__(self, index, config):
        self._index = index
        self._cfg = config

    @abc.abstractmethod
    def add(self, line: str):
        raise NotImplementedError

    @abc.abstractmethod
    def get_by_keyword(self, word: str, limit: int=10):
        raise NotImplementedError

    @abc.abstractmethod
    def reindexing(self):
        raise NotImplementedError
