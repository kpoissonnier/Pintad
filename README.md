# Pintad
Podcast 'n Interview transcription and diarization

Inspired by the work of https://sandstorm.de/de/blog/post/ai-podcast-transcripts-with-speaker-detection.html 
I wanted to practice python, so I've done that

need : pyannote, openai whisper and other stuff

Very first step, create a token for pyannote (see https://github.com/pyannote/pyannote-audio )
convert your audio file into a wav file if it is not ( ffmped -i youraudiofile.whatever youraudiofile.wav )

then 4 steps on linux or wsl : 
./pyannote_script.py youraudiofile.wav
create a "youraudiofile" directory, and a file youraudiofile/youraudiofile.diarization.txt

./cut_the_file.py youraudiofile.wav
will create chunks of audio into the directory youraudiofile for each speaker

./transcript_chunks.py youraudiofile.wav 
will transcript audio chunks, and write the transcript into txt files

./concatenate_transcripts.py youraudiofile.wav
will concatenate chunks into a main file youraudiofile/youraudiofile.transcription.txt




