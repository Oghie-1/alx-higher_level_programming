#!/usr/bin/python3

import py_compile
import importlib.util

# Compile the Python source file (hidden_4.py) into a .pyc file
py_compile.compile('hidden_4.pyc')

# Load the compiled module
module_name = 'hidden_4'
module_spec = importlib.util.spec_from_file_location(module_name, module_name + '.pyc')
module = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(module)

# Enumerate and print the attributes
for attr_name in dir(module):
    if not attr_name.startswith("__"):  # Exclude special attributes
        print(attr_name)
