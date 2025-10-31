import os
from datetime import datetime
import mimetypes
import uuid

class ArchiveRecord:
    """
    Represents a single file and its metadata within the CampusDrive Digital Archive System.

    This class stores essential information about a file, such as its name, size, type,
    author, and timestamps. It also supports metadata editing and keyword searching.

    Example:
        >>> record = ArchiveRecord("C:/Users/Manasa/Documents/report.pdf", author="Manasa", tags=["research", "final"])
        >>> print(record)
        report.pdf - Manasa (application/pdf)
        >>> record.matches_keyword("research")
        True
    """

    def __init__(self, file_path, author="Unknown", tags=None):
        """
        Initialize an ArchiveRecord instance.

        Args:
            file_path (str): Path to the file.
            author (str): Creator or owner of the file. Defaults to "Unknown".
            tags (list[str], optional): Descriptive tags for categorization or search.

        Raises:
            FileNotFoundError: If the file does not exist.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File '{file_path}' not found.")

        self._id = str(uuid.uuid4())
        self._file_path = file_path
        self._author = author
        self._tags = tags or []
        self._metadata = self._extract_metadata()

    # ----- Properties -----
    @property
    def id(self):
        """str: Unique identifier for this record (read-only)."""
        return self._id

    @property
    def file_path(self):
        """str: File path of the record."""
        return self._file_path

    @property
    def author(self):
        """str: Author or creator of the file."""
        return self._author

    @property
    def tags(self):
        """list[str]: List of descriptive tags associated with the file."""
        return self._tags

    @property
    def metadata(self):
        """dict: File metadata (read-only copy)."""
        return self._metadata.copy()

    # ----- Private Helper -----
    def _extract_metadata(self):
        """Extract metadata such as name, size, type, and timestamps."""
        stat = os.stat(self._file_path)
        return {
            "name": os.path.basename(self._file_path),
            "size_kb": round(stat.st_size / 1024, 2),
            "type": mimetypes.guess_type(self._file_path)[0] or "unknown",
            "created": datetime.fromtimestamp(stat.st_ctime),
            "modified": datetime.fromtimestamp(stat.st_mtime)
        }

    # ----- Public Methods -----
    def edit_metadata(self, author=None, tags=None):
        """
        Edit metadata fields for this record.

        Args:
            author (str, optional): Update the author name.
            tags (list[str], optional): Replace or add descriptive tags.

        Example:
            >>> record.ed
