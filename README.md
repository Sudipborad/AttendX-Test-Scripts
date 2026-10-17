
# AttendX-Test-Scripts

## Project Description
A collection of sample automation tests for the
AttendX Student Attendance Application.

## Test Scripts

### 1. login_test.py
Tests basic login input validation:
- Non-empty username and password
- Empty username
- Empty password

### 2. attendance_test.py
Tests attendance-marking validation:
- Marking a student Present
- Marking a student Absent
- Rejecting an empty student ID
- Rejecting an invalid attendance status

## Requirements
- Python 3
- Python unittest module (included with Python)

## How to Run
Run the following commands in the terminal:

python login_test.py
python attendance_test.py

## Note
These are standalone demonstration tests.
They do not connect to a live AttendX application.

## Version Control Workflow

The project uses Git for local version control
and GitHub for remote storage and collaboration.

Changes are staged, committed, pushed, and pulled
to keep the local and remote repositories synchronized.
