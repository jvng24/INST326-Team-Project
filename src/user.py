import uuid
from datetime import datetime
from archive_collection import ArchiveCollection

class User:
    """
    Represents a user interacting with the archive system.

    Demonstrates composition by owning multiple ArchiveCollection objects.
    """

    def __init__(self, name, role="Viewer"):
        """
        Initialize a User instance.

        Args:
            name (str): User's name.
            role (str): User role (e.g., Viewer, Archivist).

        Raises:
            ValueError: If name is empty or invalid.
        """
        if not name or not isinstance(name, str):
            raise ValueError("User name must be a non-empty string.")

        self._name = name
        self._role = role
        self._user_id = str(uuid.uuid4())
        self._collections = []
        self._activity_log = []

    # --- Properties ---
    @property
    def name(self):
        return self._name

    @property
    def role(self):
        return self._role

    @property
    def user_id(self):
        return self._user_id

    @property
    def collections(self):
        """Return a copy of the user's collections."""
        return self._collections.copy()

    # --- Methods ---
    def add_collection(self, collection):
        """
        Add an ArchiveCollection to the user.

        Args:
            collection (ArchiveCollection): Collection to add.

        Raises:
            TypeError: If object is not an ArchiveCollection.
        """
        if not isinstance(collection, ArchiveCollection):
            raise TypeError("Only ArchiveCollection objects can be added.")

        self._collections.append(collection)
        self._log_action(f"Added collection '{collection.name}'")

    def remove_collection(self, collection_name):
        """
        Remove a collection by name.
        """
        before = len(self._collections)
        self._collections = [
            c for c in self._collections if c.name != collection_name
        ]

        if len(self._collections) == before:
            print("⚠️  No collection found with that name.")
        else:
            self._log_action(f"Removed collection '{collection_name}'")

    def list_collections(self):
        """
        Display all collections owned by the user.
        """
        print(f"\n👤 User: {self._name} ({self._role})")
        print("📚 Collections:")
        for c in self._collections:
            print(f"  - {c.name} ({c.record_count} records)")
        print()

    def _log_action(self, message):
        """Internal helper to record user activity."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._activity_log.append(f"[{timestamp}] {message}")

    def show_activity_log(self):
        """
        Display the user's activity log.
        """
        print(f"\n📜 Activity Log for {self._name}:")
        for entry in self._activity_log:
            print(entry)
        print()

    # --- Representations ---
    def __str__(self):
        return f"User(name='{self._name}', role='{self._role}')"

    def __repr__(self):
        return f"<User id={self._user_id[:8]} name={self._name}>"
