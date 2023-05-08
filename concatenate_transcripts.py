#!/usr/bin/env python3
#code qui transcrit les morceaux découpés grace à Pyannote
import sys
#from pydub import AudioSegment
import re
from time import sleep
import os


basename = sys.argv[1].split('.')[0]
fichierSource = "{}.{}".format(basename, "wav")

fichierALire = "{}/{}.diarization.txt".format(basename, basename)

with open(fichierALire, "r", newline=None) as pyannoteFile:
    pyannoteSortie = pyannoteFile.readlines()

transcription = open('{}/{}.transcription.txt'.format(basename, basename), "w")
for line in pyannoteSortie:
    #print(line)
    transcriptName = "{}-{}{}".format(re.sub(':', '-', line.split(' ')[1]), basename, ".wav.txt")
    cible = basename + "/" + transcriptName
    #print("affichage de ", cible)
    speaker = line.split(' ')[6]
    speaker = re.sub("\n", "", speaker)
    timecode = line.split(' ')[1].split('.')[0]
    with open(cible, "r", newline=None) as f:
        transcript = f.read()
    print(timecode, speaker, " : ", transcript)
    ligneAEcrire = timecode + " " + speaker + " :" + transcript + "\n"
    transcription.write(ligneAEcrire)
    #print(line.split(' ')[1].split('.')[0])
    # result = model.transcribe(cible, initial_prompt="{}".format(initial_string))
    # print(result["text"])
    # with open("{}.txt".format(cible), "w") as f:
    #     f.write(result["text"])
transcription.close()