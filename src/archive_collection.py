from datetime import datetime
from abstract_archive_item import AbstractArchiveItem
from archive_record import ArchiveRecord


class ArchiveCollection(AbstractArchiveItem):
    """
    Represents a collection of ArchiveRecord objects.
    Demonstrates composition (has-a relationship).
    """

    def __init__(self, name: str):
        if not name or not isinstance(name, str):
            raise ValueError("Collection name must be a non-empty string.")

        super().__init__(name)

        self._records = []
        self._created = datetime.now()

    # ---------- Properties (Encapsulation) ----------

    @property
    def records(self):
        """Read-only access to records in the collection."""
        return list(self._records)

    @property
    def created(self):
        """datetime: When the collection was created."""
        return self._created

    # ---------- Composition Methods ----------

    def add_record(self, record: ArchiveRecord) -> None:
        """Add an ArchiveRecord to the collection."""
        if not isinstance(record, ArchiveRecord):
            raise TypeError("Only ArchiveRecord instances can be added.")
        self._records.append(record)

    def remove_record(self, record_name: str) -> None:
        """Remove a record by name."""
        original_len = len(self._records)
        self._records = [
            r for r in self._records if r.metadata["name"] != record_name
        ]

        if len(self._records) == original_len:
            raise ValueError("No record found with that name.")

    # ---------- Polymorphic Methods ----------

    def display_info(self) -> None:
        """Display collection-specific information."""
        print(f"\n📚 Collection: {self._name}")
        print(f"📦 Records: {len(self._records)}")
        print(f"📅 Created: {self._created}")
        for r in self._records:
            print(f"   - {r.metadata['name']} ({r.author})")

    def calculate_size(self) -> float:
        """Return total size of all records in KB."""
        return sum(r.calculate_size() for r in self._records)

    # ---------- String Representations ----------

    def __str__(self):
        return f"Collection '{self._name}' ({len(self._records)} items)"

    def __repr__(self):
        return f"ArchiveCollection(name='{self._name}', records={len(self._records)})"
