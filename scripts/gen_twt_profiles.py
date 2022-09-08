#!/usr/bin/python3
# Run this script from main directory of repo
# example: python3 devscripts/gen_twt_profiles.py

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

with open ("quicktwtr.tmp", 'w') as f:
    for line in data:
        if not line.startswith("#"):
            f.write("\n<div class=\"grid-item\">\n")
            f.write("    <a class=\"twitter-timeline\" href=\"https://twitter.com/"+line.rstrip('\n')+"?"+"ref_src=twsrc"+"%"+"5Etfw\" width=\"500px\" height=\"250px\">Tweets by "+line.rstrip('\n')+"</a> <script async src=\"https://platform.twitter.com/widgets.js\" charset=\"utf-8\"></script>\n")
            f.write("</div>")
    f.close()

clear()
print("Done! Check quicktwtr.tmp for the results.\n")