# LeetCode-Interview-Ready

## Your Comprehensive Code Practice Platform for Technical Interviews

Welcome to LeetCode-Interview-Ready, your comprehensive code practice platform designed to prepare you effectively for technical interviews. This repository is tailored to help you excel in your preferred code editor, emphasizing the creation of custom test cases, running code from the terminal, and applying Object-Oriented Programming (OOP) principles. LeetCode's online editor abstracts away skills such as creating, linking and running test cases - which are all typically tested in coding interviews. This repo provides handy scripts to automate boilerplate and examples to ensure you're ready for any bare-bones environment on interview day.

## What is LeetCode-Interview-Ready?

LeetCode-Interview-Ready is your personal workspace to practice and enhance your coding skills, with a strong emphasis on interview preparation. Here's how it can benefit you:

### 1. Bare Bones Practice

We recognize the importance of being well-prepared to thrive in various coding environments. LeetCode-Interview-Ready allows you to practice coding in different editors, ensuring you're ready for interviews that may require running your code independently.

### 2. Crafting Custom Test Cases

Master the skill of creating tailored test cases for your code. Delve into edge cases and rigorous testing independently, essential skills for interviews.

### 3. Command Line Mastery

Hone your ability to execute and test code directly from the command line. Interviews may not provide a full development environment, and we'll empower you to navigate this challenge with confidence.

## How to Use LeetCode-Interview-Ready

Getting started is easy:

1. Clone the repository:

   ```bash
   git clone https://github.com/[your-username]/LeetCode-Interview-Ready.git
   ```

   Repository Structure

   - `src/`: Contains all the source code files, organized by problem categories.
   - `tests/`: Includes test cases for each problem, emphasizing on covering edge cases.
   - `docs/`: Any documentation or notes related to the problems or concepts.
   - `utils/`: Utility scripts and common modules used across different solutions.

2. Navigate to the `src/` directory:

   ```bash
   cd LeetCode-Interview-Ready/src
   ```

3. Run the addnew.py script to create files for a new problem:

   ```bash
   python addnew.py
   ```

   Follow the prompts to enter the question title (e.g., "841. Keys and Rooms"). The script will generate appropriately named documentation, source code, and test files.

4. Solve the question in the src/ file. Create tests in the tests/ file. Write optional documentation in the docs/ file.

To run tests:

1. Ensure you are in the root directory of the project (`LeetCode-Interview-Ready`):

   ```bash
   cd path/to/LeetCode-Interview-Ready
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
