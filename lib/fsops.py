#!/usr/bin/env python3
"""
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
* Audiophiles Music Manager          Build 20180119          VER0.0.0PREALPHA *
* (C)2017 Mattijs Snepvangers                           pegasus.ict@gmail.com *
* lib/fsops.py                       Filesystem Operations   VER0.0.0PREALPHA *
* License: MIT                             Please keep my name in the credits *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""

import os
# file_list = []
# trash_list = []

def is_this_a_dir(path):
    """verify whether a directory exists

    """
    return os.path.isdir(path)

def scan_dir(rootdir):
    """Scans rootdir recursively

    store files in lists for further processing based on extension."""
    global file_list, trash_list
    from pathlib import PurePath
    audio_exts = [mp3, flac, m4a, aif, ogg, wma, wav, cda, mp2, ape, midi, mid,
                 mod, opus, au, aac, cue]
    for root, files in os.walk(rootdir): ###CHECK### subfolders?
        for thisfile in files:
            file_ext = PurePath(thisfile).suffix
            if file_ext not in audio_exts:
                trash_list.append(thisfile)
            else :
                file_list.append(os.path.join(root,thisfile))

def is_this_a_file(path):
    """verify "path" to be a file"""
    result = os.path.isfile(path)
    return result

def delete_file(file_to_be_deleted):
    """delete file_to_be_deleted"""
    os.unlink(file_to_be_deleted)
    return True

def main():
    """just in case somebody wants to test this file by itself"""
    pass

# standard boilerplate
if __name__ == '__main__':
    main()
