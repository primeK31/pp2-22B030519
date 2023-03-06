import os

path_name = "D:\python_labs\pp2-22B030519"
print('Exist:', os.access(path_name, os.F_OK))
print('Readable:', os.access(path_name, os.R_OK))
print('Writable:', os.access(path_name, os.W_OK))
print('Executable:', os.access(path_name, os.X_OK))
