"""
Based on the show_attrs.py file by ddesroches: 
https://github.com/echonest/pyechonest/blob/master/examples/show_attrs.py

Recursively concatenates pitches from hdf5 files in the MSD directory structure.

For example:

$ python all_pitches_msd.py /u/classes/3535/modules/MillionSongSubset/data/

by Mitch Parry 2015-02-12
"""

import sys
import os
import hdf5_getters
import numpy as np

def _is_hdf5(f):
    _, ext = os.path.splitext(f)
    ext = ext[1:] # drop leading '.'
    return ext == 'h5'

def _get_one_pitches(f):
    with hdf5_getters.open_h5_file_read(f) as h5:
        pitches = hdf5_getters.get_segments_pitches(h5)
        return pitches

def get_all_pitches(directory):
    "get the pitches for each hdf5 file in this or any subdirectories"
    pitches = []
    for f in os.listdir(directory):
        path = os.path.join(directory, f)
        print path
        if _is_hdf5(f):
            p = _get_one_pitches(path)
            pitches.extend(p)
        elif os.path.isdir(path):
            p = get_all_pitches(path)
        else:
            continue

        pitches.extend(p)

    return pitches

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print 'usage: python all_pitches_msd.py path_to_MSD'
    else:
        pitches = get_all_pitches(sys.argv[1])
        #print pitches
        print len(pitches),"total segments"
        print "mean=",np.mean(pitches,axis=0)
        print "stdev=",np.std(pitches,axis=0)
