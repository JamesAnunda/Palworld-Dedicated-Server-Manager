from abc import ABC, abstractmethod


class ISavable(ABC):
    @abstractmethod
    def save(self) -> dict:
        pass

class IRestorable(ABC):
    @abstractmethod
    def restore(self, restore_data: dict) -> None:
        pass
