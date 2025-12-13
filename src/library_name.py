"""
library_name.py — Digital Archive Management Utility Library

A collection of simple, intermediate-level functions to help organize,
manage, and retrieve digital files for academic and collaborative projects.
"""

import os
import shutil
import mimetypes
import uuid
from datetime import datetime
import hashlib


############ SIMPLE FUNCTIONS (7) ##############

def count_total_files(archive_records):
    """Return the total number of files in the archive."""
    return len(archive_records)


def get_file_extension(file_name):
    """Return the file extension from a given file name."""
    return '.' + file_name.split('.')[-1] if '.' in file_name else ''


def validate_file_format(file_path, allowed_formats=None):
    """Check if a file's extension is allowed."""
    if allowed_formats is None:
        allowed_formats = ['.pdf', '.jpg', '.png']
    return any(file_path.lower().endswith(ext) for ext in allowed_formats)


def filter_archive_by_author(archive_records, author_name):
    """Return all files created by a specific author."""
    return [
        record for record in archive_records
        if author_name.lower() in record.get("author", "").lower()
    ]


def format_file_size(size_bytes):
    """Convert file size in bytes to a human-readable format."""
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} PB"


def generate_unique_id(prefix="FILE"):
    """Generate a short unique ID."""
    return f"{prefix}-{uuid.uuid4().hex[:8]}"


def get_file_name_without_extension(file_path):
    """Return the file name without its extension."""
    return os.path.splitext(os.path.basename(file_path))[0]


########### MEDIUM FUNCTIONS (5) ##############

def extract_file_metadata(file_path):
    """Extract metadata from a file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist.")

    stat = os.stat(file_path)

    return {
        "name": os.path.basename(file_path),
        "size": format_file_size(stat.st_size),
        "type": mimetypes.guess_type(file_path)[0] or "unknown",
        "extension": os.path.splitext(file_path)[1],
        "folder": os.path.dirname(file_path),
        "created": datetime.fromtimestamp(stat.st_ctime),
        "modified": datetime.fromtimestamp(stat.st_mtime),
    }


def validate_metadata_fields(metadata, required_fields):
    """Ensure required metadata fields exist and are not empty."""
    for field in required_fields:
        if field not in metadata or metadata[field] in (None, ""):
            return False
    return True


def calculate_file_checksum(file_path, algorithm="sha256"):
    """Calculate a file checksum."""
    if algorithm not in ("md5", "sha1", "sha256"):
        raise ValueError(f"Unsupported algorithm: {algorithm}")

    hasher = getattr(hashlib, algorithm)()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)

    return hasher.hexdigest()


def rename_file_with_id(file_path, unique_id):
    """Rename a file to include a unique ID."""
    folder = os.path.dirname(file_path)
    base, ext = os.path.splitext(os.path.basename(file_path))
    new_path = os.path.join(folder, f"{base}_{unique_id}{ext}")
    os.rename(file_path, new_path)
    return new_path


def list_files_by_type(directory, file_type):
    """List all files of a specific type in a directory."""
    matches = []
    for root, _, files in os.walk(directory):
        for f in files:
            if f.lower().endswith(file_type.lower()):
                matches.append(os.path.join(root, f))
    return matches


################ COMPLEX FUNCTIONS (3) ##################

def organize_files_by_metadata(directory, metadata_field):
    """Organize files into folders based on a metadata field."""
    moved_files = []

    for root, _, files in os.walk(directory):
        for f in files:
            if f.startswith('.'):
                continue

            path = os.path.join(root, f)
            meta = extract_file_metadata(path)
            field_value = str(meta.get(metadata_field, "Unknown")).replace(" ", "_")

            target_folder = os.path.join(directory, field_value)
            os.makedirs(target_folder, exist_ok=True)

            new_path = os.path.join(target_folder, f)
            counter = 1
            while os.path.exists(new_path):
                base, ext = os.path.splitext(f)
                new_path = os.path.join(target_folder, f"{base}_{counter}{ext}")
                counter += 1

            shutil.move(path, new_path)
            moved_files.append((path, new_path))

    return moved_files


def generate_archive_report(directory, output_path):
    """Generate a summary report of archive contents."""
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
        report.write("Files by Type:\n")
        for t, c in type_counts.items():
            report.write(f"  {t}: {c}\n")
        report.write("\nTop 5 Largest Files:\n")
        for size, path in largest_files[:5]:
            report.write(f"  {path} ({format_file_size(size)})\n")


def detect_duplicate_files(directory, remove_duplicates=False):
    """Detect duplicate files using checksums."""
    checksums = {}
    duplicates = []

    for root, _, files in os.walk(directory):
        for f in files:
            if f.startswith('.'):
                continue

            path = os.path.join(root, f)
            checksum = calculate_file_checksum(path)

            if checksum in checksums:
                duplicates.append((checksums[checksum], path))
                if remove_duplicates:
                    os.remove(path)
            else:
                checksums[checksum] = path

    return duplicates
