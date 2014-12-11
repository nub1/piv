#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy
import random

# variables:
size = 2000

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
    #print "Adding to " + str(r1) + " " + str(r2) + " " + str(r3)
    grid[r1][r2]['gold'] += random.randint(0,1)
    grid[r1][r2]['copper'] += random.randint(0,3)
    grid[r1][r2]['iron'] += random.randint(0,10)




# datatype for grid (name, iron, copper, gold)
dt = numpy.dtype( [('name1',numpy.str_, 16), ('iron','int'), ('copper','int'), ('gold','int')] )

# init grid
print "Initializing grid..."
dt = numpy.zeros((size,size), dtype=dt)
print "Grid (size "+str(size*size)+") initialized"

# dropping ressources
itemsToDrop=size*size/100
dropRessources(dt,itemsToDrop)






# debug
raw_input('Press any key to continue:')
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


