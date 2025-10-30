# Simple function references 









### extract_file_metadata
**Purpose:** Extract metadata from a file including name, size, type, extension, folder, and timestamps.

**Parameters:**  
- `file_path` (str): Path to the file.

**Returns:**  
- `dict`: Metadata including name, size, type, extension, folder, created, modified.

**Raises:**  
- `FileNotFoundError`: If the file does not exist.


----------------------------------------------------------

### validate_metadata_fields
**Purpose:** Ensure all required metadata fields exist and are not empty.

**Parameters:**  
- `metadata` (dict)  
- `required_fields` (list of str)

**Returns:**  
- `bool`: True if all required fields are present and not empty, False otherwise.


----------------------------------------------------------
### calculate_file_checksum
**Purpose:** Generate a checksum for a file using a specified algorithm for integrity verification or duplicate detection.

**Parameters:**  
- `file_path` (str)  
- `algorithm` (str, optional): "md5", "sha1", or "sha256" (default `"sha256"`)

**Returns:**  
- `str`: Hexadecimal hash of the file.

**Raises:**  
- `ValueError`: If the algorithm is unsupported.


----------------------------------------------------------

### rename_file_with_id
**Purpose:** Rename a file to include a unique ID before its extension.

**Parameters:**  
- `file_path` (str)  
- `unique_id` (str)

**Returns:**  
- `str`: New file path.


----------------------------------------------------------

### list_files_by_type
**Purpose:** List all files of a specific type in a directory and subdirectories.

**Parameters:**  
- `directory` (str)  
- `file_type` (str): File extension (e.g., ".pdf")

**Returns:**  
- `list of str`: Paths of matching files.


----------------------------------------------------------

## COMPLEX FUNCTIONS (30+ lines)

### organize_files_by_metadata
**Purpose:** Organize files (including subfolders) based on a specified metadata field.

**Parameters:**  
- `directory` (str)  
- `metadata_field` (str)

**Returns:**  
- None

**Raises:**  
- `FileNotFoundError`: If a file does not exist.


----------------------------------------------------------

### generate_archive_report
**Purpose:** Generate a detailed archive report including file count, total size, file types, month created, and top 5 largest files.

**Parameters:**  
- `directory` (str)  
- `output_path` (str)

**Returns:**  
- None


----------------------------------------------------------

### detect_duplicate_files
**Purpose:** Detect duplicate files in a directory using checksums; optionally remove duplicates.

**Parameters:**  
- `directory` (str)  
- `remove_duplicates` (bool, optional, default False)

**Returns:**  
- `list of tuples`: Each tuple contains paths of duplicate files.



##### CLASS REFERENCE #######

**CLASS NAME:** `Student`  
**Description:** Represents a student with attributes and methods for updating academic performance, checking honors eligibility, and displaying information


### __init__
**Purpose:** Initialize a new student with a name, student ID, and GPA.

**Parameters:**  
- `name` (str): The student’s full name.  
- `student_id` (int): The unique student identification number.  
- `gpa` (float): The student’s current GPA.

**Returns:**  
- None

### update_gpa
**Purpose:** Update the student’s GPA value if it is within a valid range (0.0–4.0).

**Parameters:**  
- `new_gpa` (float): The new GPA value to assign.

**Returns:**  
- None

**Raises:**  
- `ValueError`: If the new GPA is not between 0.0 and 4.0.


### is_honors
**Purpose:** Determine whether the student qualifies for the honors list.

**Parameters:**  
- None

**Returns:**  
- `bool`: True if the student’s GPA is 3.5 or higher, otherwise False.


### __str__
**Purpose:** Provide a readable string representation of the student object for display purposes.

**Parameters:**  
- None

**Returns:**  
- `str`: A formatted string showing the student’s name, ID, and GPA.
