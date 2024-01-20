def create_files(question_name):
    # Split the input question name into number and lowercase name
    number, name = question_name.split(". ", 1)
    name = name.replace(" ", "_").lower()

    # Create filenames for docs, src, and tests
    docs_filename = f"docs/{number}_{name}.md"
    src_filename = f"src/{name}.py"
    tests_filename = f"tests/test_{name}.py"

    with open(docs_filename, "w") as docs_file:
        docs_file.write(f'# {number} {name.replace("_", " ").title()}\n')
        docs_file.write(f"\n")
        docs_file.write(f"## Problem Description\n")
        docs_file.write(f"\n")
        docs_file.write(
            f"In the \"{name.replace('_', ' ').title()}\" problem, you are given a description of the problem here.\n"
        )
        docs_file.write(f"\n")
        docs_file.write(f"### Constraints\n")
        docs_file.write(f"\n")
        docs_file.write(f"- Describe the constraints of the problem here.\n")
        docs_file.write(f"\n")
        docs_file.write(f"## Examples\n")
        docs_file.write(f"\n")
        docs_file.write(f"### Example 1\n")
        docs_file.write(f"\n")
        docs_file.write(f"**Input:** Describe the input for Example 1\n")
        docs_file.write(f"**Output:** Describe the expected output for Example 1\n")
        docs_file.write(f"**Explanation:** Describe the explanation for Example 1\n")
        docs_file.write(f"\n")
        docs_file.write(f"### Example 2\n")
        docs_file.write(f"\n")
        docs_file.write(f"**Input:** Describe the input for Example 2\n")
        docs_file.write(f"**Output:** Describe the expected output for Example 2\n")
        docs_file.write(f"**Explanation:** Describe the explanation for Example 2\n")
        docs_file.write(f"\n")
        docs_file.write(f"## Approach\n")
        docs_file.write(f"\n")
        docs_file.write(f"Explain your approach to solving the problem here.\n")
        docs_file.write(f"\n")
        docs_file.write(f"### Algorithm\n")
        docs_file.write(f"\n")
        docs_file.write(f"Describe the algorithm you used here.\n")
        docs_file.write(f"\n")
        docs_file.write(f"## Solution Code\n")
        docs_file.write(f"\n")
        docs_file.write(f"```python\n")
        docs_file.write(f"def {name}(input_parameter):\n")
        docs_file.write(f'    """\n')
        docs_file.write(f"    Your function description here.\n")
        docs_file.write(f'    """\n')
        docs_file.write(f"    # Your code here\n")
        docs_file.write(f"    pass\n\n")
        docs_file.write(f"```\n")
        docs_file.write(f"\n")
        docs_file.write(f"## Complexity Analysis\n")
        docs_file.write(f"\n")
        docs_file.write(
            f"- **Time Complexity:** Describe the time complexity of your solution.\n"
        )
        docs_file.write(
            f"- **Space Complexity:** Describe the space complexity of your solution.\n"
        )
        docs_file.write(f"\n")
        docs_file.write(f"## Running the Tests\n")
        docs_file.write(f"\n")
        docs_file.write(f"```bash\n")
        docs_file.write(f"python -m unittest {tests_filename}\n")
        docs_file.write(f"```\n")

    # Create the src file with a function and input
    with open(src_filename, "w") as src_file:
        src_file.write(f"def {name}(arguments here):\n")
        src_file.write(f'    """\n')
        src_file.write(f"    Your function description here.\n")
        src_file.write(f'    """\n')
        src_file.write(f"    # Your code here\n")
        src_file.write(f"    pass\n\n")

    # Create the tests file with boilerplate content
    with open(tests_filename, "w") as tests_file:
        tests_file.write(f"import unittest\nfrom src.{name} import {name}\n\n")
        tests_file.write(
            f'class Test{name.replace("_", "").title()}(unittest.TestCase):\n'
        )

        # Generate test function names as test_filename_1, test_filename_2, and so on
        for i in range(1, 4):  # You can change the range as needed
            tests_file.write(f"    def test_{name}_{i}(self):\n")
            tests_file.write(f'        """\n')
            tests_file.write(f"        Test case {i} description here.\n")
            tests_file.write(f'        """\n')
            tests_file.write(
                f"        self.assertTrue({name}([]))\n\n"
            )  # Using an empty list as generic input

        # Additional test methods can be added here

        tests_file.write(f'if __name__ == "__main__":\n')
        tests_file.write(f"    unittest.main()\n")


if __name__ == "__main__":
    # Input the question name from the user
    question_name = input("Enter the question name (e.g., '841. Keys and Rooms'): ")
    create_files(question_name)
