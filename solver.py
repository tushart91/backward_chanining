#!/usr/bin/env python

########################################
# @file     solver.py
# @author   Tushar Tiwari
# @email    ttiwari@usc.edu
# @course   Foundations of Artificial Intelligence/HW3
# @prof     Prof. Itti
# @date     2014-11-10
########################################

from kb import KB_DB
from sentence import AtomicSentence
from sentence import Sentence
from sentence import Variable
from pprint import pprint
from copy import deepcopy
DEBUG = False
LIMIT = 100
def solve(n, KB_str, query):
    KB = KB_DB()
    goal = AtomicSentence(query)
    for i in KB_str:
        KB.insert(i)
    output = dict()
    for i in fol_bc_or(KB,goal,dict(),dict()):
        if i:
            output = dict(output.items() + i.items())
    if DEBUG:
        pprint("Output: " + str(output))
    if output:
        return "TRUE"
    return "FALSE"

def fol_bc_or(KB, goal, theta, count):
    #raw_input("Press Enter to continue...")
    if DEBUG:
        pprint("fol_bc_or(KB, " + str(goal) + ", " + str(theta) + ", " + \
                str(count) + ")")
    rules = KB.fetch_rules(goal)
    if DEBUG:
        pprint("rules: " + str(rules))
    for rule in rules:
        if rule.rhs not in count.keys():
            count[rule.rhs] = 1
        elif count[rule.rhs] >= LIMIT: 
            pprint("Limit Exceeded: " + str(rule.rhs))
            return
        else:
            count[rule.rhs] += 1
        for _theta_ in fol_bc_and(KB, rule.lhs, \
                unify(rule.rhs, goal, deepcopy(theta)), deepcopy(count)):
            yield _theta_

def fol_bc_and(KB, goals, theta, count):
    if DEBUG:
        if goals:
            pprint("fol_bc_and(KB, " + str([str(x) for x in goals]) + \
                    ", " + str(theta) + ", " + str(count) + ")")
        else:
            pprint("fol_bc_and(KB, " + str([]) + ", " + str(theta) + ", " + \
                    str(count) + ")")
    if not goals: yield theta
    else:
        first = goals[0]
        rest  = None
        if len(goals) > 1:
            rest = goals[1:]
        if not theta:
            for _theta_ in fol_bc_or(KB, first, deepcopy(theta), \
                    deepcopy(count)):
                for __theta__ in fol_bc_and(KB, rest, deepcopy(_theta_), \
                        deepcopy(count)):
                    yield __theta__
        else:
            for _theta_ in fol_bc_or(KB, substitute(theta, first),
                    deepcopy(theta), deepcopy(count)):
                for __theta__ in fol_bc_and(KB, rest, deepcopy(_theta_), \
                        deepcopy(count)):
                    yield __theta__
def unify(x, y, theta):
    if DEBUG:
        pprint("unify(" + str(x) + ", " + str(y) + ", " + str(theta) + ")")
    if theta == None:
        return None
    elif x == y:
        return theta
    elif isinstance(x, Variable) and x.isVariable:
        return unify_var(x, y, theta)
    elif isinstance(y, Variable) and y.isVariable:
        return unify_var(y, x, theta)
    elif isinstance(x, AtomicSentence) and isinstance(y, AtomicSentence):
        return unify(x.argv, y.argv, unify(x.key, y.key, theta))
    elif isinstance(x, list) and isinstance(y, list):
        return unify(x[1:],y[1:],unify(x[0], y[0], theta))
    else: return None

def unify_var(var, x, theta):
    if DEBUG:
        pprint("unify_var(" + str(var) + ", " + str(x) + ", " + \
                str(theta) + ")")
    if var in theta:
        return unify(theta[var], x, theta)
    elif x in theta:
        return unify(var, theta[x], theta)
    else:
        theta[var] = x
    return theta

def substitute(theta, var):
    if DEBUG:
        pprint("substitute(" + str(theta) + ", " + str(var) + ")")
    new_var = var.__copy__()
    for i in range(var.args):
        if var.argv[i].isVariable and var.argv[i] in theta:
            new_var.argv[i] = theta[var.argv[i]]
    return new_var

