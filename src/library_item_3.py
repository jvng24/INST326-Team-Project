from datetime import datetime

class ArchiveCollection:
    """
    Represents a collection of ArchiveRecord objects grouped under a specific category.

    This class enables organization, searching, and summarizing of records that belong
    to the same project, topic, or type.

    Example:
        >>> collection = ArchiveCollection("Research Projects")
        >>> collection.add_record(record1)
        >>> collection.add_record(record2)
        >>> collection.find_by_author("Manasa")
    """

    def __init__(self, name):
        """
        Initialize an ArchiveCollection.

        Args:
            name (str): Name of the collection or category.

        Raises:
            ValueError: If name is empty or not a string.
        """
        if not name or not isinstance(name, str):
            raise ValueError("Collection name must be a non-empty string.")
        self._name = name
        self._records = []
        self._created = datetime.now()

    # --- Properties ---
    @property
    def name(self):
        """str: The name of this collection."""
        return self._name

    @property
    def record_count(self):
        """int: The number of records currently stored."""
        return len(self._records)

    # --- Methods ---
    def add_record(self, record):
        """
        Add an ArchiveRecord to this collection.

        Args:
            record (ArchiveRecord): Record to add.

        Raises:
            TypeError: If the record is not an ArchiveRecord instance.
        """
        from archive_record import ArchiveRecord  # optional type check
        if not isinstance(record, ArchiveRecord):
            raise TypeError("Only ArchiveRecord instances can be added.")
        self._records.append(record)
        print(f"✅ Added '{record.metadata['name']}' to collection '{self._name}'.")

    def remove_record(self, record_id):
        """
        Remove a record by its ID.

        Args:
            record_id (str): The unique ID of the record to remove.
        """
        before = len(self._records)
        self._records = [r for r in self._records if r.id != record_id]
        after = len(self._records)
        if before == after:
            print("⚠️  No record found with that ID.")
        else:
            print(f"🗑️  Record removed from '{self._name}'.")

    def find_by_author(self, author_name):
        """Return all records created by a given author."""
        return [r for r in self._records if r.author.lower() == author_name.lower()]

    def search(self, keyword):
        """Return all records containing the keyword in name or tags."""
        return [r for r in self._records if r.matches_keyword(keyword)]

    def summary(self):
        """Display a formatted summary of the collection."""
        print(f"\n📚 Collection: {self._name}")
        print(f"📦 Records: {self.record_count}")
        print(f"📅 Created: {self._created.strftime('%Y-%m-%d %H:%M:%S')}")
        for r in self._records:
            print(f"   - {r}")
        print()

    # --- Representations ---
    def __str__(self):
        return f"ArchiveCollection('{self._name}', {self.record_count} records)"

    def __repr__(self):
        return f"<ArchiveCollection name={self._name} records={self.record_count}>"
