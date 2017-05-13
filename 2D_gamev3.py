import pygame, sys
from pygame.locals import *
import sqlite3 as sqlite

#starts sqlite3
try:
        conn = sqlite.connect('database.db')
        cursor = conn.cursor()
        
        try:
                cursor.execute('''CREATE TABLE data (user, dirt, stone, water, wood, coal, iron, grass, glass, steel, fire, clay, brick)''')
                conn.commit()
        except sqlite.Error:
                Table = True
except:
        database = False
        open('database.db','w')
        conn = sqlite.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE data (user, dirt, stone, water, wood, coal, iron, grass, glass, steel, fire, clay, brick)''')
#sets the skins
pygame.display.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 600))
player = pygame.image.load('player.png').convert_alpha(screen)
#playerdown =

DIRT = 0 
GRASS = 1
STONE = 2
WOOD = 3
WATER = 4
COAL = 5
IRON = 6
STEEL = 7
FIRE = 8 
GLASS = 9
CLAY = 10
BRICK = 11

#player = playerdown
colours = {
    DIRT : pygame.image.load('dirt.jpg').convert(),
    GRASS : pygame.image.load('grass.jpg').convert(),
    STONE : pygame.image.load('stone.jpg').convert(),
    WOOD : pygame.image.load('wood.jpg').convert(),
    WATER : pygame.image.load('water.jpg').convert(),
    COAL : pygame.image.load('coal.jpg').convert(),
    IRON : pygame.image.load('iron.jpg').convert(),
    STEEL : pygame.image.load('steel.png').convert(),
    FIRE : pygame.image.load('fire-0.png').convert(),
    GLASS: pygame.image.load('glass.png').convert(),
    CLAY: pygame.image.load('clay.png').convert(),
    BRICK: pygame.image.load('brick.png').convert()
        }

#player stats
playerpos = [1,1]

#makes the map
tilemap = [
        [STONE,  STONE, STONE, WATER, WATER, GRASS, GRASS, GRASS],
        [STONE,   COAL, STONE, WATER, WATER, GRASS, DIRT,   DIRT],
        [STONE,  STONE,  COAL, WATER, WATER, GRASS, WOOD,  GRASS],
        [ IRON,   IRON, STONE, WATER, WATER, WATER, GRASS, GRASS],
        [ IRON,  STONE, GRASS, WATER, WATER, WATER, GRASS, STONE],
        [STONE,  STONE, GRASS,  WOOD, WATER, WATER, GRASS, STONE],
        [STONE,  STONE, GRASS, GRASS, WATER, GRASS, STONE, STONE],
        [STONE,   DIRT,  DIRT, GRASS, GRASS, GRASS, STONE,  COAL]
        ]

#useful data
TILESIZE = 40
MAPWIDTH = 8
MAPHEIGHT = 8
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
#sets the invnetory

inv_query = cursor.execute('''SELECT * FROM data WHERE user="player1"''')
qinv = inv_query.fetchall()
if len(qinv) == 0:
        cursor.execute('''INSERT INTO data (user, dirt, stone, water, wood, coal, iron, grass, glass, steel, fire, clay, brick) values ("player1", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)''')
       	conn.commit()
       	inv_query = cursor.execute('''SELECT * FROM data WHERE user="player1"''')
       	qinv = inv_query.fetchall()
	conn.commit()
print qinv

Dirt1 = int(qinv[0][1])
Stone1 = int(qinv[0][2])
Water1 = int(qinv[0][3])
Wood1 = int(qinv[0][4])
Coal1 = int(qinv[0][5])
Iron1 = int(qinv[0][6])
Grass1 = int(qinv[0][7])
Glass1 = int(qinv[0][8])
Steel1 = int(qinv[0][9])
Fire1 = int(qinv[0][10])
Clay1 = int(qinv[0][11])
Brick1 = int(qinv[0][12])

inventory = { 
    IRON : Iron1,
    STONE : Stone1,
    COAL : Coal1,
    WATER : Water1,
    WOOD : Wood1,
    GRASS : Grass1,
    DIRT : Dirt1,
    STEEL : Steel1,
    FIRE : Fire1,
    GLASS : Glass1,
    CLAY : Clay1,
    BRICK : Brick1
        }

true = True
resources = [DIRT,GRASS,STONE,COAL,IRON,WATER,WOOD,STEEL,FIRE,GLASS,CLAY,BRICK]
font = pygame.font.SysFont('FreeSansBold', 18)
#starts pygame
pygame.init()

DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE + 50))




#main loop
while True:
        #if pygame.error:
        #        print pygame.error
        #detects user events
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                        #detects if user quits then exits
                elif event.type == KEYDOWN:
                        #moves the player
                        if (event.key == K_RIGHT):
                                playerpos[0] += 1
                                if playerpos[0] > MAPWIDTH - 1:
                                        playerpos[0] = MAPWIDTH - 1
                        elif (event.key == K_LEFT):
                                playerpos[0] -= 1
                                if playerpos[0] < 0:
                                        playerpos[0] = 0
                        elif (event.key == K_UP):
                                playerpos[1] -= 1
                                if playerpos[1] < 0:
                                        playerpos[1] = 0
                        elif (event.key == K_DOWN):
                                playerpos[1] += 1
                                if playerpos[1] > MAPHEIGHT - 1:
                                        playerpos[1] = MAPHEIGHT - 1
                        #picks up the item
                        elif (event.key == K_e):
                            currentTile = tilemap[playerpos[0]][playerpos[1]]
                            inventory[currentTile] += 1
                            print inventory
                        #sets the placing mecanics
                        elif (event.key == K_1):
                                currentTile = tilemap[[playerpos[0]][playerpos[1]]]
                                if inventory[DIRT] > 0:
                                        inventory[DIRT] -= 1
                                        tilemap[playepos[0]][playerpos[1]] = DIRT
                                        inventory[currentTile] += 1
                        elif (event.key == K_2):
                                currentTile = tilemap[[playerpos[0]][playerpos[1]]]
                                if inventory[GRASS] > 0:
                                        inventory[GRASS] -= 1
                                        tilemap[playepos[0]][playerpos[1]] = GRASS
                                        inventory[currentTile] += 1
                        elif (event.key == K_3):
                                CurrentTile = tilemap[[playerpos[0]][playerpos[1]]]
                                if inventory[STONE] > 0:
                                        inventory[STONE] -= 1
                                        tilemap[playerpos[0]][playerpos[1]] = STONE
                                        inventory[CurrentTile] += 1
                        elif (event.key == K_4):
                                currentTile = tilemap[[playerpos[0]][playerpos[1]]]
                                if inventory[WOOD] > 0:
                                        inventory[WOOD] -= 1
                                        tilemap[playepos[0]][playerpos[1]] = WOOD
                                        inventory[currentTile] += 1
                        elif (event.key == K_5):
                                currentTile = tilemap[[playerpos[0]][playerpos[1]]]
                                if inventory[WATER] > 0:
                                        inventory[WATER] -= 1
                                        tilemap[playepos[0]][playerpos[1]] = WATER
                                        inventory[currentTile] += 1
                        elif (event.key == K_6):
                                currentTile = tilemap[[playerpos[0]][playerpos[1]]]
                                if inventory[COAL] > 0:
                                        inventory[COAL] -= 1
                                        tilemap[playerpos[0]][playerpos[1]] = COAL
                                        inventory[currentTile] += 1
                        elif (event.key == K_7):
                                currentTile = tilemap[[playerpos[0]][playerpos[1]]]
                                if inventory[IRON] > 0:
                                        inventory[IRON] -= 1
                                        tilemap[playerpos[0]][playerpos[1]] = IRON
                                        inventory[currentTile] += 1
                        elif (event.key == K_8):
                                currentTile = tilemap[[playerpos[0]][playerpos[1]]]
                                if inventory[GLASS] > 0:
                                        inventory[GLASS] -= 1
                                        tilemap[playerpos[0]][playerpos[1]] = GLASS
                                        inventory[currentTile] += 1
                        elif (event.key == K_9):
                                currentTile = tilemap[[playerpos[0]][playerpos[1]]]
                                if inventory[FIRE] > 0:
                                        inventory[FIRE] -= 1
                                        tilemap[playerpos[0]][playerpos[1]] = FIRE
                                        inventory[currentTile] += 1
                        elif (event.key == K_0):
                                currentTile = tilemap[[playerpos[0]][playerpos[1]]]
                                if inventory[STEEL] > 0:
                                        inventory[STEEL] -= 1
                                        tilemap[playerpos[0]][playerpos[1]] = STEEL
                                        inventory[currentTile] += 1
                        elif (event.key == K_MINUS):
                                currentTile = tilemap[[playerpos[0]][playerpos[1]]]
                                if inventory[CLAY] > 0:
                                        inventory[CLAY] -= 1
                                        tilemap[playerpos[0]][playerpos[1]] = CLAY
                                        inventory[currentTile] += 1
                        elif (event.key == K_EQUALS):
                                currentTile = tilemap[[playerpos[0]][playerpos[1]]]
                                if inventory[BRICK] > 0:
                                        inventory[BRICK] -= 1
                                        tilemap[playerpos[0]][playerpos[1]] = BRICK
                                        inventory[currentTile] += 1
        #cursor.execute(
        query = '''UPDATE data SET dirt="{0}", grass={1}, wood={2}, stone={3}, water={4}, coal={5}, iron={6}, glass={7}, fire={8}, steel={9}, clay={10}, brick={11} WHERE user="player1"'''.format(
                                                                          inventory[DIRT],
                                                                          inventory[GRASS],
                                                                          inventory[WOOD],
                                                                          inventory[STONE],
                                                                          inventory[WATER],
                                                                          inventory[COAL],
                                                                          inventory[IRON],
                                                                          inventory[GLASS],
                                                                          inventory[FIRE],
                                                                          inventory[STEEL],
                                                                          inventory[CLAY],
                                                                          inventory[BRICK]
                                                                         )
                       #)
        cursor.execute(query)
        #displays the invntory
        placepos = 10
        for item in resources:
                DISPLAYSURF.blit(colours[item],(placepos,MAPHEIGHT*TILESIZE+20))
                placepos += 30
                textobj = font.render(str(inventory[item]), True, WHITE, BLACK)
                DISPLAYSURF.blit(textobj,(placepos,MAPHEIGHT*TILESIZE+20))
                placepos += 50
        #display update
        for row in range(MAPHEIGHT):
                for column in range(MAPWIDTH):
                        DISPLAYSURF.blit(colours[tilemap[row][column]], (column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))
        DISPLAYSURF.blit(player,(playerpos[0]*TILESIZE,playerpos[1]*TILESIZE))
        pygame.display.update()
conn.close()
        
