import os, sys
try:
    __import__("easy").login()
except Exception as e:
    exit(str(e))
