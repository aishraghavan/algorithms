"""
Inspired by NPTEL lecture
https://www.youtube.com/watch?v=TTQPvDs24Xk&index=10&list=PL93496BB4FA8A7387
"""
from collections import namedtuple
Move = namedtuple('Move', ['from_peck', 'to_peck'])
#p = Move('A', to_peck='B')
#print p

def tower_of_hanoi(number_of_discs, from_peck, to_peck, via):
	if (number_of_discs == 1):
		return [(Move(from_peck, to_peck))]
	else:
		L1 = tower_of_hanoi(number_of_discs-1, from_peck, via, to_peck)
		L2 = tower_of_hanoi(1, from_peck, to_peck, via)
		L3 = tower_of_hanoi(number_of_discs-1, via, to_peck, from_peck)
		L1.extend(L2)
		L1.extend(L3)
		return L1

print "Tower of Hanoi: number_of_discs = 1"
print "------------------------------------"
print tower_of_hanoi(1, "A", "B", "C")
print "Tower of Hanoi: number_of_discs = 2"
print "------------------------------------"
print tower_of_hanoi(2, "A", "B", "C")
print "Tower of Hanoi: number_of_discs = 3"
print "------------------------------------"
print tower_of_hanoi(3, "A", "B", "C")