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




############ SIMPLE FUNCTIONS (7) ##############

def count_total_files(archive_records):
    """Return the total number of files in the archive.
    
    Args:
        archive_records (list): A list of all file records.
    
    Returns:
        int: The total number of files.
    """
    return len(archive_records)


def get_file_extension(file_name):
    """Return the file extension from a given file name.
    
    Args:
        file_name (str): The name of the file.
    
    Returns:
        str: The file's extension (e.g., '.pdf').
    """
    return '.' + file_name.split('.')[-1] if '.' in file_name else ''


def validate_file_format(file_path, allowed_formats=None):
    """Check if a file's format is allowed.
    
    Args:
        file_path (str): Path or name of the file.
        allowed_formats (list, optional): List of valid formats. Defaults to ['.pdf', '.jpg', '.png'].
    
    Returns:
        bool: True if the file is in an allowed format, False otherwise.
    """
    if allowed_formats is None:
        allowed_formats = ['.pdf', '.jpg', '.png']
    return any(file_path.lower().endswith(ext) for ext in allowed_formats)


def filter_archive_by_author(archive_records, author_name):
    """Return all files created by a specific author.
    
    Args:
        archive_records (list[dict]): List of file records.
        author_name (str): Author to search for.
    
    Returns:
        list[dict]: Files that match the author name.
    """
    return [record for record in archive_records if author_name.lower() in record.get("author", "").lower()]








########### MEDIUM FUNCTIONS (5) ##############


def extract_file_metadata(file_path):
    """
    Extract metadata from a file including name, size, type, and timestamps.

    Args:
        file_path (str): Path to the file.

    Returns:
        dict: Metadata including name, size, type, created, modified.

    Raises:
        FileNotFoundError: If the file does not exist.

    Example:
        extract_file_metadata("/home/user/docs/report.pdf")
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist.")

    stat = os.stat(file_path)
    file_size = format_file_size(stat.st_size)
    file_type = mimetypes.guess_type(file_path)[0] or "unknown"
    created = datetime.fromtimestamp(stat.st_ctime)
    modified = datetime.fromtimestamp(stat.st_mtime)

    # extra info: extension and folder
    base_name = os.path.basename(file_path)
    ext = os.path.splitext(file_path)[1]
    folder = os.path.dirname(file_path)

    metadata = {
        "name": base_name,
        "size": file_size,
        "type": file_type,
        "extension": ext,
        "folder": folder,
        "created": created,
        "modified": modified
    }

    # optionally print metadata for debugging
    print(f"Extracted metadata for {base_name}: {metadata}")

    return metadata




def validate_metadata_fields(metadata, required_fields):
    """
    Ensure all required metadata fields exist and are not empty.

    Args:
        metadata (dict): Metadata dictionary.
        required_fields (list of str): Keys that must exist.

    Returns:
        bool: True if all required fields are present and not empty, False otherwise.

    Example:
        validate_metadata_fields({'name': 'file.pdf', 'size': '12 KB'}, ['name', 'size'])
    """
    missing = []
    for field in required_fields:
        if field not in metadata or metadata[field] in [None, ""]:
            missing.append(field)

    if missing:
        print(f"Missing or empty metadata fields: {missing}")
        return False

    # optional: extra check for string length
    for k, v in metadata.items():
        if isinstance(v, str) and len(v) > 255:
            print(f"Warning: {k} seems unusually long")

    return True




def calculate_file_checksum(file_path, algorithm="sha256"):
    """
    Calculate a file checksum for duplicate detection or integrity verification.

    Args:
        file_path (str): Path to the file.
        algorithm (str, optional): Hash type ("md5", "sha1", "sha256").

    Returns:
        str: Hexadecimal hash of the file.

    Raises:
        ValueError: If the algorithm is unsupported.

    Example:
        calculate_file_checksum("report.pdf", "md5")
    """
    import hashlib

    if algorithm not in ["md5", "sha1", "sha256"]:
        raise ValueError(f"Unsupported algorithm: {algorithm}")

    hasher = getattr(hashlib, algorithm)()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)

    # optional: print hash for debugging
    checksum = hasher.hexdigest()
    print(f"{algorithm} checksum for {file_path}: {checksum}")
    return checksum


def rename_file_with_id(file_path, unique_id):
    """
    Rename a file to include a unique ID before the extension.

    Args:
        file_path (str): Original file path.
        unique_id (str): Unique ID to append.

    Returns:
        str: New file path.

    Example:
        rename_file_with_id("report.pdf", "DOC-123")
    """
    folder = os.path.dirname(file_path)
    base, ext = os.path.splitext(os.path.basename(file_path))
    new_name = f"{base}_{unique_id}{ext}"
    new_path = os.path.join(folder, new_name)
    os.rename(file_path, new_path)
    print(f"Renamed {file_path} -> {new_path}")
    return new_path




def list_files_by_type(directory, file_type):
    """
    List all files of a specific type in a directory and subdirectories.

    Args:
        directory (str): Path to the folder.
        file_type (str): File extension (e.g., ".pdf").

    Returns:
        list of str: Paths of matching files.

    Example:
        list_files_by_type("/home/user/docs", ".pdf")
    """
    matches = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.lower().endswith(file_type.lower()):
                matches.append(os.path.join(root, f))
    print(f"Found {len(matches)} {file_type} files in {directory}")
    return matches



################ COMPLEX FUNCTIONS (3) ##################


def organize_files_by_metadata(directory, metadata_field):
    """
    Organize files in a directory (and subdirectories) into subfolders 
    based on a specific metadata field.

    Args:
        directory (str): Path to the directory containing files.
        metadata_field (str): Metadata field for grouping (e.g., 'type', 'created').

    Raises:
        FileNotFoundError: If a file in the directory does not exist.

    Example:
        organize_files_by_metadata("/home/user/docs", "type")
    """
    moved_files = []

    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.startswith('.'):
                continue  # skip hidden files
            path = os.path.join(root, f)
            if not os.path.exists(path):
                raise FileNotFoundError(f"{path} does not exist.")

            meta = extract_file_metadata(path)
            field_value = meta.get(metadata_field, "Unknown")
            folder_name = str(field_value).replace(" ", "_")
            target_folder = os.path.join(directory, folder_name)

            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            # handle filename conflicts
            new_path = os.path.join(target_folder, f)
            if os.path.exists(new_path):
                base, ext = os.path.splitext(f)
                counter = 1
                while os.path.exists(os.path.join(target_folder, f"{base}_{counter}{ext}")):
                    counter += 1
                new_path = os.path.join(target_folder, f"{base}_{counter}{ext}")

            shutil.move(path, new_path)
            moved_files.append((path, new_path))

    print(f"Moved {len(moved_files)} files into folders based on {metadata_field}.")
 


def generate_archive_report(directory, output_path):
    """
    Generate a detailed summary report of all files in a directory and save it.

    Args:
        directory (str): Directory to scan.
        output_path (str): File path for saving the report.

    Example:
        generate_archive_report("/home/user/docs", "/home/user/docs/report.txt")
    """
    total_files = 0
    total_size = 0
    type_counts = {}
    monthly_counts = {}
    largest_files = []

    for root, dirs, files in os.walk(directory):
        for f in files:
            path = os.path.join(root, f)
            if not os.path.isfile(path):
                continue
            try:
                stat = os.stat(path)
            except FileNotFoundError:
                print(f"Warning: {path} not found.")
                continue

            total_files += 1
            size = stat.st_size
            total_size += size

            ftype = mimetypes.guess_type(path)[0] or "unknown"
            type_counts[ftype] = type_counts.get(ftype, 0) + 1

            month = datetime.fromtimestamp(stat.st_ctime).strftime("%Y-%m")
            monthly_counts[month] = monthly_counts.get(month, 0) + 1

            largest_files.append((size, path))

    largest_files.sort(reverse=True)
    top5 = largest_files[:5]

    with open(output_path, "w") as report:
        report.write(f"Archive Report for: {directory}\n")
        report.write(f"Total Files: {total_files}\n")
        report.write(f"Total Size: {format_file_size(total_size)}\n")
        report.write("\nFiles by Type:\n")
        for t, c in type_counts.items():
            report.write(f"  {t}: {c}\n")
        report.write("\nFiles by Month Created:\n")
        for m, c in monthly_counts.items():
            report.write(f"  {m}: {c}\n")
        report.write("\nTop 5 Largest Files:\n")
        for s, p in top5:
            report.write(f"  {p} ({format_file_size(s)})\n")




def detect_duplicate_files(directory, remove_duplicates=False):
    """
    Detect duplicate files in a directory using checksums and optionally remove them.

    Args:
        directory (str): Directory to scan.
        remove_duplicates (bool, optional): If True, delete duplicates. Default False.

    Returns:
        list of tuples: Each tuple contains paths of duplicate files.

    Example:
        duplicates = detect_duplicate_files("/home/user/docs")
    """
    checksums = {}
    duplicates = []

    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.startswith('.'):
                continue
            path = os.path.join(root, f)
            if not os.path.isfile(path):
                continue
            try:
                checksum = calculate_file_checksum(path)
            except FileNotFoundError:
                print(f"Warning: {path} not found.")
                continue

            if checksum in checksums:
                duplicates.append((checksums[checksum], path))
                if remove_duplicates:
                    os.remove(path)
            else:
                checksums[checksum] = path

    print(f"Found {len(duplicates)} duplicate file pairs.")
    return duplicates










