import uuid
from datetime import datetime
from archive_collection import ArchiveCollection

class User:
    """
    Represents a user with multiple collections.
    Demonstrates composition.
    """

    def __init__(self, name, role="Viewer"):
        if not name or not isinstance(name, str):
            raise ValueError("User name must be a non-empty string.")
        self.name = name
        self.role = role
        self.user_id = str(uuid.uuid4())
        self.collections = []
        self.activity_log = []

    def add_collection(self, collection):
        if not isinstance(collection, ArchiveCollection):
            raise TypeError("Only ArchiveCollection objects can be added.")
        self.collections.append(collection)
        self._log_action(f"Added collection '{collection.name}'")

    def remove_collection(self, collection_name):
        before = len(self.collections)
        self.collections = [c for c in self.collections if c.name != collection_name]
        after = len(self.collections)
        if before == after:
            print("⚠️  No collection found with that name.")
        else:
            self._log_action(f"Removed collection '{collection_name}'")

    def list_collections(self):
        print(f"\n👤 User: {self.name} ({self.role})")
        print("📚 Collections:")
        for c in self.collections:
            print(f"  - {c.name} ({len(c.records)} records)")
        print()

    def _log_action(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.activity_log.append(f"[{timestamp}] {message}")

    def show_activity_log(self):
        print(f"\n📜 Activity Log for {self.name}:")
        for entry in self.activity_log:
            print(entry)
        print()
