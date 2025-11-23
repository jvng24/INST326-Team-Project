import os
import mimetypes
from datetime import datetime
from abstract_archive_item import AbstractArchiveItem

class ArchiveRecord(AbstractArchiveItem):
    """
    Represents a single file with metadata.
    """

    def __init__(self, file_path, author="Unknown", tags=None):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File '{file_path}' not found.")

        self.file_path = file_path
        self.author = author
        self.tags = tags or []
        self.metadata = self._extract_metadata()

    def _extract_metadata(self):
        stat = os.stat(self.file_path)
        return {
            "name": os.path.basename(self.file_path),
            "size_kb": round(stat.st_size / 1024, 2),
            "type": mimetypes.guess_type(self.file_path)[0] or "unknown",
            "created": datetime.fromtimestamp(stat.st_ctime),
            "modified": datetime.fromtimestamp(stat.st_mtime)
        }

    # Inherited / Polymorphic Methods 

    def display_info(self):
        """Display record-specific info."""
        print(f"\n📄 File: {self.metadata['name']}")
        print(f"👤 Author: {self.author}")
        print(f"🏷️  Tags: {', '.join(self.tags) if self.tags else 'None'}")
        print(f"💾 Size: {self.metadata['size_kb']} KB")
        print(f"📁 Type: {self.metadata['type']}")
        print(f"🕒 Created: {self.metadata['created']}")
        print(f"✏️  Modified: {self.metadata['modified']}\n")

    def calculate_size(self):
        return self.metadata['size_kb']
    
