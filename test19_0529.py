import os
import shutil

os.chdir('C:\\')

if not os.path.isdir('pdf'):
    os.makedirs('pdf')

for folder, subfolders, filenames in os.walk(r'C:\py_temp'):
    for filename in filenames:
        if filename.endswith('.pdf'):
            shutil.copy(folder + "\\" + filename, r'C:\pdf')
