from abc import ABC, abstractmethod


class QueryCreator(ABC):
    @abstractmethod
    def get_respond(self):
        pass
