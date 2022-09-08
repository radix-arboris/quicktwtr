#!/usr/bin/python3
# Run this script from main directory of repo
# example: python3 devscripts/add_twt_profiles.py

from opcode import opname
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()
print("\n1. Create a file with a list of profiles you want to add.\n")
print("2. Each profile should be on a new line.\n")
input_file = input("Enter full path to file: ")

with open (input_file) as f:
    data = f.readlines()
    f.close()

with open ("data/quicktwtr.toml.tmp", 'w') as f:
    for line in data:
        if not line.startswith("#"):
            f.write("[[handles]]")
            f.write("twth = \""+line+"\"\n")
    f.close()

clear()
print("Done! Check data/quicktwtr.toml.tmp for the results.\n")