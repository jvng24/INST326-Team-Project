from abc import ABC, abstractmethod

class AbstractArchiveItem(ABC):
    """
    Abstract base class for all archive items.

    Ensures files and collections share a common interface
    and can be handled polymorphically.
    """

    def __init__(self, name: str):
        self._name = name

    @abstractmethod
    def display_info(self) -> None:
        """Display information about the archive item."""
        pass

    @abstractmethod
    def calculate_size(self) -> float:
        """Return the size of the item in KB."""
        pass
