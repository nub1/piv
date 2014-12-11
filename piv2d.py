#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy
import random
import threading
import signal
import sys

# variables:
size = 500
tickcount = 15.0
dropchance = 1

def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)

def getFieldInfo(grid):
    print grid
    res = "Iron: " + str(grid['iron']) + "\r\n"
    res = res + "Copper: "+ str(grid['copper']) + "\r\n"
    res = res + "Gold: "+ str(grid['gold']) + "\r\n"
    return res

def dropRessources(grid, itemToDrop):
    size=len(grid)
    for i in xrange(0,itemsToDrop):
    	# find a field
        r1=random.randint(0,size-1)
        r2=random.randint(0,size-1)

        # add random ressources to it
        #print "Adding to " + str(r1) + " " + str(r2) + " " + str(r3)
        # change of ressources per field: 0-1 gold (50%), 0-3 copper (25%), 0-10 iron (90%)
        grid[r1][r2]['gold'] += random.randint(0,1)
        grid[r1][r2]['copper'] += random.randint(0,3)
        grid[r1][r2]['iron'] += random.randint(0,10)

def tick():
    threading.Timer(tickcount, tick).start()
    print "Dropping " + str(itemsToDrop) + " ressources on fields...",
    dropRessources(dt,itemsToDrop)
    print "done!"

# handle ctrl+c (for saving state)
signal.signal(signal.SIGINT, signal_handler)

# datatype for grid (name, iron, copper, gold)
dt = numpy.dtype( [('name1',numpy.str_, 16), ('iron','int'), ('copper','int'), ('gold','int')] )

# init grid
print "Initializing grid (size "+str(size*size)+")...",
dt = numpy.zeros((size,size), dtype=dt)
print "done!"

# drop ressources (by starting tick() thread)
itemsToDrop=size*size/100*dropchance
print "Dropping " + str(itemsToDrop) + " ressources on fields...",
tick()
print "done!"




# debug
#raw_input('Press any key to continue:')
print "############# RANDOM TESTS HERE ###############"
print dt[9][1]
c = dt[1][3]
print c['name1']
c['name1'] = "My data"
c['gold'] = 1337
print str(dt[1][3])
for i in xrange(0,99):
    if dt[0][i]['gold'] > 0:
        print "(0,"+str(i)+"):"
        print getFieldInfo(dt[0][i])