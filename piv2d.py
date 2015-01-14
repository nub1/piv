#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy
import random
import threading
import signal
import sys
import socket
import threading

# variables:
size = 10
tickcount = 8.0
dropchance = 1
server = None
players = []
tickthread = None

class Player:
    pass

def handle_clientConnection(s):
    s.send("piv server asks for authentication: \n")
    request = s.recv(1024).strip()
    # TODO: switch/case with dictionary in python - authenticate
    if request == "list":
        s.send("Current players: \n")
        for i in players:
            s.send(str(i.id)+":"+str(i.nick)+"\n")
    if request == "help":
        s.send("list - list players\n")
        s.send("help - this help message\n")
        s.send("me - information about your connection\n")
    if request == "me": 
        s.send(s.getpeername()[0])
        s.send(":")
        s.send(str(s.getpeername()[1]))
        s.send("\n")

    s.send("bye!\n")
    s.close()

def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        global tickthread
        global server
        tickthread.cancel()
        tickthread.join()
        server.close()
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
    global tickthread
    tickthread = threading.Timer(tickcount, tick)
    tickthread.daemon = True
    tickthread.start()
    print "Dropping " + str(itemsToDrop) + " ressources on fields...",
    dropRessources(dt,itemsToDrop)
    print "done!"




# handle ctrl+c (for saving state)
signal.signal(signal.SIGINT, signal_handler)

# datatype for grid (name, iron, copper, gold)
dt = numpy.dtype( [('name',numpy.str_, 16), ('iron','int'), ('copper','int'), ('gold','int')] )

# init grid
print "Initializing grid (size "+str(size*size)+")...",
dt = numpy.zeros((size,size), dtype=dt)
print "done!"

# drop ressources (by starting tick() thread)
itemsToDrop=size*size/100*dropchance
print "Dropping " + str(itemsToDrop) + " ressources on fields...",
tick()
print "done!"

# player array init
p = Player()
p.nick = "test"
p.pw = "pw"
p.id = 0
players.append(p)
p = Player()
p.nick = "test2"
p.pw = "pw"
p.id = 1
players.append(p)

# set up listener and client connection handler
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0",8000))
server.listen(5)
while True:
    client,addr = server.accept()
    client_handler = threading.Thread(target=handle_clientConnection, args=(client,))
    client_handler.start()




# debug
#raw_input('Press any key to continue:')
print "############# RANDOM TESTS HERE ###############"
print dt[9][1]
c = dt[1][3]
print c['name']
c['name'] = "My data"
c['gold'] = 1337
print str(dt[1][3])
for i in xrange(0,99):
    if dt[0][i]['gold'] > 0:
        print "(0,"+str(i)+"):"
        print getFieldInfo(dt[0][i])
