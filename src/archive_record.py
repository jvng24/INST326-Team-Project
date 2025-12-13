import os
import mimetypes
from datetime import datetime
from abstract_archive_item import AbstractArchiveItem


class ArchiveRecord(AbstractArchiveItem):
    """
    Represents a single file with metadata.
    """

    def __init__(self, file_path: str, author: str = "Unknown", tags=None):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File '{file_path}' not found.")

        super().__init__(os.path.basename(file_path))

        self._file_path = file_path
        self._author = author
        self._tags = tags or []
        self._metadata = self._extract_metadata()

    # ---------- Private Helpers ----------

    def _extract_metadata(self) -> dict:
        stat = os.stat(self._file_path)
        return {
            "name": os.path.basename(self._file_path),
            "size_kb": round(stat.st_size / 1024, 2),
            "type": mimetypes.guess_type(self._file_path)[0] or "unknown",
            "created": datetime.fromtimestamp(stat.st_ctime),
            "modified": datetime.fromtimestamp(stat.st_mtime),
        }

    # ---------- Properties (Encapsulation) ----------

    @property
    def file_path(self) -> str:
        return self._file_path

    @property
    def author(self) -> str:
        return self._author

    @property
    def tags(self) -> list:
        return list(self._tags)

    @property
    def metadata(self) -> dict:
        return dict(self._metadata)

    # ---------- Polymorphic Methods ----------

    def display_info(self) -> None:
        """Display record-specific information."""
        print(f"\n📄 File: {self._metadata['name']}")
        print(f"👤 Author: {self._author}")
        print(f"🏷️  Tags: {', '.join(self._tags) if self._tags else 'None'}")
        print(f"💾 Size: {self._metadata['size_kb']} KB")
        print(f"📁 Type: {self._metadata['type']}")
        print(f"🕒 Created: {self._metadata['created']}")
        print(f"✏️  Modified: {self._metadata['modified']}")

    def calculate_size(self) -> float:
        """Return the file size in KB."""
        return self._metadata["size_kb"]

    # ---------- String Representations ----------

    def __str__(self):
        return f"{self._metadata['name']} ({self._metadata['size_kb']} KB)"

    def __repr__(self):
        return (
            f"ArchiveRecord(file='{self._metadata['name']}', "
            f"author='{self._author}')"
        )
