"""
library_name.py — Digital Archive Management Utility Library

A collection of reusable utility functions for organizing, validating,
and managing digital archives for academic and collaborative projects.
"""

import os
import shutil
import mimetypes
import uuid
import hashlib
from datetime import datetime


################ SIMPLE FUNCTIONS (7) ################

def format_file_size(size_bytes):
    """
    Convert file size in bytes to a human-readable string.

    Args:
        size_bytes (int): File size in bytes.

    Returns:
        str: Formatted size (e.g., '2.3 MB').
    """
    for unit in ["B", "KB", "MB", "GB"]:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} TB"


def generate_unique_identifier():
    """
    Generate a unique identifier for a file.

    Returns:
        str: UUID-based unique ID.
    """
    return str(uuid.uuid4())


def validate_file_path(file_path):
    """
    Validate that a file path exists.

    Args:
        file_path (str)

    Returns:
        bool
    """
    return os.path.isfile(file_path)


def get_file_extension(file_path):
    """
    Get a file's extension.

    Args:
        file_path (str)

    Returns:
        str
    """
    return os.path.splitext(file_path)[1]


def get_file_name(file_path):
    """
    Get a file's base name.

    Args:
        file_path (str)

    Returns:
        str
    """
    return os.path.basename(file_path)


def get_parent_directory(file_path):
    """
    Get parent directory of a file.

    Args:
        file_path (str)

    Returns:
        str
    """
    return os.path.dirname(file_path)


def is_hidden_file(file_path):
    """
    Check if a file is hidden.

    Args:
        file_path (str)

    Returns:
        bool
    """
    return os.path.basename(file_path).startswith(".")


################ MEDIUM FUNCTIONS (5) ################

def extract_file_metadata(file_path):
    """
    Extract metadata from a file including name, size, type, extension,
    folder, and timestamps.

    Raises:
        FileNotFoundError
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist.")

    stat = os.stat(file_path)

    metadata = {
        "name": get_file_name(file_path),
        "size": format_file_size(stat.st_size),
        "type": mimetypes.guess_type(file_path)[0] or "unknown",
        "extension": get_file_extension(file_path),
        "folder": get_parent_directory(file_path),
        "created": datetime.fromtimestamp(stat.st_ctime),
        "modified": datetime.fromtimestamp(stat.st_mtime),
    }
    return metadata


def validate_metadata_fields(metadata, required_fields):
    """
    Ensure required metadata fields exist and are not empty.
    """
    for field in required_fields:
        if field not in metadata or metadata[field] in ("", None):
            return False
    return True


def calculate_file_checksum(file_path, algorithm="sha256"):
    """
    Generate a checksum for a file.
    """
    if algorithm not in ["md5", "sha1", "sha256"]:
        raise ValueError("Unsupported algorithm")

    hasher = getattr(hashlib, algorithm)()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def rename_file_with_id(file_path, unique_id):
    """
    Rename file by appending a unique ID.
    """
    folder = get_parent_directory(file_path)
    base, ext = os.path.splitext(get_file_name(file_path))
    new_path = os.path.join(folder, f"{base}_{unique_id}{ext}")
    os.rename(file_path, new_path)
    return new_path


def list_files_by_type(directory, file_type):
    """
    List files of a specific type in directory and subdirectories.
    """
    matches = []
    for root, _, files in os.walk(directory):
        for f in files:
            if f.lower().endswith(file_type.lower()):
                matches.append(os.path.join(root, f))
    return matches


################ COMPLEX FUNCTIONS (3) ################

def organize_files_by_metadata(directory, metadata_field):
    """
    Organize files into subfolders based on metadata field.
    """
    for root, _, files in os.walk(directory):
        for f in files:
            path = os.path.join(root, f)
            if is_hidden_file(path):
                continue

            meta = extract_file_metadata(path)
            key = str(meta.get(metadata_field, "Unknown")).replace(" ", "_")
            target_dir = os.path.join(directory, key)

            os.makedirs(target_dir, exist_ok=True)
            shutil.move(path, os.path.join(target_dir, f))


def generate_archive_report(directory, output_path):
    """
    Generate archive summary report.
    """
    total_files = 0
    total_size = 0
    type_counts = {}
    largest_files = []

    for root, _, files in os.walk(directory):
        for f in files:
            path = os.path.join(root, f)
            if not os.path.isfile(path):
                continue

            stat = os.stat(path)
            total_files += 1
            total_size += stat.st_size

            ftype = mimetypes.guess_type(path)[0] or "unknown"
            type_counts[ftype] = type_counts.get(ftype, 0) + 1

            largest_files.append((stat.st_size, path))

    largest_files.sort(reverse=True)

    with open(output_path, "w") as report:
        report.write(f"Total Files: {total_files}\n")
        report.write(f"Total Size: {format_file_size(total_size)}\n\n")
        report.write("File Types:\n")
        for t, c in type_counts.items():
            report.write(f"{t}: {c}\n")

        report.write("\nTop 5 Largest Files:\n")
        for size, path in largest_files[:5]:
            report.write(f"{path} ({format_file_size(size)})\n")


def detect_duplicate_files(directory, remove_duplicates=False):
    """
    Detect duplicate files using checksums.
    """
    seen = {}
    duplicates = []

    for root, _, files in os.walk(directory):
        for f in files:
            path = os.path.join(root, f)
            if not os.path.isfile(path):
                continue

            checksum = calculate_file_checksum(path)
            if checksum in seen:
                duplicates.append((seen[checksum], path))
                if remove_duplicates:
                    os.remove(path)
            else:
                seen[checksum] = path

    return duplicates
