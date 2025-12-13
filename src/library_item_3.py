from datetime import datetime
from abstract_archive_item import AbstractArchiveItem


class ArchiveCollection(AbstractArchiveItem):
    """
    Represents a collection of ArchiveRecord objects grouped under a specific category.
    Demonstrates composition and polymorphism.
    """

    def __init__(self, name):
        if not name or not isinstance(name, str):
            raise ValueError("Collection name must be a non-empty string.")
        self._name = name
        self._records = []
        self._created = datetime.now()

    # --- Properties ---

    @property
    def name(self):
        return self._name

    @property
    def record_count(self):
        return len(self._records)

    @property
    def records(self):
        """Read-only access to records."""
        return list(self._records)

    # --- Methods ---

    def add_record(self, record):
        from archive_record import ArchiveRecord
        if not isinstance(record, ArchiveRecord):
            raise TypeError("Only ArchiveRecord instances can be added.")
        self._records.append(record)
        print(f"✅ Added '{record.metadata['name']}' to collection '{self._name}'.")

    def remove_record(self, record_id):
        before = len(self._records)
        self._records = [r for r in self._records if r.id != record_id]
        if len(self._records) == before:
            print("⚠️  No record found with that ID.")
        else:
            print(f"🗑️  Record removed from '{self._name}'.")

    def find_by_author(self, author_name):
        return [r for r in self._records if r.author.lower() == author_name.lower()]

    def search(self, keyword):
        return [r for r in self._records if r.matches_keyword(keyword)]

    # --- Polymorphic Methods ---

    def display_info(self):
        """Display collection-specific information (polymorphic override)."""
        print(f"\n📚 Collection: {self._name}")
        print(f"📦 Records: {self.record_count}")
        print(f"📅 Created: {self._created.strftime('%Y-%m-%d %H:%M:%S')}")
        for r in self._records:
            print(f"   - {r}")
        print()

    def calculate_size(self):
        """Return total size of all records in KB."""
        return sum(r.calculate_size() for r in self._records)

    # --- Representations ---

    def __str__(self):
        return f"ArchiveCollection('{self._name}', {self.record_count} records)"

    def __repr__(self):
        return f"<ArchiveCollection name={self._name} records={self.record_count}>"
