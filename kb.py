#!/usr/bin/env python

########################################
# @file     kb.py
# @author   Tushar Tiwari
# @email    ttiwari@usc.edu
# @course   Foundations of Artificial Intelligence/HW3
# @prof     Prof. Itti
# @date     2014-11-08
########################################

from sentence import Sentence
from sentence import AtomicSentence

#class KB_AtomicSentence:
    #def __init__(self):
        #self.KB = []
        #self.mapper = dict()
        #self.n = -1

    #def insert(self, string):
        #sentence = AtomicSentence(string)
        #self.n += 1
        #if sentence.key in self.mapper:
            #self.mapper[sentence.key].append(self.n)
        #else:
            #self.mapper[sentence.key] = [self.n]
        #self.KB.append(sentence)

    #def fetch_rules(self, i):
        #if i.key in self.mapper:
            #return [self.KB[x] for x in self.mapper[i.key]]
        #return []

    #def __str__(self):
        #return "\n".join(str(x) for x in self.KB)

class KB_Sentence:
    def __init__(self):
        self.KB = []
        self.mapper = dict()
        self.n = -1

    def insert(self, string):
        sentence = Sentence(string)
        self.n += 1
        if sentence.key in self.mapper:
            self.mapper[sentence.key].append(self.n)
        else:
            self.mapper[sentence.key] = [self.n]
        self.KB.append(sentence)

    def fetch_rules(self, i):
        ret = []
        if i.key in self.mapper:
            for x in self.mapper[i.key]:
                if self.KB[x].rhs == i or i.unify(self.KB[x].rhs) or \
                        self.KB[x].rhs.unify(i):
                    ret.append(self.KB[x])
        return ret

    def __str__(self):
        return "\n".join(str(x) for x in self.KB)

class KB_DB:
    def __init__(self):
        self.KB = KB_Sentence()
        self.n = 0
    
    def insert(self, string):
        if "=>" not in string:
            string = "=>" + string
        self.KB.insert(string)
        self.n += 1

    def fetch_rules(self, i):
        output = self.KB.fetch_rules(i)
        return output

    def __str__(self):
        return str(self.KB)

