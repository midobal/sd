#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class SD:
    """
    Stadistical dictionary.
    """
    def __init__(self, file):
        """
        Dictionary creation.
        """
        self.words = {}
        self.probs = {}
        
        for line in open(file):
            try:
                if self.probs[line.split()[0]] < float(line.split()[-1]):
                    self.probs[line.split()[0]] = float(line.split()[-1])
                    self.words[line.split()[0]] = line.split()[1]
            except:
                self.words[line.split()[0]] = line.split()[1]
                self.probs[line.split()[0]] = float(line.split()[-1])

    def getWord(self, word):
        """
        This method returns the most probable word. 
        In case of error, the source word is returned.
        """
        try:
            return self.words[word]
        except:
            return word

def usage():
    """
    This function shows the usage message.
    """
    sys.stderr.write('Usage: ' + sys.argv[0] + ' -t text_file -a alignments\n')
    sys.exit(-1)

def getArguments():
    """
    This function checks the arguments and returns their value.
    """
    text = None
    alignments = None
    
    #Loop through the arguments.
    n = 1
    while n < len(sys.argv):
        
        if sys.argv[n] == '-t':
            src = sys.argv[n + 1]
            n += 2
        
        elif sys.argv[n] == '-a':
            alignments = sys.argv[n + 1]
            n += 2
            
        else:
            usage()

    #Check that mandatory arguments are present.
    if text == None or alignments == None:
        usage()

    #Check all paths.
    if not os.path.isfile(text):
        sys.stderr.write('Error opening file ' + src + '\n')
        sys.exit(-1)

    if not os.path.isfile(alignments):
        sys.stderr.write('Error opening file ' + alignments + '\n')
        sys.exit(-1)

    #Return arguments.
    return text, alignments
        
if __name__ == "__main__":
    """
    This function translates a text using an statistical dictionary.
    """
    text, alignments = getArguments()
    
    sd = SD(alignments)
    
    for line in open(text):
        sentence = ''
        for word in line.split():
            sentence += sd.getWord(word) + ' '
        print sentence.strip()
