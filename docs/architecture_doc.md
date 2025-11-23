# CampusDrive Architecture Document

## Overview
CampusDrive is a Digital Archive Management System designed for organizing, managing, and retrieving digital files efficiently. The system uses advanced object-oriented programming concepts including inheritance, polymorphism, abstract base classes, and composition to ensure code reuse, scalability, and flexibility.

---

## 1. Inheritance Hierarchy

### Abstract Base Class
- **AbstractArchiveItem (ABC)**  
  - Base class for all archive items.
  - Defines two abstract methods:
    - `display_info()`
    - `calculate_size()`
  - Purpose: Enforces a consistent interface for all archive items.


### Derived Classes
- **ArchiveRecord**
  - Represents a single file with metadata (author, size, type, tags).
  - Overrides `display_info()` to show file-specific details.
  - Overrides `calculate_size()` to return file size in KB.
- **ArchiveCollection**
  - Represents a collection of multiple `ArchiveRecord` objects.
  - Overrides `display_info()` to show collection-level details.
  - Overrides `calculate_size()` to sum the sizes of all contained records.
  
**Rationale:**  
`ArchiveRecord` “is-a” `AbstractArchiveItem`, and `ArchiveCollection` also “is-a” `AbstractArchiveItem` since a collection behaves like an archive item at a higher level. This hierarchy allows polymorphic handling of individual files and collections uniformly.

-------------------------------------------------

## 2. Polymorphism

Polymorphism is demonstrated via the `display_info()` and `calculate_size()` methods:

**ArchiveRecord**
- Represents a single file with metadata (name, author, size, type, timestamps, tags).
- Overrides display_info() to show file-specific details.
- Overrides calculate_size() to return the size of the individual file in KB.

**ArchiveCollection**
- Represents a collection of multiple ArchiveRecord objects.
- Overrides display_info() to show collection-level details, such as the names of all contained records.
- Overrides calculate_size() to return the total size of all contained files

> **Benefit:** Code can operate on `AbstractArchiveItem` references without needing to know the concrete type.

-------------------------------------------------

## 3. Composition Relationships

- **ArchiveCollection has ArchiveRecord objects**
  - A collection “has-a” set of records.
  - Chosen over inheritance because a collection is not a file, but it manages multiple files.

- **User has ArchiveCollection objects**
  - A user “has-a” set of collections.
  - Chosen because users organize and interact with collections, but a user is not a collection.

**Rationale:** Composition allows modeling real-world relationships directly and encourages modular, reusable code.

-----------------------------------------

## 4. Design Patterns and Principles

- **Single Responsibility Principle**
  - `ArchiveRecord` handles individual file metadata.
  - `ArchiveCollection` manages groups of files.
  - `User` manages collections and activity logs.

- **Open/Closed Principle**
  - New types of archive items can be added by extending `AbstractArchiveItem` without modifying existing code.

- **DRY (Don't Repeat Yourself)**
  - Polymorphic methods (`display_info`, `calculate_size`) avoid code duplication between records and collections.

