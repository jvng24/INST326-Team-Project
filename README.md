# INST326 – Team Project

## CampusDrive: Digital Archive Management System

---

## Project Overview

**CampusDrive** is a digital archive management system designed to help students and collaborative groups organize, store, and retrieve digital files efficiently. As college students, we observed that files are often lost, mislabeled, duplicated, or difficult to locate across personal devices and shared folders. This leads to wasted time, poor collaboration, and potential loss of important academic work.

CampusDrive addresses these challenges by combining:

* A reusable **function library** for file and metadata management
* An **object-oriented archive system** (records, collections, users)
* Tools for **searching, organizing, validating, backing up, and reporting** on files

Together, these components create a scalable, user-friendly digital archive suitable for schools and large group projects.

---

## Team Members and Contributions

* **Juliana Nguyen**

  * Wrote and structured the README documentation
  * Implemented medium- and complex-level functions in the function library
  * Created usage examples and reporting utilities

* **Nathaly Robles**

  * Implemented simple utility functions
  * Updated and refined README documentation
  * Contributed to core file-handling logic

* **Manasa Chekuri**

  * Expanded the function library with advanced archive operations
  * Designed and implemented object-oriented archive components (records, collections, users)

---

## Domain Focus and Problem Statement

**Domain:** Digital Archive Management for academic institutions and collaborative environments.

**Problem:** Digital files such as research papers, media, scanned documents, and group resources are frequently disorganized, duplicated, or lost. Existing folder systems do not scale well and lack consistent metadata, searchability, and integrity checks.

**Solution:** CampusDrive provides a structured archive system that:

* Stores files with consistent metadata
* Enables keyword, author, and type-based searching
* Detects duplicates and validates file integrity
* Supports collections, users, and scalable organization

---

## Installation and Setup

1. Save the main utility library as:

   ```
   library_name.py
   ```

2. Ensure Python 3 is installed.

3. Place files to be managed inside a directory on your system.

4. Example setup:

   ```python
   file_path = "C:/Users/Example/Documents/report1.pdf"
   ```

---

## System Architecture

CampusDrive consists of **two major components**:

### 1. Function Library

A reusable set of simple, medium, and complex functions for file handling and analysis.

### 2. Object-Oriented Archive System

Classes that represent real-world archive entities:

* `ArchiveRecord` – individual files
* `ArchiveCollection` – groups of records
* `User` – users who manage collections
* `DirectoryManager` – manages directories and filesystem operations

---

## Function Library Overview

### Simple Functions

* `count_total_files(archive_records)`
* `get_file_extension(file_name)`
* `validate_file_format(file_path, allowed_formats)`
* `filter_archive_by_author(archive_records, author_name)`
* `format_file_size(size_bytes)`
* `generate_unique_id(prefix)`
* `get_file_name_without_extension(file_path)`

These functions perform basic validation, formatting, and filtering tasks.

---

### Medium-Complexity Functions

* `extract_file_metadata(file_path)`
  Retrieves file name, size, type, extension, folder, and timestamps.

* `validate_metadata_fields(metadata, required_fields)`
  Ensures required metadata exists and is valid.

* `calculate_file_checksum(file_path, algorithm)`
  Generates hashes for integrity verification and duplicate detection.

* `rename_file_with_id(file_path, unique_id)`
  Renames files using unique identifiers.

* `list_files_by_type(directory, file_type)`
  Recursively finds files by extension.

---

### Complex Functions

* `organize_files_by_metadata(directory, metadata_field)`
  Automatically sorts files into subfolders based on metadata.

* `generate_archive_report(directory, output_path)`
  Creates a detailed report including file counts, sizes, types, and trends.

* `detect_duplicate_files(directory, remove_duplicates)`
  Identifies duplicate files using checksums and optionally removes them.

* `backup_archive_database(source_path, backup_path)`
  Creates a backup of the archive for data protection.

* `generate_storage_report(archive_records)`
  Summarizes archive size and storage usage.

---

## Object-Oriented Archive System

### Abstract Base Class

* `AbstractArchiveItem`
  Defines required methods (`display_info`, `calculate_size`) for archive items.

---

### ArchiveRecord

Represents a single file and its metadata.

**Features:**

* Unique ID assignment
* Metadata extraction
* Author and tag support
* Keyword searching
* Metadata editing

---

### ArchiveCollection

Groups related `ArchiveRecord` objects.

**Features:**

* Add and remove records
* Search by author or keyword
* Collection summaries
* Size calculations

---

### User

Represents a system user who owns collections.

**Features:**

* User roles (Viewer, Archivist)
* Multiple collections
* Activity logging
* Collection management

---

### DirectoryManager

Handles filesystem-level operations.

**Features:**

* Lists files by type
* Extracts metadata
* Organizes directories
* Detects and removes duplicates
* Tracks scan history

---

## Key Features Implemented

* File upload and storage
* Metadata extraction and editing
* Keyword, author, and type-based search
* Duplicate detection using checksums
* Automatic directory organization
* Archive reporting and summaries
* Backup and data integrity tools
* Scalable object-oriented design

---

## Project Goals Achieved

✔ Centralized digital archive
✔ Searchable metadata system
✔ File integrity and duplicate protection
✔ Scalable and modular design
✔ Professional documentation and structure

---

## Conclusion

CampusDrive demonstrates a complete digital archive management solution that integrates functional programming, object-oriented design, and real-world file system operations. The project showcases teamwork, scalability, and professional software development practices aligned with real academic and collaborative needs.
