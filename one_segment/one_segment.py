#!/usr/bin/env python
# encoding: utf=8
"""
one_segment.py

Digest only the first segment of every beat.

By Mitch Parry, 2015-02-05.
Based on echonest/remix-examples/one/one.py by Ben Lacker, 2009-02-18.
"""
import echonest.remix.audio as audio

usage = """
Usage: 
    python one_segment.py <input_filename> <output_filename>

Example:
    python one_segment.py input.mp3 output.mp3
"""

def main(input_filename, output_filename):
    # load audio file
    audiofile = audio.LocalAudioFile(input_filename)
    # get the beats (Audio Quanta)
    beats = audiofile.analysis.beats
    # create a new empty list of Audio Quanta
    collect = audio.AudioQuantumList()
    # add the first segment in each beat in sequence
    for beat in beats:
        # beat.children are the segments in this beat
        # beat.children()[0] is the first segment
        collect.append(beat.children()[0])
    # Get the raw audio data for the audio quanta and store them in 'out'
    out = audio.getpieces(audiofile, collect)
    # encode the raw audio as the appropriate file type (using en-ffmpeg)
    out.encode(output_filename)

if __name__ == '__main__':
    import sys
    try:
        input_filename = sys.argv[1]
        output_filename = sys.argv[2]
    except:
        print usage
        sys.exit(-1)
    main(input_filename, output_filename)
