#!/usr/bin/env python3
"""
************************************************************************
** Audiophiles Music Manager                         VER0.0.0PREALPHA **
** (C)2017 Mattijs Snepvangers                  pegasus.ict@gmail.com **
** debugger.py              debug engine             VER0.0.0PREALPHA **
** License: MIT                    Please keep my name in the credits **
************************************************************************
"""

class deBUGger():
    """debugger...

    generates debug log"""
    def __init__(self):
        import time
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        debugfilepath = "debug-" + timestamp + ".log"
        ###TODO### create pipe to debuglog

    @classmethod
    def debug_this(self, **kwargs):
        for key, value in kwargs:
            debugline = key + ": " + value + "\n"
            this.debuglog =+ debugline ###CHECK###

def main():
    """just in case somebody wants to test the debugger itself"""
    print("It works!!! ;-)")
    ###TODO### do something with the various methods/functions of this file

# standard boilerplate
if __name__ == '__main__':
    main()
