#!/usr/bin/env python3
"""Bloco de notas

$ notes.py new "Minha Nota"
tag: tech
text:
bla bla bla

$ notes.py read --tag=tech 
"""

__version__ = "0.1.0!"

import os
import sys

path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid arguments")
    sys.exit(1)

