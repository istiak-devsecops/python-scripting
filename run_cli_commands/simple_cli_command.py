# run simple CLI command in terminal

import sys
import subprocess

if len(sys.argv) < 2:
    print("Usage: python3 script.py <commands>")
    sys.argv(2) # invalid arguments

command = sys.argv[1:]  # capture all the command except the script name
result =  subprocess.run(command, capture_output=True, text=True)
print(result.stdout)  # print the output in the terminal