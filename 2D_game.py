#!/usr/bin/python
import pygame, sys
from pygame.locals import *
import sqlite3 as sqlite

#starts sqlite3
conn = sqlite.connect('database.db')
cursor = conn.cursor()

try:
	cursor.execute('''CREATE TABLE data
		(user, dirt, stone, water, wood, coal, iron, grass)''')
	conn.commit()
except sqlite.Error:
	Table = True
	
#inits the varables
dirt = 0
grass = 1
stone = 2
wood = 3
water = 4
coal = 5
iron = 6

#sets the skins
pygame.display.init()
screen = pygame.display.set_mode((800, 600))
player = pygame.image.load('player.png').convert_alpha(screen)
colours = {
	dirt : pygame.image.load('dirt.jpg').convert(),
	grass : pygame.image.load('grass.jpg').convert(),
	stone : pygame.image.load('stone.jpg').convert(),
	wood : pygame.image.load('wood.jpg').convert(),
	water : pygame.image.load('water.jpg').convert(),
	coal : pygame.image.load('coal.jpg').convert(),
	iron : pygame.image.load('iron.jpg').convert()
	}

#player stats
playerpos = [0,0]

#makes the map
tilemap = [
	[stone, stone, stone, water, water, grass, grass, grass],
	[stone, coal, stone, water, water, grass, dirt, dirt],
	[stone, stone, coal, water, water, grass, wood, grass],
	[iron, iron, stone, water, water, water, grass, grass],
	[iron, stone, grass, water, water, water, grass, stone],
	[stone, stone, grass, wood, water, water, grass, stone],
	[stone, stone, grass, grass, water, grass, stone, stone],
	[stone, dirt, dirt, grass, grass, grass, stone, coal]
	]

#useful data
TILESIZE = 40
MAPWIDTH = 8
MAPHEIGHT = 8
ironamt = 0
stoneamt = 0
coalamt = 0
wateramt = 0
woodamt = 0
grassamt = 0
dirtamt = 0
true = True
#starts pygame
pygame.init()

DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

#main loop
while True:
	
	#detects user events
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			#detects if user quits then exits
		elif event.type == KEYDOWN:
			if (event.key == K_RIGHT):
				while true == True:
					playerpos[0] += 1
					if event.type == KEYUP:
						break
					elif true == True and playerpos[0] < MAPWIDTH - 1:
						playerpos[0] -= 1
					else:
						true = True					
			elif (event.key == K_LEFT):
				while true == True:
					playerpos[0] -= 1
					if event.type == KEYUP:
						break
					else:
						true = True
			elif (event.key == K_UP):
				while true == True:
					playerpos[1] += 1
					if event.type == KEYUP:
						break
					else:
						true = True
			elif (event.key == K_DOWN):
				while true == True:
					playerpos[0] -= 1
					if event.type == KEYUP:
						break
					else:
						true = True
			else:
				blank = True 
	#makes the background
	for row in range(MAPHEIGHT):
		for column in range(MAPWIDTH):
			DISPLAYSURF.blit(colours[tilemap[row][column]], (column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))
			DISPLAYSURF.blit(player,(playerpos[0]*TILESIZE,playerpos[1]*TILESIZE))
	#display update
	pygame.display.update()
conn.close()
