import os
import librosa
import numpy
import json
import math

# source: https://www.youtube.com/playlist?list=PL-wATfeyAMNrtbkCNsLcpoAyBBRJZVlnf
DATASET_PATH = "./Data"
JSON_PATH = "data.json"

SAMPLE_RATE = 22050
DURATION = 30
SAMPLES_PER_TRACK = SAMPLE_RATE * DURATION # 661500

def save_mfcc(dataset_path, json_path, n_mfcc=13, n_fft=2048, hop_length=512, num_segments=6) :
    # make dictionary to store data
    song_data = {
        "mapping": [],
        "mfcc": [],
        "labels": []
    }

    num_samples_per_segment = int(SAMPLES_PER_TRACK / num_segments) # 110250
    expected_num_mfcc_vectors_per_segment = math.ceil(num_samples_per_segment / hop_length) # 215.33

    # iterate through genres and songs within the genres
    for i, (dirpath, dirnames, filenames) in enumerate(os.walk(dataset_path)) :

        if dirpath is not dataset_path:

            # fill mapping array
            dirpath_components = dirpath.split("\\")
            semantic_label = dirpath_components[-1]
            if (semantic_label != "genres_original"):
                song_data["mapping"].append(semantic_label)
            print("\nProcessing {}".format(semantic_label))

            # process files
            for f in filenames:

                file_path = os.path.join(dirpath, f)
                print(file_path)
                try:
                    signal, sr = librosa.load(file_path, sr=SAMPLE_RATE)
                except:
                    print("error") # actually coded

                for s in range(num_segments) :
                    start_sample = num_samples_per_segment * s
                    finish_sample = start_sample + num_samples_per_segment

                    mfcc = librosa.feature.mfcc(y = signal[start_sample:finish_sample], sr = sr, n_fft=n_fft, n_mfcc=n_mfcc, hop_length=hop_length)
                    mfcc = mfcc.T

                    if len(mfcc) == expected_num_mfcc_vectors_per_segment :
                        song_data["mfcc"].append(mfcc.tolist())
                        song_data["labels"].append(i - 2)
                        print("{}, segment:{}".format(file_path, s))
                    

    with open(json_path, "w") as fp :
        json.dump(song_data, fp, indent=4)


if __name__ == "__main__"  :
    save_mfcc(DATASET_PATH, JSON_PATH)