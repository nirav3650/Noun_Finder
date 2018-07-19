# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 10:42:31 2018

@author: NIRAV
"""
import nltk
import sys


class Nounfinder:
    nounlist = []

    def __init__(self):
        print("Noun Extracter from Sentence")

    def process_chunk(self, majorlist1):
        c11 = 0
        while c11 < len(majorlist1):
            semitup = majorlist1[c11]
            if isinstance(semitup, nltk.tree.Tree):
                nltl01 = semitup.leaves()
                self.nounlist.append(nltl01[0][0])

            else:
                if semitup[1] == "NNP" or semitup[1] == "NNPS" or semitup[1] == "NN":
                    self.nounlist.append(semitup[0])

            c11 += 1
        return self.nounlist


if __name__ == "__main__":
    try:
        obj = Nounfinder()
        sentencefromuser = sys.argv[1]
        noun = []
        wordslist = []
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sentencefromuser))):
            wordslist.append(chunk)
        noun = obj.process_chunk(wordslist)
        print("The Nouns are: ", noun)
    except:
        print("Pass the sentence as command line argument")
