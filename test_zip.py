import os
import zipfile

os.chdir(r'C:\py_temp')
compressed = zipfile.ZipFile('compressed.zip', 'w')


os.chdir(r'C:\pdf_compressed')
for file in os.listdir():
    compressed.write(file, compress_type=zipfile.ZIP_DEFLATED)
compressed.close()
