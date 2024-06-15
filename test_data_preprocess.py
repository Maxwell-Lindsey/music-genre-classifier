import librosa
from data import *
from os.path import exists

file_path = "invalid_file_path"

def test_invalid_file_path():
    entered_except = False
    try:
        signal, sr = librosa.load(file_path, sr=data.SAMPLE_RATE)
    except:
        entered_except = True

    assert entered_except == True
    print("valid file path entered")

def test_data_file_created():
    PATH_TO_FILE = "data.json"
    file_exists = exists(PATH_TO_FILE)
    assert file_exists
    print("data.json file exists")

# run assert tests
test_invalid_file_path()
test_data_file_created()

# all test cases passed
print("all test cases passed for test_data_preprocess.py")