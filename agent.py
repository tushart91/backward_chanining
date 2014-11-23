#!/usr/bin/env python

########################################
# @file     agent.py
# @author   Tushar Tiwari
# @email    ttiwari@usc.edu
# @course   Foundations of Artificial Intelligence/HW3
# @prof     Prof. Itti
# @date     2014-11-08
########################################

from solver import solve

def main():
    input_file = "input.txt"
    output_file = "output.txt"
    f = open(input_file, 'r')
    query = f.readline().strip()
    n     = int(f.readline().strip())
    KB = []
    for i in range(0, n):
        KB.append(f.readline().strip())
    f.close()
    output = solve(n, KB, query)
    f = open(output_file, 'w')
    write_string(f, output)
    f.close()
    return

def write_string(f, string):
    f.write(string)
    f.write("\n")

if __name__ == "__main__":
    main()
