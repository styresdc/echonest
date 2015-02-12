# Problem
We want to analyze the pitches in all the segments in the [million song dataset].

# Question
1. What information does the [million song dataset] provide?
2. How do you get the timbre for every segment in song in the MSD?
3. How do you get the timbre for every segment in every song in the MSD?

# Resources
1. [Million Song Dataset]
2. [Million Song Dataset Code]
3. [Pyechonest Show Attrs Example]

### 1. Mini-abstract and relevance of [Million Song Dataset]
The Million Song Dataset contains analysis and metadata for one million songs from [The Echo Nest].  The descriptors for each track are availble in the [example track description], including the `segments_timbre` method for getting all the timbre values for the segments.  This resource answers the question 1: what information does the MSD provide?

### 2. Mini-abstract and relevance of [Million Song Dataset Code]
The code for the MSD shows how to open an hdf5 file in Python (among other languages).  There is a link to [hdf5_getters.py] that provides helper methods for dealing with HDF5 files from the MSD.  Put the `hdf5_getters.py` file in your current directory or on your python path.  Specifically, the following code puts the timbre for every segment in a MSD file:
```python
import hdf5_getters
h5 = hdf5_getters.open_h5_file_read('MSD/data/A/A/A/TRAAAAK128F9318786.h5')
timbre = hdf5_getters.get_segments_timbre(h5)
h5.close()
```
This resource answers question 2: how to get the timbre for one song.

### 3. Mini-abstract and relevance of [Pyechonest Show Attrs Example]
This code prints some attributes from every song in a directory.  Specifically, I am reusing the `show_attrs` method to recursively analyze every song in the MSD.  The [all_pitches_msd.py] demonstrates how to recursively concatenate the pitches of hdf5 files in the MSD directory structure.


[Million Song Dataset]: http://labrosa.ee.columbia.edu/millionsong/
[Million Song Dataset Code]: http://labrosa.ee.columbia.edu/millionsong/pages/code
[The Echo Nest]: http://echonest.com
[example track description]: http://labrosa.ee.columbia.edu/millionsong/pages/example-track-description
[hdf5_getters.py]: https://github.com/tb2332/MSongsDB/blob/master/PythonSrc/hdf5_getters.py
[Pyechonest Show Attrs Example]: https://github.com/echonest/pyechonest/blob/master/examples/show_attrs.py
[all_pitches_msd.py]: https://github.com/rmparry7/echonest/tree/master/all_pitches_msd
