# Exercise 1 – Student Class

## Overview

This project implements a simple Python class called `Student`.
The class models a student with a name, student ID, and a list of enrolled courses.

The project also includes a unit test to verify that enrolling in a course correctly updates the student's course list.

---

## Features

### Student class

The `Student` class provides the following functionality:

* **Attributes**

  * `name`: The student's name
  * `student_id`: A unique identifier for the student
  * `courses`: A list of courses the student is enrolled in

* **Methods**

  * `enroll(course)`: Adds a course to the student's list of courses
  * `get_courses()`: Returns the list of enrolled courses

The class uses the `__init__` method to initialize the data members.

---

## Project Structure

```
exercise1/
├── exercise1/
│   ├── __init__.py
│   └── exercises.py
├── tests/
│   └── test_main.py
├── environment.yml
├── setup.py
└── README.md
```

---

## Setup

### 1. Create the conda environment

```
conda env create -f environment.yml
conda activate exercise1
```

### 2. Install the package

Install the project in editable mode:

```
pip install -e .
```

---

## Running the Code

You can run Python and create a `Student` object manually:

```python
from exercise1.exercises import Student

student = Student("Claudia", 123)
student.enroll("course1")

print(student.get_courses())
```

---

## Running Tests

The project includes a test to verify that enrolling in a course increases the number of courses.

Run the tests with:

```
python -m pytest
```

---

## Example Test

The test checks that calling `enroll()` adds a new course:

```python
def test_enrollment():
    student = Student("Claudia", 123)
    len1 = len(student.courses)
    student.enroll("course1")
    len2 = len(student.courses)
    assert len2 - len1 == 1
```

---

## Notes

* The class includes basic docstrings and simple error handling.
* The project is managed with Git and includes an environment file for reproducibility.
