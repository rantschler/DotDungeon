
import gameclass as gc
import pygame as pg
from pygame.locals import *

class Viewer:

    def __init__(self,size,area = (800,600)):
        
        self.scale = 25
        
        self.size = size
        self.screen = pg.display.set_mode(self.size,RESIZABLE,32)
        self.background = gc.Background(self.size,gc.BLACK)
        self.resize()
        
        self.view_area = area
        
    def subscribe_to_map(self,map):
        
        self.map = map
        map.get_board().set_viewer(self)
    
    def subscribe_to_player(self,player):
        
        self.player = player
    
    def get_scale(self):
        
        return self.scale
    
    def get_view_area(self):
        """ Returns the area of the active map. """
        
        return self.view_area
    
    def get_center(self):
        
        x,y = self.player.get_position()
        x *= self.scale
        y *= self.scale
        x += self.scale//2
        y += self.scale//2
        
        return x,y
    
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
        
        x,y = self.view_area
        x += 4
        y += 4
        pg.draw.rect(self.screen,gc.WHITE,((198,78),(x,y)))
        self.screen.blit(map,(200,80))
        
        #
        # Draw all objects above.
        
        #

        pg.display.update()


class Board:
    
    def __init__(self,map,size = (35,35)):
        
        #
        # size - # of squares side to side
        # scale - # of pixels per side of a square
        # area - view area
        #
        
        self.map = map
        self.x , self.y = size
    
    def set_viewer(self,viewer):
        """ Sets the view screen. """
        
        self.viewer = viewer
        
        scale = self.viewer.get_scale()
        
        x,y = self.x,self.y
        x *= scale 
        y *= scale 
        
        self.board = pg.Surface((x,y))
        self.board.convert()
        self.board.fill((63,63,63))
        
    def draw_object(self,pic,pos,scale):
        
        x,y = pos
        
        x *= scale
        y *= scale
        
        self.board.blit(pic,(x,y))
        
    def view(self,center=(100,100),size=(200,200)):
        
        size = self.viewer.get_view_area()
        center = self.viewer.get_center()
        scale = self.viewer.get_scale()
        
        x = - center[0] + size[0]//2
        y = - center[1] + size[1]//2
        
        self.out = pg.Surface(size)
        self.out.convert()
        self.out.blit(self.board,(x,y))
        
        return self.out
        

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

def classic_hash(self,scale = 15):
        
    out = pg.Surface((scale,scale))
    out.convert()
    out.fill((0,0,0))
        
    pg.draw.rect(out,(255,255,255),(1,1,scale-2,scale-2))
    
    size = int(float(scale) )
    push = int((scale - size)*4/3+3)
    gc.screenprint(out,"#",[push,-2],size,gc.BLACK)
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