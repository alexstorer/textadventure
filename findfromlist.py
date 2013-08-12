import sys
import getopt
import glob
import csv

def interact():
	import code
	code.InteractiveConsole(locals=globals()).interact()

def compareSingle(tabfile,txt):
    # return 1 if things are found, 0 otherwise
    txtfile = txt
    tab = open(tabfile,'r').read()
    txt = open(txt,'r').read()
    d = dict()
    for cite in tab.split('\r'):
        if len(cite)>0:
            if txt.find(cite)>=0:
                d[cite] = 1
                print "found ", cite, " in ", txtfile
            else:
                d[cite] = 0    
    return d
            
def main():
    # Assume that the input is the directory containing all of the suff you want.  One .tab file and a bunch of pdf
    # python findfromlist.py examples/
    mydir = sys.argv[1]
    txts = glob.glob(mydir+'/*.txt')
    tab = glob.glob(mydir+'/*.tab')
    tabfile = tab[0]
    print "Using citations in file:", tabfile
    for t in txts:
        compareSingle(tabfile,t)

if __name__ == "__main__":
    sys.exit(main())