import os
import shutil
from datetime import datetime
import mimetypes
import hashlib

class DirectoryManager:
    """
    Reps and manages a directory of files within our digital archive system

    """

    def __init__(self, directory_path):
        """
        Initialize a DirectoryManager object.

        Args:
            directory_path (str): The path of the directory to manage.

        Raises:
            FileNotFoundError: If the directory does not exist.
        """
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Directory '{directory_path}' does not exist.")
        if not os.path.isdir(directory_path):
            raise ValueError(f"'{directory_path}' is not a directory.")

        self._directory_path = directory_path
        self._last_scanned = None


    @property
    def directory_path(self):
        """str: Get the directory path."""
        return self._directory_path

    @property
    def last_scanned(self):
        """datetime or None: When the directory was last scanned."""
        return self._last_scanned

    def list_files_by_type(self, file_type):
        """
        List all files of a given type in the directory (and subdirectories).

        Args:
            file_type (str): File extension (e.g., ".pdf", ".txt").

        Returns:
            list[str]: List of file paths.
        """
        matches = []
        for root, _, files in os.walk(self._directory_path):
            for f in files:
                if f.lower().endswith(file_type.lower()):
                    matches.append(os.path.join(root, f))
        print(f"Found {len(matches)} {file_type} files in {self._directory_path}")
        self._last_scanned = datetime.now()
        return matches

    def extract_file_metadata(self, file_path):
        """
        Extract metadata from a file (integrates extract_file_metadata from Project 1).

        Args:
            file_path (str): File path.

        Returns:
            dict: Metadata including name, size, type, and timestamps.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"{file_path} does not exist.")

        stat = os.stat(file_path)
        return {
            "name": os.path.basename(file_path),
            "size": f"{stat.st_size / 1024:.2f} KB",
            "type": mimetypes.guess_type(file_path)[0] or "unknown",
            "created": datetime.fromtimestamp(stat.st_ctime),
            "modified": datetime.fromtimestamp(stat.st_mtime),
        }

    def organize_by_metadata(self, metadata_field="type"):
        """
        Organize files in the directory into subfolders based on a metadata field.

        Args:
            metadata_field (str): Field to group by ("type" or "created").

        Returns:
            int: Number of files moved.
        """
        moved_files = 0
        for root, _, files in os.walk(self._directory_path):
            for f in files:
                if f.startswith('.'):
                    continue
                path = os.path.join(root, f)
                meta = self.extract_file_metadata(path)
                field_value = meta.get(metadata_field, "Unknown")

                folder_name = str(field_value).replace(" ", "_").replace("/", "-")
                target_folder = os.path.join(self._directory_path, folder_name)

                os.makedirs(target_folder, exist_ok=True)
                new_path = os.path.join(target_folder, f)

                # Handle conflicts
                if os.path.exists(new_path):
                    base, ext = os.path.splitext(f)
                    counter = 1
                    while os.path.exists(os.path.join(target_folder, f"{base}_{counter}{ext}")):
                        counter += 1
                    new_path = os.path.join(target_folder, f"{base}_{counter}{ext}")

                shutil.move(path, new_path)
                moved_files += 1

        print(f"Moved {moved_files} files into folders based on '{metadata_field}'.")
        return moved_files

    def detect_duplicates(self, remove_duplicates=False):
        """
        Detect duplicate files in the directory using file checksums.

        Args:
            remove_duplicates (bool): If True, delete duplicate files.

        Returns:
            list[tuple]: List of duplicate file pairs.
        """
        checksums = {}
        duplicates = []

        for root, _, files in os.walk(self._directory_path):
            for f in files:
                path = os.path.join(root, f)
                if not os.path.isfile(path):
                    continue

                hasher = hashlib.sha256()
                with open(path, "rb") as file:
                    for chunk in iter(lambda: file.read(4096), b""):
                        hasher.update(chunk)
                checksum = hasher.hexdigest()

                if checksum in checksums:
                    duplicates.append((checksums[checksum], path))
                    if remove_duplicates:
                        os.remove(path)
                else:
                    checksums[checksum] = path

        print(f"Found {len(duplicates)} duplicate pairs.")
        return duplicates

 
    def __str__(self):
        return f"DirectoryManager(path='{self._directory_path}')"

    def __repr__(self):
        return f"<DirectoryManager path='{self._directory_path}'>"
