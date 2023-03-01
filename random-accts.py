#!/usr/bin/env python
import sys
import random

accts_file = str(sys.argv[1])

with open(accts_file, "r") as file:
    accts = file.read().split("\n")

half_accts = len(accts)//2

random.shuffle(accts)

accts_assigned = {"mau": accts[:half_accts], "juan": accts[half_accts:]}


#with open("accts_assigned.txt", "w") as file:
    
print(accts_assigned)
