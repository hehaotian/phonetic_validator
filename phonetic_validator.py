# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 12:03:10 2014

@author: haotianhe

This phonetic validator script checks whether the input contains invalid characters that SAMPA for American English does not accept, and output the error report.
"""

import sys

class usEnglishSymbols():
    
    '''
        default constructor with American English SAMPA symbols. It includes two different set, one is for mono-character symbols with the key "MONO", and another is for multi-character symbols with the key "MULTI".
    '''
    def __init__(self):
        self.symbolList = dict()
        monochar = set(['p', 'b', 't', 'd', 'k', 'g', 'f', 'v', 'T', 'D', 's', 'z', 'S', 'Z', 'h', 'm', 'n', 'N', 'r', 'l', 'w', 'j', 'I', 'E', '{', 'A', 'V', 'U', 'i', 'e', 'u', 'o', 'O', '@', '"'])
        multichar = set(['@`', 'aI', 'OI', 'aU', '3`', 'tS', 'dZ'])
        self.symbolList = {"MONO" : monochar, "MULTI" : multichar}
    
    '''
        this function takes the set tag and the symbol that you want to add to the American English SAMPA
        
    '''
    def addNewSymbol(self, tag, s):
        self.symbolList[tag].add(s)
    
    '''
        this function takes the set tag and the symbol that you want to remove from the American English SAMPA
    '''
    def removeSymbol(self, tag, s):
        self.symbolList[tag].discard(s)

    '''
        this function returns the American English SAMPA as a dictionary with the set tag as the key
    '''
    def returnList(self):
        return self.symbolList

if __name__ == "__main__":
    
    if (len(sys.argv) == 2):
        input = sys.argv[1]
    else:
        input = "test.txt"

    scripts = open(input, 'r')

    '''
        according to the notes of American English SAMPA (http://www.phon.ucl.ac.uk/home/sampa/american.htm), there are several notational variants. You can adjust the SAMPA symbols by calling addNewSymbol or removeSymbol functions with the set tag "MONO" or "MULTI" and the symbol. Try to uncomment the trials below, and see what happens.
    '''
    sampa = usEnglishSymbols()
    # sampa.addNewSymbol("MONO", '4')
    # sampa.addNewSymbol("MONO", '`')
    # sampa.addNewSymbol("MULTI", 'eI')
    # sampa.addNewSymbol("MULTI", 'oU')
    # sampa.addNewSymbol("MULTI", '@r')
    # sampa.removeSymbol("MONO", 'r')
    english = sampa.returnList()

    line_count = 0
    for line in scripts.readlines():

        line = line.split(" ")
        line_count += 1
        
        '''
            reads each line in the input file and gets the transcriptions in each line
        '''
        for i in range(0, len(line)):
            script = line[i]
            
            '''
                for the transcription of each word, it first checks whether multi-character symbols are in the transcription, and then does it for mono-character symbols. Once the transcription symbols matches their corresponding in the SAMPA, we delete them, and only remain those unrecognized.
            '''
            for s in english["MULTI"]:
                if s in script:
                    script = script.replace(s, "")

            for t in english["MONO"]:
                if t in script:
                    script = script.replace(t, "")
            
            '''
                for the transcription of each word, if there are still some symbols unrecognized, it reports the error
            '''
            script = script.strip()
            if len(script) == 0: continue
            else:
                unrecog = list(script)
                for i in range(0, len(unrecog)):
                    print "Line " + str(line_count) + ': Error starting at "' + unrecog[i] + '"'