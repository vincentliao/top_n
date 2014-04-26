#! /usr/bin/env python
# description : Show those largest n numbers from a file. 
#               seems like a unix command: cat file.txt | sort -n -r | head -n 3
# author      : vincentliao
# date        : 20140424

import sys

TOP_N = 3
top = [None] * (TOP_N+1)

def escalate(top):
	for i in reversed(range(1, TOP_N+1)):
		if top[i] > top[i-1]: 
			top[i], top[i-1] = top[i-1], top[i]

# read number from file(command argument)
fd = open(sys.argv[1], "r")
numbers = []
while True:
	line = fd.readline().strip()
	if line == '':
		break
				
	top[TOP_N] = int(line) 
	escalate(top)

for n in top[:TOP_N]:
	print n
