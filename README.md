# Study-LeetCode

## Description

This repository is dedicated to my journey through solving problems on LeetCode. It's not just a collection of solutions, but a testament to an organized workflow and a practice arena for setting up classes, creating custom test cases, handling edge cases, and executing code via the command line.

## Purpose

The primary goals of this repository are:

- **Tracking Progress**: Documenting my progress on LeetCode problems.
- **Demonstrating Organized Workflow**: Showcasing a professional and systematic approach to problem-solving.
- **Practice and Learning**: Improving my skills in setting up classes, writing comprehensive test cases, and understanding edge cases.
- **Command Line Proficiency**: Running and testing code using command line interfaces.

## Repository Structure

- `src/`: Contains all the source code files, organized by problem categories.
- `tests/`: Includes test cases for each problem, emphasizing on covering edge cases.
- `docs/`: Any documentation or notes related to the problems or concepts.
- `utils/`: Utility scripts and common modules used across different solutions.

## How to Use

To run a solution:

1. Clone the repository:

   ```bash
   git clone https://github.com/[your-username]/study-leetcode.git
   ```

2. Navigate to the `src/` directory:

   ```bash
   cd study-leetcode/src
   ```

3. Run the addnew.py script to create files for a new problem:

   ```bash
   python addnew.py
   ```

   Follow the prompts to enter the question title (e.g., "841. Keys and Rooms"). The script will generate appropriately named documentation, source code, and test files.

4. Solve the question in the src/ file. Create tests in the tests/ file. Write optional documentation in the docs/ file.

To run tests:

1. Ensure you are in the root directory of the project (`study-leetcode`):

   ```bash
   cd path/to/study-leetcode
   ```

2. Run the test file for a specific problem using Python's `-m` flag. Replace `[problem-name]` with the actual name of the problem:

   ```bash
   python -m unittest tests.test_[problem-name]
   ```

   For example, if you have a test file named `test_keys_and_rooms.py` in the `tests` directory, you would run:

   ```bash
   python -m unittest tests.test_keys_and_rooms
   ```

## Understanding Test Results

When running unit tests using the `unittest` library in Python, you will see two symbols that indicate the results of test cases:

- `.` (Dot):

  - A `.` represents a successful test case execution without any errors or failures.
  - Each `.` corresponds to a single test method or test case that has executed successfully.
  - These dots are displayed to provide a visual progress indicator for the test suite.

  Example:
  `......`

- `E` (Error):
- An `E` indicates that a test case encountered an unexpected error during execution.
- Errors can occur for various reasons, such as unhandled exceptions, assertion failures, or other runtime issues.
- The `E` symbol indicates that a test case failed due to an unexpected error.

  Example:
  `..E...`

## Contributing

While this repository primarily serves as a personal log of my LeetCode journey, suggestions or advice on improving solutions, test cases, or any other aspect of the repository are always welcome.
