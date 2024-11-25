# ──> To run this script as intended:
# ──> 1. Copy the file's path in PyCharm.
# ──> 2. Paste it into the terminal.
# ──> 3. Execute it with one or more arguments (e.g., 'python script.py Name').

import sys  # ──> Import 'sys' to access command-line arguments.

# ──> Check if at least one argument (besides the script name) is provided.
if len(sys.argv) < 2:
    # ──> Exit with an error message if no argument is provided.
    sys.exit("Too few arguments")

"""
──> Detailed Explanation:
if len(sys.argv) < 2:
    ──> This condition checks if the length of 'sys.argv' is less than 2.

Why '2'?:
    ──> 'sys.argv[0]' is always the script's name (e.g., 'script.py').
    ──> If at least one argument is passed (e.g., 'python script.py Alice'), the length of 'sys.argv' will be 2 or greater.
    ──> If no arguments are passed (e.g., just running 'python script.py'), 'len(sys.argv)' will be 1, as it only contains the script name, ['script.py'].
"""

# ──> Iterate through all arguments starting from the first user-provided one.
for arg in sys.argv[1:]:
    # ──> Print each argument as a separate name.
    print("hello, my name is", arg)
