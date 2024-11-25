import cowsay  # ──> Import 'cowsay' for fun ASCII art.
import sys     # ──> Import 'sys' to handle command-line arguments.

# ──> Check if exactly one argument (besides the script name) is provided.
if len(sys.argv) == 2:
    # ──> Use 'cowsay.trex' to display a message with a T-Rex ASCII art.
    cowsay.trex("hello, " + sys.argv[1])

    # ──> Alternative ASCII art example (commented out):
    # cowsay.cow("hello, " + sys.argv[1])
