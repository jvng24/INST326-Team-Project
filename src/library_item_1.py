import os
import shutil
import mimetypes
import hashlib
from datetime import datetime
from archive_record import ArchiveRecord


class DirectoryManager:
    """
    Manages a directory of files within the digital archive system.
    """

    def __init__(self, directory_path: str):
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Directory '{directory_path}' does not exist.")
        if not os.path.isdir(directory_path):
            raise ValueError(f"'{directory_path}' is not a directory.")

        self._directory_path = directory_path
        self._last_scanned = None

    # ---------- Properties ----------

    @property
    def directory_path(self) -> str:
        return self._directory_path

    @property
    def last_scanned(self):
        return self._last_scanned

    # ---------- Core Functionality ----------

    def scan_records(self) -> list[ArchiveRecord]:
        """
        Scan the directory and return ArchiveRecord objects.
        """
        records = []
        for root, _, files in os.walk(self._directory_path):
            for f in files:
                if f.startswith("."):
                    continue
                path = os.path.join(root, f)
                try:
                    records.append(ArchiveRecord(path))
                except FileNotFoundError:
                    continue

        self._last_scanned = datetime.now()
        return records

    def list_files_by_type(self, file_type: str) -> list[str]:
        matches = []
        for root, _, files in os.walk(self._directory_path):
            for f in files:
                if f.lower().endswith(file_type.lower()):
                    matches.append(os.path.join(root, f))

        self._last_scanned = datetime.now()
        return matches

    def extract_file_metadata(self, file_path: str) -> dict:
        stat = os.stat(file_path)
        return {
            "name": os.path.basename(file_path),
            "size_kb": round(stat.st_size / 1024, 2),
            "type": mimetypes.guess_type(file_path)[0] or "unknown",
            "created": datetime.fromtimestamp(stat.st_ctime),
            "modified": datetime.fromtimestamp(stat.st_mtime),
        }

    def organize_by_metadata(self, metadata_field: str = "type") -> list[tuple]:
        """
        Organize files into subfolders based on metadata.
        Returns list of (old_path, new_path).
        """
        moved = []

        files_to_process = []
        for root, _, files in os.walk(self._directory_path):
            for f in files:
                if f.startswith("."):
                    continue
                files_to_process.append(os.path.join(root, f))

        for path in files_to_process:
            meta = self.extract_file_metadata(path)
            value = str(meta.get(metadata_field, "Unknown")).replace(" ", "_")
            target_folder = os.path.join(self._directory_path, value)
            os.makedirs(target_folder, exist_ok=True)

            new_path = os.path.join(target_folder, os.path.basename(path))
            if os.path.exists(new_path):
                base, ext = os.path.splitext(new_path)
                counter = 1
                while os.path.exists(f"{base}_{counter}{ext}"):
                    counter += 1
                new_path = f"{base}_{counter}{ext}"

            shutil.move(path, new_path)
            moved.append((path, new_path))

        return moved

    def detect_duplicates(self, remove_duplicates: bool = False) -> list[tuple]:
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

        return duplicates

    # ---------- String Representations ----------

    def __str__(self):
        return f"DirectoryManager(path='{self._directory_path}')"

    def __repr__(self):
        return f"<DirectoryManager path='{self._directory_path}'>"
