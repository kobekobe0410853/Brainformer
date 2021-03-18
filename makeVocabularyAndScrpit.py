
# author : Sean Li
# Email  : kobekobe0410853@gmail.com
# Copyright © NCTU MLLAB

import argparse
import codecs
import re
import sys


def main():

    dictionary =  {'<PAD>':0,'<S/E>':1,'<UNK>':2}

    f = open('aishell_transcript_v0.8.txt', mode='r')
    
    fvocabulary = open('voc', mode='w')
    
    fcharacter = open('character',mode='w')
    

    for line in f.readlines():
        
        newline = line.split(' ')[0]
        line = line.strip(newline).replace(" ","").replace("\n","")
        
        for word in line:
            if word not in dictionary:
                dictionary[word] = len(dictionary)
            newline+=' '+word
        newline+='\n'
        fcharacter.write(newline)
        
    for k,v in dictionary.items():
        s = k+' '+str(v)+'\n'
        fvocabulary.write(s)
    

if __name__ == '__main__':

    main()
