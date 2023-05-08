#!/usr/bin/env python3
#code qui coupe le fichier en fonction de la sortie pyannote
import sys
from pydub import AudioSegment
import re
from time import sleep
import os

basename = sys.argv[1].split('.')[0]
fichierSource = "{}.{}".format(basename, "wav")
song = AudioSegment.from_wav(fichierSource)
os.makedirs('{}'.format(sys.argv[1].split('.')[0]), exist_ok=True)
#lister les segments
#en fonction du fichier pyannote, couper le fichier audios en segments à passer à whisper
fichierALire = "{}/{}.diarization.txt".format(basename, basename)

with open(fichierALire, "r", newline=None) as pyannoteFile:
    pyannoteSortie = pyannoteFile.readlines()

def convertIntoMs(heure):
    timecode = int(heure.split(':')[0]) * 3600000 + int(heure.split(':')[1]) * 60000 + int(re.sub(']', '', re.sub('\.', '', heure.split(':')[2])))
    return timecode

def cutNSave(source, debut, fin, name, location):
    segment = source[debut:fin]
    segment.export("{}/{}".format(location, name), format="wav")

#print(pyannoteSortie)
for line in pyannoteSortie:
    print(line.split(' '))
    print(line.split(' ')[6])
    print(convertIntoMs(line.split(' ')[1]))
    print(convertIntoMs(line.split(' ')[4]))
    print("{}-{}{}".format(re.sub(':', '-', line.split(' ')[1]), basename, ".wav"))
    segmentName = "{}-{}{}".format(re.sub(':', '-', line.split(' ')[1]), basename, ".wav")
    cutNSave(song, convertIntoMs(line.split(' ')[1]), convertIntoMs(line.split(' ')[4]), segmentName, basename)
