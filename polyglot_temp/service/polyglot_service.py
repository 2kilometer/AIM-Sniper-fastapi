from abc import ABC, abstractmethod


class PolyglotService(ABC):
    @abstractmethod
    def requestNextQuestion(self):
        pass