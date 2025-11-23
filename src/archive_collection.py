from datetime import datetime
from abstract_archive_item import AbstractArchiveItem

class ArchiveCollection(AbstractArchiveItem):
    """
    Represents a collection of ArchiveRecord objects.
    Demonstrates composition (has-a relationship).
    """

    def __init__(self, name):
        if not name or not isinstance(name, str):
            raise ValueError("Collection name must be a non-empty string.")
        self.name = name
        self.records = []
        self.created = datetime.now()

    def add_record(self, record):
        from archive_record import ArchiveRecord
        if not isinstance(record, ArchiveRecord):
            raise TypeError("Only ArchiveRecord instances can be added.")
        self.records.append(record)
        print(f"✅ Added '{record.metadata['name']}' to collection '{self.name}'.")

    def remove_record(self, record_name):
        before = len(self.records)
        self.records = [r for r in self.records if r.metadata['name'] != record_name]
        after = len(self.records)
        if before == after:
            print("⚠️  No record found with that name.")
        else:
            print(f"🗑️  Record removed from '{self.name}'.")

    # Inherited / Polymorphic Methods 
    
    def display_info(self):
        """Display collection-specific info."""
        print(f"\n📚 Collection: {self.name}")
        print(f"📦 Records: {len(self.records)}")
        print(f"📅 Created: {self.created}")
        for r in self.records:
            print(f"   - {r.metadata['name']} ({r.author})")
        print()

    def calculate_size(self):
        """Return the total size of all records in the collection."""
        return sum(r.calculate_size() for r in self.records)
