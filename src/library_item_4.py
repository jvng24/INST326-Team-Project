from datetime import datetime
import uuid

class User:
    """
    Represents a user (e.g., student, researcher, or archivist) interacting with the archive system.

    Example:
        >>> user = User("Manasa", role="Archivist")
        >>> user.add_collection(collection)
        >>> user.list_collections()
    """

    def __init__(self, name, role="Viewer"):
        """
        Initialize a User instance.

        Args:
            name (str): Name of the user.
            role (str): Role of the user (e.g., "Viewer", "Archivist").

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
        """str: The user's name."""
        return self._name

    @property
    def role(self):
        """str: The user's role."""
        return self._role

    @property
    def user_id(self):
        """str: Unique user ID."""
        return self._user_id

    @property
    def collections(self):
        """list[ArchiveCollection]: Collections owned by the user."""
        return self._collections.copy()

    # --- Methods ---
    def add_collection(self, collection):
        """
        Add a collection to this user.

        Args:
            collection (ArchiveCollection): The collection to add.

        Raises:
            TypeError: If the argument is not an ArchiveCollection.
        """
        from archive_collection import ArchiveCollection  # optional type check
        if not isinstance(collection, ArchiveCollection):
            raise TypeError("Only ArchiveCollection objects can be added.")
        self._collections.append(collection)
        self._log_action(f"Added collection '{collection.name}'")

    def remove_collection(self, name):
        """Remove a collection by name."""
        before = len(self._collections)
        self._collections = [c for c in self._collections if c.name != name]
        after = len(self._collections)
        if before == after:
            print("⚠️  No collection found with that name.")
        else:
            self._log_action(f"Removed collection '{name}'")

    def list_collections(self):
        """Display all collections owned by this user."""
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
        """Print a record of all user actions."""
        print(f"\n📜 Activity Log for {self._name}:")
        for entry in self._activity_log:
            print(entry)
        print()

    # --- Representations ---
    def __str__(self):
        return f"User(name='{self._name}', role='{self._role}')"

    def __repr__(self):
        return f"<User id={self._user_id[:8]} name={self._name}>"
