#!/usr/bin/env python3
# objective : made a prompt for whisper into initial_prompt.txt
# used common_words.txt to remove common words in your language, example french world list from https://github.com/Taknok/French-Wordlist
# for english word list used /usr/share/dict/words : $ cat /usr/share/dict/words > english.txt
# copy one of them into common_words.txt to keep an initial prompt below 1024 words (the maximum for whisper)
# import os
# import json
# import requests
import sys
import re
from time import sleep

initialpromptlist = []
try:
    inputfile= sys.argv[1]
except:
    print("need a file in argument\n try: ./initial_prompt_generator.py file.txt")
    quit()



# read the file in argument, make a list with unique words
def lireFichier(textfile):
    listOfWords=""
    with open(textfile, "r") as file:
        for line in file:
            listOfWords = listOfWords + " " + line.strip()
    listOfWords = listOfWords.lower()
    listOfWords = re.sub(r'[.,"\'-?:!;]', ' ', listOfWords)
    listOfWords = re.sub(r'[^[[:word:]]]', ' ', listOfWords)
    listOfWords = listOfWords.split()
    listOfWords = [ x for x in listOfWords if len(x) > 3]
    return listOfWords 

# read file initial_prompt.txt
# show words and number
initialpromptlist = []
commonwordslist = []
try:
    initialpromptlist = lireFichier("initial_prompt.txt")
    print("there were already ", len(initialpromptlist)," in the list")
except:
    pass


try:
    commonwordslist = lireFichier("common_words.txt")
    print("there are ", len(initialpromptlist), "common words to remove from the prompt")
except:
    pass

# read file in argument
# show words and number
newWordsList= lireFichier(inputfile)
print("Number of new words added to the prompt list:", len(newWordsList))

# finalList = []
finalList = initialpromptlist + newWordsList
finalList = [x for x in finalList if x not in commonwordslist]
finalList = list(set(finalList))
print(finalList)
print(len(finalList))

with open("initial_prompt.txt", "w") as f:
    f.write(" ".join(finalList))

# print(lireFichier(inputfile))
# print(len(lireFichier(inputfile)))

# print(set(lireFichier(inputfile)))
# print(len(set(lireFichier(inputfile))))