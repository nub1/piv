#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy
import random

def getFieldInfo(grid):
  print grid
  res = "Iron: " + str(grid['iron']) + "\r\n"
  res = res + "Copper: "+ str(grid['copper']) + "\r\n"
  res = res + "Gold: "+ str(grid['gold']) + "\r\n"
  return res


def dropRessources(grid, itemToDrop):
  print "Dropping ressources on " + str(itemsToDrop) + " fields"
  size=len(grid)
  for i in xrange(0,itemsToDrop):
    r1=random.randint(0,size-1)
    r2=random.randint(0,size-1)
    r3=random.randint(0,size-1)
    #print "Adding to " + str(r1) + " " + str(r2) + " " + str(r3)
    ar[r1][r2][r3]['gold'] += random.randint(0,1)
    ar[r1][r2][r3]['copper'] += random.randint(0,3)
    ar[r1][r2][r3]['iron'] += random.randint(0,10)
  
  



# datatype for grid
dt = numpy.dtype( [('name1',numpy.str_, 16), \
('iron','int'), \
('copper','int'), \
('gold','int')] )

#dt = numpy.dtype([('name1', '|S10'), ('name2', '<f8')])
# grid size (100=100MB RAM, 200=260MB RAM)
size=100

# init grid
print "Initializing grid..."
ar = numpy.zeros((size,size,size), dtype=dt)
print "Grid (size "+str(size*size*size)+") initialized"

# dropping ressources
itemsToDrop=size*size*size/100
dropRessources(ar,itemsToDrop)
dropRessources(ar,itemsToDrop)
dropRessources(ar,itemsToDrop)


# debug
raw_input('Press any key to continue:')
print ar[9][1][2]
c = ar[1][3][4]
print c['name1']
c['name1'] = "Meine Daten"
#c['gold'] = 1337
print str(ar[1][3][4])
for i in xrange(0,99):
  if ar[0][0][i]['gold'] > 0:
    print getFieldInfo(ar[0][0][i])


