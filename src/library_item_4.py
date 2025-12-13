from datetime import datetime
import uuid


class User:
    """
    Represents a user (e.g., student, researcher, or archivist)
    interacting with the archive system.
    """

    def __init__(self, name, role="Viewer"):
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
        return self._collections.copy()

    @property
    def activity_log(self):
        """Read-only access to user activity log."""
        return self._activity_log.copy()

    # --- Methods ---

    def add_collection(self, collection):
        from archive_collection import ArchiveCollection
        if not isinstance(collection, ArchiveCollection):
            raise TypeError("Only ArchiveCollection objects can be added.")

        if self._role.lower() != "archivist":
            self._log_action("Attempted to add collection without permission")
            raise PermissionError("Only Archivists can add collections.")

        self._collections.append(collection)
        self._log_action(f"Added collection '{collection.name}'")

    def remove_collection(self, name):
        if self._role.lower() != "archivist":
            self._log_action("Attempted to remove collection without permission")
            raise PermissionError("Only Archivists can remove collections.")

        before = len(self._collections)
        self._collections = [c for c in self._collections if c.name != name]

        if len(self._collections) == before:
            self._log_action(f"Failed to remove collection '{name}' (not found)")
            print("⚠️  No collection found with that name.")
        else:
            self._log_action(f"Removed collection '{name}'")

    def list_collections(self):
        print(f"\n👤 User: {self._name} ({self._role})")
        print("📚 Collections:")
        for c in self._collections:
            print(f"  - {c.name} ({c.record_count} records)")
        print()

    # --- Internal Helper ---

    def _log_action(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._activity_log.append(f"[{timestamp}] {message}")

    def show_activity_log(self):
        print(f"\n📜 Activity Log for {self._name}:")
        for entry in self._activity_log:
            print(entry)
        print()

    # --- Representations ---

    def __str__(self):
        return f"User(name='{self._name}', role='{self._role}')"

    def __repr__(self):
        return f"<User id={self._user_id[:8]} name={self._name}>"
