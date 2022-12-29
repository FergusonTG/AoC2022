import pathlib
import os

os.chdir(pathlib.Path(__file__).parent.parent)
print(pathlib.Path.cwd())

