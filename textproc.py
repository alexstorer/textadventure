print "hello world"

# Basic idea: we want to take in a string, and a list of other strings.  Then, return the indices of the strings where the first string is found.
def stringfinder(s1,slist):
    s1 = s1.lower()
    for ind,s in enumerate(slist):
        s = s.lower()
        # for each string in the list, look for s1 in it
        print "Is", s1, "in", s, "?"
        # ask the question - is it there?
        if s.find(s1) > -1:
            print "Yes!! And the index is ", ind
        else:
            print "Nope!"

# Ideas for how to pass the list of strings:
            # A csv file that contains the names of the text files containing the strings
            # Names of text files One by one on the command line
            # Input not just hte list of strings, but also a list of initial strings, both as 