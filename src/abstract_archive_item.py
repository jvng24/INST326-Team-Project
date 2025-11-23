from abc import ABC, abstractmethod

class AbstractArchiveItem(ABC):
    """
    Abstract base class for all archive items.

    All archive items must implement display_info().
    """

    @abstractmethod
    def display_info(self):
        """Display information about the item."""
        pass

    @abstractmethod
    def calculate_size(self):
        """Return the size of the item (in KB)."""
        pass

