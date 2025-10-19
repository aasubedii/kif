from abc import ABC, abstractmethod

class BaseAgent(ABC):
    @abstractmethod
    def handle(self, task: dict) -> dict:
        ...
