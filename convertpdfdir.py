#!/usr/env/python
import sys
import getopt
import glob
import subprocess
            
def main():
    # Assume that the input is the directory containing all of the suff you want.  One .tab file and a bunch of pdf
    # python findfromlist.py examples/
    mydir = sys.argv[1]
    pdfs = glob.glob(mydir+'/*.pdf')
    for p in pdfs:
        print "Converting to text:", p
        subprocess.call(["pdftotext",p])

if __name__ == "__main__":
    sys.exit(main())



    