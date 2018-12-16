
import gameclass as gc
import pygame as pg
from pygame.locals import *

class Viewer:

    def __init__(self,size):
        
        self.scale = 25
        
        self.size = size
        self.screen = pg.display.set_mode(self.size,RESIZABLE,32)
        self.background = gc.Background(self.size,gc.BLACK)
        self.resize()
        
        
    def subscribe_to_map(self,map):
        
        self.map = map
    
    def subscribe_to_player(self,player):
        
        self.player = player
    
    def resize(self):
        self.screen = pg.display.set_mode(self.size,RESIZABLE,32)
        self.background.resize(self.size)
    
    def update(self,interval):
        
        pass
    
    
    def view(self):
        ''' The view function draws things to the screen. '''
    
        self.background.draw(self.screen)
        scale = self.background.get_scale()
        offset = self.background.get_offset()
    
        #
        # Draw all objects below.
        #
        
        map = self.map.view(self.scale)
        self.screen.blit(map,(200,80))
        
        #
        # Draw all objects above.
        
        #

        pg.display.update()


class Board:
    
    def __init__(self,size = (800,600)):
        
        self.x , self.y = size
        
        self.board = pg.Surface(size)
        self.board.convert()
        self.board.fill((63,63,63))
        
    def draw_object(self,pic,pos,scale):
        
        x,y = pos
        
        x *= scale
        y *= scale
        
        self.board.blit(pic,(x,y))
        
    def view(self,center=(100,100),size=(200,200)):
        
        return self.board
        

def empty_square(self,scale = 15):
    
    
    out = pg.Surface((scale,scale))
    out.convert()
    out.fill((0,0,0))
        
    pg.draw.rect(out,(255,255,255),(1,1,scale-2,scale-2),1)
    
    if self.occupant:
        top = self.occupant.view(self.occupant,scale)
        out.blit(top,[0,0])
    elif self.contains:
        top = self.contains[0].view(self.contains[0],scale)
        out.blit(top,[0,0])
    elif self.room:
        gc.screenprint(out,str(self.room),[15,2],8)
        if self.room.get_center() == self:
            pg.draw.circle(out,(255,255,255),(7,17),3)
    
    return out
    
def filled_square(self,scale = 15):
        
    out = pg.Surface((scale,scale))
    out.convert()
    out.fill((0,0,0))
        
    pg.draw.rect(out,(255,255,255),(1,1,scale-2,scale-2))
        
    return out

def classic_dude(self,scale):
    
    out = pg.Surface((scale,scale))
    out.convert()
    out.fill((63,63,63))
    out.set_colorkey((63,63,63))
    
    size = int(float(scale) * 15 / 20 )
    push = int((scale - size)*2/3 + 1)
    gc.screenprint(out,"@",[push,0],size)
    
    return out
    
def classic_badass(self,scale):
    
    out = pg.Surface((scale,scale))
    out.convert()
    out.fill((63,63,63))
    out.set_colorkey((63,63,63))
    
    size = int(float(scale) * 15 / 20 )
    push = int((scale - size)*2/3 + 1)
    gc.screenprint(out,"W",[push,0],size,gc.YELLOW)
    
    return out
    
def inverse_statue(self,scale):
    
    out = pg.Surface((scale,scale))
    out.convert()
    out.fill(gc.WHITE)
    
    size = int(float(scale) * 15 / 20 )
    push = int((scale - size)*2/3 + 1)
    gc.screenprint(out,"G",[push,0],size,gc.BLACK)
    
    return out

def classic_useless(self,scale):
    
    out = pg.Surface((scale,scale))
    out.convert()
    out.fill((63,63,63))
    out.set_colorkey((63,63,63))
    
    size = int(float(scale) )
    push = int((scale)/4 + 1)
    gc.screenprint(out,"*",[push,push/2],size,gc.GOLDEN_ROD)
    
    return out

def classic_key(self,scale):
    
    out = pg.Surface((scale,scale))
    out.convert()
    out.fill((63,63,63))
    out.set_colorkey((63,63,63))
    
    size = int(float(scale)*3/4 )
    push = int((scale)/4 + 1)
    gc.screenprint(out,"-",[push,0],size,gc.GOLDEN_ROD)
    
    return out
    
def classic_up(self,scale):
    
    if self.open:
        bg = gc.BLACK
        fg = gc.WHITE
    else:
        bg = gc.WHITE
        fg = gc.BLACK
    
    out = pg.Surface((scale,scale))
    out.convert()
    out.fill(bg)
    
    size = int(float(scale) * 15 / 20 )
    push = int((scale - size)*2/3 + 1)
    gc.screenprint(out,"<",[push,0],size,fg)
    
    return out
    
def classic_door(self,scale):
    
    if self.locked:
        bg = gc.BLACK
        fg = gc.WHITE
    else:
        
        bg = gc.WHITE
        fg = gc.BLACK
    
    out = pg.Surface((scale,scale))
    out.convert()
    out.fill(bg)
    
    size = int(float(scale) * 15 / 20 )
    push = int((scale - size)*2/3 + 1)
    gc.screenprint(out,"+",[push,0],size,fg)
    
    return out