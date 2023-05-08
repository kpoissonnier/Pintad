#!/usr/bin/env python3

import os
import sys
fichier = sys.argv[1]
basename = fichier.split('.')[0]

from pyannote.audio import Pipeline

with open("pyannote_token.txt", "r") as reader:
    TOKEN = reader.read()

print(TOKEN)

os.makedirs('{}/'.format(basename), exist_ok=True)

# see https://github.com/pyannote/pyannote-audio to get a token 
# write the token in the pyannote_token.txt file
pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization@2.1", use_auth_token=TOKEN)

# or use a the pipeline offline, edit config.yaml and place it into a pyannote directorya longside with pytorch_model.bin
# see https://github.com/pyannote/pyannote-audio/blob/develop/FAQ.md#can-i-use-gated-models-(and-pipelines)-offline
# then comment the line for previous pipeline, and ucomment the following line
# copy paste into the directory pyannote the config.yaml file and the pytorch_model.bin
# and use this line in the config.yaml : segmentation: pyannote/pytorch_model.bin
# pipeline = Pipeline.from_pretrained("pyannote/config.yaml")

# apply the pipeline to an audio file
# save it to a file in a directory named after the basename of the audio file
diarization = pipeline(fichier) 
print(str(diarization))
with open("{}/{}{}".format(fichier.split('.')[0], fichier.split('.')[0], ".diarization.txt"), "w") as f:
    f.write(str(diarization))
