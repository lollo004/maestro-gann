# Download Dataset

import urllib.request
from zipfile import ZipFile
import os
import numpy as np
from IPython.display import Audio
import pretty_midi

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

def play_midi(path, fs=44100):
    try:
        midi_data = pretty_midi.PrettyMIDI(path)
        audio_data = midi_data.synthesize(fs)
        audio_data = np.int16(audio_data / np.max(np.abs(audio_data)) * 32767)
        return Audio(audio_data, rate=fs)
    except Exception as e:
        print(f"Error while reproducing {path}: {str(e)}")
        return None

# Listen to Audio
midi_path = "maestro-v3.0.0/2004/MIDI-Unprocessed_XP_08_R1_2004_01-02_ORIG_MID--AUDIO_08_R1_2004_01_Track01_wav.midi"
play_midi(midi_path)
