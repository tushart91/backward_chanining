#!/usr/bin/env python

########################################
# @file     grade.py
# @author   Tushar Tiwari
# @email    ttiwari@usc.edu
# @course   Foundations of Artificial Intelligence/HW2/HW2
# @prof     
# @date     2014-10-19
########################################
import agent

def main():
    filename1 = "/home/tushart91/AI/HW2/HW2/output.txt"
    filename2 = "/home/tushart91/AI/HW2/HW2/sample.txt"
    with open(filename1, 'r') as output_file, \
            open(filename2, 'r') as sample_file:
        string = "Equal"
        i = 1
        for line1, line2 in zip(output_file, sample_file):
            line1 = line1.strip()
            line2 = line2.strip()
            if line1 != line2:
                string = "Not Equal"
                print i, ":",line1, "!=", line2
            i += 1
    print string
    return

if __name__ == "__main__":
    agent.main()
    main()
