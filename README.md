# INST326-Team-Project

# Project Title and Description
- Name: CampusDrive 
- Description: As college students, we’ve noticed that digital files can get lost, mislabeled, or become difficult to find. Whether it’s academic research, media files, or scanned documents, there isn’t a consistent or reliable way to store and retrieve files efficiently. This issue is important because it can lead to the loss of important work, wasted time, and difficulties when collaborating in groups. The project’s foundation is a function library that provides reusable utilities for file organization, metadata management, and data integrity.

# Team Member Names and Roles
- Juliana Nguyen
- Manasa Chekuri
- Nathaly Robles

# Domain Focus and Problem Statement
- Our project focuses on Digital Archive Management for schools and large groups. The goal is to improve the organization, storage, and retrieval of digital files such as research papers, media files, scanned documents, and collaborative project resources. By providing a structured and secure way to manage files, our system supports better workflow, reduces time spent searching for documents, and ensures important work is preserved and easily shareable. 


# Installation and Setup Instructions
- Save file as library_name.py
- import os
- import uuid
- file_path = "C:/Users/Example/Documents/report1.pdf"



# Usage Examples for Key Functions
- In extract file metadata you can get details about a file. This could be things such as its name, size, type, extension, folder location, and timestamps. For example, extracting metadata from report.pdf will tell you when it was created, modified, and its file type
- In Validate metadata fields, after extracting metadata, you can check if all required fields exist and are not empty. For example, you might make sure that the file has name, size, type, and created fields before processing it further.


# Function Library Overview and Organization

- Medium Complexity --> These functions handle common tasks related to file management and metadata:
    - extract_file_metadata: Retrieves metadata from files
    - validate_metadata_fields: Ensures required metadata fields exist and are valid.
    - calculate_file_checksum: Generates checksums to verify file integrity or detect duplicates.
    - rename_file_with_id: Renames files to include a unique identifier.
    - list_files_by_type: Lists all files of a specific type in a folder.

- Complex Functions --> These functions perform larger-scale operations, often involving multiple files or complex processing:
    - organize_files_by_metadata: Automatically sorts files into subfolders based on metadata.
    - generate_archive_report: Produces a detailed summary report of a folder’s contents, including file counts, sizes, and types
    - detect_duplicate_files: Identifies duplicate files within a directory using checksums.


# Contribution Guidelines for Team Members 
- Juliana = I did the README as well as the examples, and functiosn for the medium and complex functions. 

## Nathaly Robles - Digital Archives Management System

For my part of the project I did the last 3 simple functions. I also updated the readme. 

## Functions implemeted

- format_file_size()
- generate_unique_id()
- get_file_name_without_extension()

## Manasa Chekuri - Digital Archives Management System

For my part of the project I added 5 more functions that ensure our code aligns with our topic and build off what Nathaly started.

## Functions Added
1. 'filter_archive_by_author(archive_records, author_name)'
2. 'edit_metadata(record_id, updated_fields, archive_db)'
3. 'search_files_by_keyword(archive_records, keyword)'
4. 'backup_archive_database(source_path, backup_path)'
5. 'generate_storage_report(archive_records)'
