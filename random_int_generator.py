import sys
import random 

mount = 0
if len(sys.argv) >= 2:
	mount = int(sys.argv[1])

for n in range(mount):
	print random.randint(0, sys.maxint)

