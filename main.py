# Download Dataset

import urllib.request
from zipfile import ZipFile
import os

# Download MAESTRO Dataset
dataset_dir = "maestro-v3.0.0"
if not os.path.exists(dataset_dir):
    url = 'https://storage.googleapis.com/magentadata/datasets/maestro/v3.0.0/maestro-v3.0.0-midi.zip'
    file_name = 'maestro-v3.0.0-midi.zip'
    
    urllib.request.urlretrieve(url, file_name)
    
    with ZipFile(file_name, 'r') as zip_file:
        zip_file.extractall()
    
    print("Files downloaded successfully")
    os.remove(file_name)
else:
    print("Dataset found")
