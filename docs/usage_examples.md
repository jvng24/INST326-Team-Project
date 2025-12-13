```python
# ==============================
# IMPORTS
# ==============================

from src.library_name import (
    extract_file_metadata,
    validate_metadata_fields,
    calculate_file_checksum,
    rename_file_with_id,
    list_files_by_type,
    organize_files_by_metadata,
    generate_archive_report,
    detect_duplicate_files,
    Student,
    ArchiveRecord,
    ArchiveCollection,
    User
)

from datetime import datetime


# ==============================
# SIMPLE FUNCTIONS
# ==============================

print("\n--- SIMPLE FUNCTION TESTS ---")

metadata = extract_file_metadata("demo_files/report.pdf")
print("Metadata:", metadata)

required_fields = ["name", "size", "type", "created"]
if validate_metadata_fields(metadata, required_fields):
    print("All required metadata fields are present.")
else:
    print("Missing required metadata fields.")

checksum_md5 = calculate_file_checksum("demo_files/report.pdf", "md5")
checksum_sha256 = calculate_file_checksum("demo_files/report.pdf", "sha256")
print(f"MD5 Checksum: {checksum_md5}")
print(f"SHA256 Checksum: {checksum_sha256}")

new_file_path = rename_file_with_id("demo_files/report.pdf", "DOC-123")
print(f"File renamed to: {new_file_path}")

pdf_files = list_files_by_type("demo_files", ".pdf")
print("PDF files found:", pdf_files)


# ==============================
# MEDIUM FUNCTIONS (INTEGRATION LOGIC)
# ==============================

print("\n--- MEDIUM FUNCTION USAGE ---")

# Metadata validation reused inside ArchiveRecord
record = ArchiveRecord("demo_files/report.pdf")
print("ArchiveRecord created:")
print(record)

# Assign unique ID (nice-to-have requirement)
record.assign_unique_id("REC-001")
print("Updated record with unique ID:")
print(record)


# ==============================
# COMPLEX FUNCTIONS
# ==============================

print("\n--- COMPLEX FUNCTION TESTS ---")

organize_files_by_metadata("demo_files", "type")
print("Files organized by file type.")

report_output = "demo_files/archive_report.txt"
generate_archive_report("demo_files", report_output)
print(f"Archive report generated at: {report_output}")

duplicates = detect_duplicate_files("demo_files")
if duplicates:
    print("Duplicate files detected:")
    for file1, file2 in duplicates:
        print(f" - {file1} and {file2}")
else:
    print("No duplicate files found.")


# ==============================
# CLASS INTEGRATION TESTS
# ==============================

print("\n--- CLASS INTEGRATION TESTS ---")

# ArchiveCollection (composition: has ArchiveRecords)
collection = ArchiveCollection("Research Reports")
collection.add_record(record)
print("ArchiveCollection created:")
print(collection)

# User (composition: has collections)
user = User("juliana")
user.add_collection(collection)

print(f"User '{user.username}' manages the following collections:")
for c in user.collections:
    print(f" - {c.name}")


# ==============================
# STUDENT CLASS TEST
# ==============================

print("\n--- STUDENT CLASS TEST ---")

student = Student("Juliana Nguyen", 10234, 3.2)
print("Created student:", student)

student.update_gpa(3.8)
print("Updated GPA:", student.gpa)

if student.is_honors():
    print(f"{student.name} qualifies for honors.")
else:
    print(f"{student.name} does not qualify for honors.")

print("Final student record:", student)
