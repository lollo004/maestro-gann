# Download Dataset

import urllib.request
from zipfile import ZipFile
import os

url = 'https://storage.googleapis.com/magentadata/datasets/maestro/v3.0.0/maestro-v3.0.0-midi.zip'
file_name = 'maestro-v3.0.0-midi.zip'

urllib.request.urlretrieve(url, file_name)

with ZipFile(file_name, 'r') as zip_file:
    zip_file.extractall()

print("Files extracted successfully")
os.remove(file_name)
