import sys         # ──> Import 'sys' to handle command-line arguments.
from sayings import hello  # ──> Import the 'hello' function from the 'sayings' module.

# ──> Check if exactly one argument (besides the script name) is provided.
if len(sys.argv) == 2:
    # ──> Call the 'hello' function, passing the provided argument as a parameter.
    hello(sys.argv[1])
