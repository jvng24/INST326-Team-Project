

```python
from src.library_name import (
    extract_file_metadata,
    validate_metadata_fields,
    calculate_file_checksum,
    rename_file_with_id,
    list_files_by_type,
    organize_files_by_metadata,
    generate_archive_report,
    detect_duplicate_files
)


# SIMPLE FUNCTIONS









# MEDIUM FUNCTIONS

metadata = extract_file_metadata("demo_files/report.pdf")
print("Metadata:", metadata)

required_fields = ["name", "size", "type", "created"]
if validate_metadata_fields(metadata, required_fields):
    print("All required metadata fields are present!")
else:
    print("Some metadata fields are missing or empty.")

checksum_md5 = calculate_file_checksum("demo_files/report.pdf", "md5")
checksum_sha256 = calculate_file_checksum("demo_files/report.pdf", "sha256")
print(f"MD5: {checksum_md5}")
print(f"SHA256: {checksum_sha256}")

new_file_path = rename_file_with_id("demo_files/report.pdf", "DOC-123")
print(f"File renamed to: {new_file_path}")

pdf_files = list_files_by_type("demo_files", ".pdf")
print(f"Found PDF files: {pdf_files}")





# COMPLEX FUNCTIONS

organize_files_by_metadata("demo_files", "type")
print("Files have been organized by type into subfolders.")

output_report = "demo_files/archive_report.txt"
generate_archive_report("demo_files", output_report)
print(f"Archive report generated at: {output_report}")

duplicates = detect_duplicate_files("demo_files")
if duplicates:
    print("Duplicate files detected:")
    for dup1, dup2 in duplicates:
        print(f"  {dup1} and {dup2}")
else:
    print("No duplicate files found.")



#CLASS 1

student = Student("Juliana Nguyen", 10234, 3.2)
print(f"Created student: {student}")

student.update_gpa(3.8)
print(f"GPA updated to: {student.gpa}")

if student.is_honors():
    print(f"{student.name} qualifies for honors!")
else:
    print(f"{student.name} does not qualify for honors.")

print("Final student record:", student)

