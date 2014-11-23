#!/usr/bin/env python

########################################
# @file     sentence.py
# @author   Tushar Tiwari
# @email    ttiwari@usc.edu
# @course   Foundations of Artificial Intelligence/HW3
# @prof     Prof. Itti
# @date     2014-11-08
########################################

import re

class Variable:

    def __init__(self, string):
        string = string.strip()
        self.value = string
        if re.match(r"[A-Z][A-z,a-z]*", string):
            self.isConstant = True
        else:
            self.isConstant = False
        self.isVariable = not self.isConstant

    def __eq__(self, alt):
        if self.value == alt.value and self.isConstant == alt.isConstant and \
                self.isVariable == alt.isVariable:
            return True
        return False

    def __ne__(self, alt):
        return not self.__eq__(alt)

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.value + str(self.isVariable) + str(self.isConstant))

class AtomicSentence:
    
    def __init__(self, string):
        self.parse(string)
    
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        self.string = self.predicate + "("
        self.string += ",".join(str(x) for x in self.argv) + ")"
        return self.string
    
    def __hash__(self):
        return hash(self.__str__())

    def __copy__(self):
        return AtomicSentence(self.__str__())

    def __eq__(self, alt):
        if alt.__str__() == self.__str__():
            return True
        return False

    def __ne__(self, alt):
        return not self.__eq__(alt)

    def indexof(self, atom_sent):
        for i in range(self.args):
            if atom_sent == self.argv[i]:
                return i

    def parse(self, string):
        string = string.strip()
        self.predicate = re.match(r"[A-Z][A-Z,a-z]*", string).group()
        self.key = self.predicate
        string = string.replace(self.predicate, "")
        string = string.replace("(", "")
        string = string.replace(")", "")
        argv = string.split(",")
        self.args = len(argv)
        self.argv = []
        for i, val in enumerate(argv):
            self.argv.append(Variable(val))

    def unify(self, alt):
        if self.predicate != alt.predicate or self.args != alt.args:
            return None
        substitutions = []
        for i in range(self.args):
            if self.argv[i].isConstant and alt.argv[i].isConstant and \
                    self.argv[i] != alt.argv[i]:
                return None
            elif self.argv[i].isVariable and alt.argv[i].isConstant:
                substitutions.append([self.argv[i].value, alt.argv[i].value])
        return substitutions

    def substitute(self, substitutions):
        new = self.__copy__()

        for key,val in substitutions:
            key = Variable(key)
            val = Variable(val)
            new.argv[self.indexof(key)] = val
        return new

class Sentence:
    def parse(self, string):
        params = string.split("=>")
        if params[0]:
            self.antecedent = map(lambda x: AtomicSentence(x), \
                    sorted(params[0].split("&")))
        else:
            self.antecedent = []
        self.consequent = AtomicSentence(params[1])
        self.key = self.consequent.key
    
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        self.string = "&".join(str(x) for x in self.antecedent) + "=>" + \
                str(self.consequent)
        return self.string

    @property
    def lhs(self):
        return self.antecedent

    @property
    def rhs(self):
        return self.consequent

    def __init__(self, string):
        self.parse(string)

