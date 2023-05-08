#!/usr/bin/env python3
#code qui transcrit les morceaux découpés grace à Pyannote
import sys
#from pydub import AudioSegment
import re
#from time import sleep
import os
import whisper

#model = whisper.load_model("tiny.en")
#model = whisper.load_model("base")
#model = whisper.load_model("small.en")
model = whisper.load_model("medium.en")
#model = whisper.load_model("large")

textFile = "initial_prompt.txt" 
basename = sys.argv[1].split('.')[0]

def initial_prompting(textFile) :
    with open(textFile, "r") as file: 
        listing = [line.rstrip() for line in file]
        listing = ' '.join(listing)
    return listing

initial_string = initial_prompting(textFile)
print("{}".format(initial_string))

#lister les segments
#en fonction du fichier pyannote, transcrire les fichiers
#fichierALire = sys.argv[1]
fichierALire = "{}/{}.diarization.txt".format(basename, basename)

with open(fichierALire, "r", newline=None) as pyannoteFile:
    pyannoteSortie = pyannoteFile.readlines()

# for line in pyannoteSortie:
#     print(line)
#     segmentName = "{}-{}{}".format(re.sub(':', '-', line.split(' ')[1]), basename, ".wav")
#     print(basename + "/" + segmentName)

for line in pyannoteSortie:
    #print(line)
    segmentName = "{}-{}{}".format(re.sub(':', '-', line.split(' ')[1]), basename, ".wav")
    cible = basename + "/" + segmentName
    print("transcription de ", cible)
    result = model.transcribe(cible, initial_prompt="{}".format(initial_string))
    print(result["text"])
    with open("{}.txt".format(cible), "w") as f:
        f.write(result["text"])
