from abc import ABC, abstractmethod


class ISavable(ABC):
    @abstractmethod
    def save(self) -> None:
        pass

class IRestorable(ABC):
    @abstractmethod
    def restore(self) -> None:
        pass
