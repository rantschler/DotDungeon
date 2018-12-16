#
# Basic Video Game Physics module
# gameclass.py  v0.95
#

import pygame

### COLOR CONSTANTS ###

def color_constants():
    """ Color constant globals """

    global ALICE_BLUE, ANTIQUE_WHITE, AQUA, AQUAMARINE,AZURE
    global BEIGE, BISQUE, BLACK, BLANCHED_ALMOND, BLUE
    global BLUE_VIOLET, BROWN, BURLY_WOOD
    global CADET_BLUE, CHARTREUSE, CHOCOLATE, CORAL
    global CORNFLOWER_BLUE, CORNSILK, CRIMSON, CYAN
    global DARK_BLUE, DARK_CYAN, DARK_GOLDEN_ROD, DARK_GRAY
    global DARK_GREEN, DARK_KHAKI, DARK_MAGENTA, DARK_OLIVE_GREEN
    global DARK_ORANGE, DARK_ORCHID, DARK_RED, DARK_SALMON, DARK_SEA_GREEN 
    global DARK_SLATE_BLUE, DARK_SLATE_GRAY, DARK_TURQUOISE, DARK_VIOLET 
    global DEEP_PINK, DEEP_SKY_BLUE, DIM_GRAY, DODGER_BLUE
    global FIRE_BRICK, FLORAL_WHITE, FOREST_GREEN, FUCHSIA
    global GAINSBORO, GHOST_WHITE, GOLD, GOLDEN_ROD 
    global GRAY, GREEN, GREEN_YELLOW 
    global HONEY_DEW, HOT_PINK 
    global INDIAN_RED, INDIGO, IVORY
    global KHAKI
    global LAVENDER, LAVENDER_BLUSH, LAWN_GREEN, LEMON_CHIFFON
    global LIGHT_BLUE, LIGHT_CORAL, LIGHT_CYAN, LIGHT_GOLDEN_ROD_YELLOW
    global LIGHT_GRAY, LIGHT_GREEN, LIGHT_PINK, LIGHT_SALMON
    global LIGHT_SEA_GREEN, LIGHT_SKY_BLUE, LIGHT_SLATE_GRAY
    global LIGHT_STEEL_BLUE, LIGHT_YELLOW, LIME, LIME_GREEN, LINEN
    global MAGENTA, MAROON
    global MEDIUM_AQUA_MARINE, MEDIUM_BLUE, MEDIUM_ORCHID
    global MEDIUM_PURPLE, MEDIUM_SEA_GREEN, MEDIUM_SLATE_BLUE 
    global MEDIUM_SPRING_GREEN, MEDIUM_TURQUOISE, MEDIUM_VIOLET_RED 
    global MIDNIGHT_BLUE, MINT_CREAM, MISTY_ROSE, MOCCASIN
    global NAVAJO_WHITE, NAVY
    global OLD_LACE, OLIVE, OLIVE_DRAB, ORANGE, ORANGE_RED, ORCHID 
    global PALE_GOLDEN_ROD, PALE_GREEN, PALE_TURQUOISE, PALE_VIOLET_RED
    global PAPAYA_WHIP, PEACH_PUFF, PERU, PINK, PLUM, POWDER_BLUE, PURPLE
    global RED, ROSY_BROWN, ROYAL_BLUE 
    global SADDLE_BROWN, SALMON, SANDY_BROWN 
    global SEA_GREEN, SEA_SHELL
    global SIENNA, SILVER, SKY_BLUE
    global SLATE_BLUE, SLATE_GRAY
    global SNOW, SPRING_GREEN, STEEL_BLUE
    global TAN, TEAL, THISTLE, TOMATO, TURQUOISE
    global VIOLET
    global WHEAT, WHITE, WHITE_SMOKE
    global YELLOW, YELLOW_GREEN
    
    ALICE_BLUE = (240,248,255)
    ANTIQUE_WHITE = (250,235,215)
    AQUA = (0,255,255)
    AQUAMARINE = (127,255,212)
    AZURE = (240,255,255)
    BEIGE = (245,245,220)
    BISQUE = (255,228,196)
    BLACK = (0,0,0)
    BLANCHED_ALMOND = (255,235,205)
    BLUE = (0,0,255)
    BLUE_VIOLET = (138,43,226)
    BROWN = (165,42,42)
    BURLY_WOOD = (222,184,135)
    CADET_BLUE = (95,158,160)
    CHARTREUSE = (117,255,0)
    CHOCOLATE = (210,105,30)
    CORAL = (255,127,80)
    CORNFLOWER_BLUE = (100,149,237)
    CORNSILK = (255,248,220)
    CRIMSON = (220,20,60)
    CYAN = (0,255,255)
    DARK_BLUE = (0,0,139)
    DARK_CYAN = (0,139,139)
    DARK_GOLDEN_ROD = (184,134,11)
    DARK_GRAY = (169,169,169)
    DARK_GREEN = (0,100,0)
    DARK_KHAKI = (189,183,107)
    DARK_MAGENTA = (139,0,139)
    DARK_OLIVE_GREEN = (85,109,47) 
    DARK_ORANGE = (255,140,0)
    DARK_ORCHID = (153,50,204)
    DARK_RED = (139,0,0)
    DARK_SALMON = (233,150,122)
    DARK_SEA_GREEN = (143,188,143)
    DARK_SLATE_BLUE = (48,61,139)
    DARK_SLATE_GRAY = (47,79,79)
    DARK_TURQUOISE = (0,206,209)
    DARK_VIOLET = (148,0,211)
    DEEP_PINK = (255,20,147)
    DEEP_SKY_BLUE = (0,191,255)
    DIM_GRAY = (105,105,105)
    DODGER_BLUE = (30,144,255)
    FIRE_BRICK = (178,34,34)
    FLORAL_WHITE = (255,250,240)
    FOREST_GREEN = (34,139,34)
    FUCHSIA = (255,0,255)
    GAINSBORO = (220,220,220)
    GHOST_WHITE = (248,248,255)
    GOLD = (255,215,0)
    GOLDEN_ROD = (218,165,32)
    GRAY = (128,128,128)
    GREEN = (0,128,0)
    GREEN_YELLOW = (173,255,47)
    HONEY_DEW =  (240,255,240)
    HOT_PINK = (255,105,132)
    INDIAN_RED = (205,92,92)
    INDIGO = (75,0,130)
    IVORY = (255,255,240)
    KHAKI = (240,230,140)
    LAVENDER = (230,230,250)
    LAVENDER_BLUSH = (255,240,245)
    LAWN_GREEN = (124,252,0)
    LEMON_CHIFFON = (255,250,205)
    LIGHT_BLUE = (173,216,230)
    LIGHT_CORAL = (240,128,128)
    LIGHT_CYAN = (244,255,255)
    LIGHT_GOLDEN_ROD_YELLOW = (250,250,210)
    LIGHT_GRAY = (211,211,211)
    LIGHT_GREEN = (144,238,144)
    LIGHT_PINK = (255,182,193)
    LIGHT_SALMON = (255,160,122)
    LIGHT_SEA_GREEN = (20,178,170)
    LIGHT_SKY_BLUE = (135,206,250)
    LIGHT_SLATE_GRAY = (119,136,153)
    LIGHT_STEEL_BLUE = (176,196,222)
    LIGHT_YELLOW = (255,255,244)
    LIME = (0,255,0)
    LIME_GREEN = (50,205,50)
    LINEN = (250,240,230)
    MAGENTA = (255,0,255)
    MAROON = (128,0,0)
    MEDIUM_AQUA_MARINE = (102,205,170)
    MEDIUM_BLUE = (0,0,205)
    MEDIUM_ORCHID = (186,85,211)
    MEDIUM_PURPLE = (147,112,219)
    MEDIUM_SEA_GREEN = (60,179,113)
    MEDIUM_SLATE_BLUE = (123,104,238)
    MEDIUM_SPRING_GREEN = (0,250,154)
    MEDIUM_TURQUOISE = (72,209,204)
    MEDIUM_VIOLET_RED = (199,21,204)
    MIDNIGHT_BLUE = (25,25,112)
    MINT_CREAM = (245,255,250)
    MISTY_ROSE = (255,228,225)
    MOCCASIN = (255,228,181)
    NAVAJO_WHITE = (255,222,173)
    NAVY = (0,0,128)
    OLD_LACE = (253,245,230)
    OLIVE = (128,128,0)
    OLIVE_DRAB = (107,142,35)
    ORANGE = (255,165,0)
    ORANGE_RED = (255,69,0)
    ORCHID = (218,122,214)
    PALE_GOLDEN_ROD = (238,232,170)
    PALE_GREEN = (152,251,152)
    PALE_TURQUOISE = (175,238,238)
    PALE_VIOLET_RED = (219,112,147)
    PAPAYA_WHIP = (255,239,213)
    PEACH_PUFF = (255,218,185)
    PERU = (205,133,63)
    PINK = (255,192,203)
    PLUM = (221,160,221)
    POWDER_BLUE = (176,224,230)
    PURPLE = (128,0,128)
    RED = (255,0,0)
    ROSY_BROWN = (188,143,143)
    ROYAL_BLUE = (65,105,225)
    SADDLE_BROWN = (139,69,19)
    SALMON = (250,128,114)
    SANDY_BROWN = (250,164,96)
    SEA_GREEN = (46,139,87)
    SEA_SHELL = (255,250,238)
    SIENNA = (160,82,45)
    SILVER = (192,192,192)
    SKY_BLUE = (135,206,235)
    SLATE_BLUE = (106,90,205)
    SLATE_GRAY = (112,128,144)
    SNOW = (255,250,250)
    SPRING_GREEN = (0,255,127)
    STEEL_BLUE = (70,130,180)
    TAN = (210,180,140)
    TEAL = (0,128,128)
    THISTLE = (216,191,216)
    TOMATO = (255,99,71)
    TURQUOISE = (64,224,208)
    VIOLET = (238,130,238)
    WHEAT = (245,222,179)
    WHITE = (255,255,255)
    WHITE_SMOKE = (245,245,245)
    YELLOW = (255,255,0)
    YELLOW_GREEN = (154,205,50)

color_constants()

### GAMESCLASS FUNCTIONS ###

def meld_colors(color1,color2,pct):
    
    x,y,z = color1
    u,v,w = color2
    
    a = (x*x*(1.0-pct)+u*u*pct)**0.5
    b = (y*y*(1.0-pct)+v*v*pct)**0.5
    c = (z*z*(1.0-pct)+w*w*pct)**0.5
    
    return a,b,c
    
def screenprint(screen = None,message="",position = [0,0],size = 20,color = WHITE,font = "Arial"):
    ''' Prints a message on the PyGame screen. 
            screen - the PyGame object on which to place text
            message - the string object to print on the screen
            positon - a two-element list of integers describing where to
                        print the message on the screen
            size - an integer representing the size of text to print
            color - a PyGame color or a gameclass color constant
            font - a string representing the font to print on the screen  
    '''

    position = (int(position[0]),int(position[1]))
    
    message = str(message)
    
    outputfont = pygame.font.SysFont(font,size)
    outputmessage = outputfont.render(message,1,color)
    
    if screen:
        screen.blit(outputmessage,position)
        
    return outputmessage

def format_time(time):
    """ Takes the time in milliseconds and returns a properly formatted
        time mm:ss.dd. """
    
    output = ""
    
    time /= 100
    
    decimal = time % 10
    
    str_decimal = str(decimal)
    
    time /= 10
    
    seconds = time % 60
    
    str_seconds = str(seconds)
    
    if seconds < 10:
        str_seconds = "0"+str_seconds 
    
    time /= 60
    
    minutes = time % 60
    
    str_minutes = str(minutes)
    
    if minutes < 10:
        str_minutes = "0"+str_minutes 
    
    output = str_minutes + ":" +str_seconds+ "." + str_decimal
    
    return output

def draw_not(screen,position = (0,0),size = 20,color = WHITE,bgcolor = BLACK):
    '''
    Draws a circle with a symbol for not inside of it.
    
    The position is the upper left hand corner of the symbol, 
    the size is its diameter.
    The color and bgcolor are gameclass colors.
    '''
    
    center = [0,0]
    center[0] = position[0] + size // 2
    center[1] = position[1] + size // 2
    radius = size // 2
    
    point1 = (center[0] - radius//3,center[1])
    point2 = (center[0] + radius//3,center[1])
    
    
    pygame.draw.circle(screen,color,center,radius)
    
    pygame.draw.circle(screen,bgcolor,center,radius-radius//5)
    
    pygame.draw.line(screen,color,point1,point2,radius // 5)
    
    pass
    
def draw_and(screen,position = (0,0),size = 20,color = WHITE,bgcolor = BLACK):
    '''
    Draws a circle with a symbol for and inside of it.
    
    The position is the upper left hand corner of the symbol, 
    the size is its diameter.
    The color and bgcolor are gameclass colors.
    '''
    
    center = [0,0]
    center[0] = position[0] + size // 2
    center[1] = position[1] + size // 2
    radius = size // 2
    
    point1 = (center[0] - radius//3,center[1] + radius // 3)
    point2 = (center[0],center[1] - radius // 3)
    point3 = (center[0] + radius//3,center[1] + radius // 3)
    
    
    pygame.draw.circle(screen,color,center,radius)
    
    pygame.draw.circle(screen,bgcolor,center,radius-radius//5)
    
    pygame.draw.line(screen,color,point1,point2,radius // 5)
    pygame.draw.line(screen,color,point3,point2,radius // 5)
    
    pass
    
def draw_or(screen,position = (0,0),size = 20,color = WHITE,bgcolor = BLACK):
    '''
    Draws a circle with a symbol for or inside of it.
    
    The position is the upper left hand corner of the symbol, 
    the size is its diameter.
    The color and bgcolor are gameclass colors.
    '''
    
    
    center = [0,0]
    center[0] = position[0] + size // 2
    center[1] = position[1] + size // 2
    radius = size // 2
    
    point1 = (center[0] - radius//3,center[1] - radius // 3)
    point2 = (center[0],center[1] + radius // 3)
    point3 = (center[0] + radius//3,center[1] - radius // 3)
    
    
    pygame.draw.circle(screen,color,center,radius)
    
    pygame.draw.circle(screen,bgcolor,center,radius-radius//5)
    
    pygame.draw.line(screen,color,point1,point2,radius // 5)
    pygame.draw.line(screen,color,point3,point2,radius // 5)
    
    pass

### GAMECLASS CLASSES ###
    

class Background:
    """ A modifiable background object that can be drawn on during the
        operation of the game.  """
        
    def __init__(self,screen_size,color = BLACK):
            
        self.color = color
        self.base = pygame.Surface(screen_size)
        self.base.convert()
        self.base.fill(color)
        
        self.field = None
        
        self.scale = 1.0
        self.offset = (0.0,0.0)
        
        pass
    
    def make_field(self,drawer,size=(80.0,60.0),scale =0.5, offset=(0.0,0.0)):
        
        self.field = Field(field_size,field_scale,field_offset)
        self.field.imprint(drawer,self)
    
    def get_field(self):
        
        return self.field
    
    def get_size(self):
        """ Returns the size of the background image. """
        
        return self.base.get_size()
    
    def set_scale(self,value):
        
        self.scale = value
        
    def set_offset(self,value):
        
        self.offset = value
    
    def get_scale(self):
        
        return self.scale
        
    def get_offset(self):
        
        return self.offset
    
    def resize(self,size):

        self.base = pygame.Surface(size)
        self.base.convert()
        self.base.fill(self.color)
    
           
    def clear(self):
        """ Blanks out the background to be its currently assigned 
            background color. """
            
        self.base.fill(self.color)
    
    def fill(self,color):
        """ Fills the background with the given color and sets that
            color as the new background color for other operations. """
            
        self.color = color
        self.base.fill(color)
        
    def detail(self,detail,position):
        """ Overlays a picture on top of the current background. """
        
        self.base.blit(detail,position)
        
    def draw(self,screen):
        """ Draws the background. """
        
        screen.blit(self.base,(0,0))


class Foreground:
    
    def __init__(self,background,image = None):
        
        pos = background.get_size()
        
        if image:
            self.image = image(self,background)
        else:
            self.image = None
        
        self.width = pos[0]
        self.height = pos[1]
        
        self.message = []
        self.msg_output = True
        self.msg_state = 0
        self.msg_counter = 0
        self.msg_counter_max = 30
        
        self.score = 0
        self.best = 0
        
        pass
        
    def append_message(self,value):
        
        self.message.append(str(value))
        
        pass
    
    def disable_messages(self):
        
        self.msg_output = False
        
        pass
    
    def enable_messages(self):
        
        self.msg_output = True
        
        pass
    
    def draw_message(self,screen):
        
        if self.msg_output and self.message:
            message = self.message[self.msg_state]
            
            pos = [0,0]
            pos[0] = self.width // 2 - 5 * len(message)
            pos[1] = self.height //2 - 20
            screenprint(screen,message,pos)
            
            if self.msg_counter >= self.msg_counter_max:
                self.msg_state += 1
                self.msg_counter = 0
            else:
                self.msg_counter += 1
            if self.msg_state >= len(self.message):
                self.msg_state = 0
        
            
    
    def draw(self,screen):
        
        self.image.blit(screen)
        
        self.draw_score(screen)
        self.draw_best(screen)
        self.draw_message(screen)
        
        pass


class Field:
    
    def __init__(self,size,art = None):
        
        #
        # Physical size of field.
        #
        
        self.x = 0.0
        self.y = 0.0
        
        self.w = size[0]
        self.h = size[1]
        
        #
        # Proportion of field on screen.
        #
        
        self.x_pct = 0.0
        self.y_pct = 0.0      
        
        self.w_pct = 1.0
        self.h_pct = 1.0
        
        #
        # Field 
        #
        
        self.art = art
    
    def set_offset(self,offset):
        
        self.x = float(offset[0])
        self.y = float(offset[1])
    
    def get_size(self):
        """ Returns width and height of the field in meters. """
        
        return (self.w,self.h)
    
    def get_fill(self):
        """ Returns the percentage of the screen that the field is
            expected to fill.  Reported relative to the widths. """
            
        return self.w_pct
    
    def get_scale(self):
        
        return self.art.get_scale()
    
    def get_offset(self):
        """ Returns the percentage of the screen to the top-left 
            corner of the field.  Both component are reported. """ 
            
        return (self.x,self.y)
    
    def get_edges(self):
        """ Returns the edges of the field in its own terms. """
        
        edge1 = [0,0]
        edge2 = self.get_size()
        
        return edges
    
    def set_position(self,pos):
        
        self.x_pct = pos[0]
        self.y_pct = pos[1]
    
    def contains(self,thing):
        """ Checks to see if an object is in the field. """
        
        pos = thing.get_position()
        
        in_x = 0.0 <= pos[0] <= self.w
        in_y = 0.0 <= pos[1] <= self.h
        
        return in_x and in_y
    
    def imprint(self,background):
        """ Imprints art_function on the background of the screen. 
            Requires a function that draws the background, which
                is drawn onto the background and does not change
                unless the imprint() method is called again. """
        
        self.art = background

class Strip:
    
    def __init__(self,base_cell):
        
        self.strip = base_cell
        self.length = 1
        self.cell_size = base_cell.get_size()
        self.strip_size = self.cell_size
        
        pass
        
    def __len__(self):
        
        return self.length
    
    def get_cell_size(self):
        
        return self.cell_size
        
    
    def add_cell(self,new_cell):
        
        new_width = self.strip_size[0] + self.cell_size[0]
        new_height = self.strip_size[1]
        
        new_size = (new_width,new_height)
        
        new_strip = pygame.Surface(new_size)
        new_strip.convert()
        
        new_strip.blit(self.strip,(0,0))
        new_strip.blit(new_cell,(self.strip_size[0],0))
        
        self.strip = new_strip
        self.strip_size = new_size
        self.length += 1
        
        pass
    
    def get_cell(self,number):
        
        pass
        
    def view_cell(self,screen,position = (0,0),number = 0):
        
        #cell = ...base cell...
        #if number < len(self):
        #    cell = ...single cell...
        #else:
        #    print "Error: Only "+str(len(self))+" cells in strip."
        
        screen.blit(cell,position)
        
        pass
        
    def draw(self,screen,position = (0,0)):
        
        screen.blit(self.strip,position)
        
        pass
        
class Button:
    
    def __init__(self,position,size,colors = [WHITE],text = [],border = None,delay_time = 0):
        """
        Creates a button on the screen 
        
            position - 2 element list, x and y position of left hand corner
            size - 2 element list, width and height of the button. 
            colors - 4 color constants:
                0 - color of main area of active button
                1 - color of the button while depressed
                3 - color of the deactivated button
                
                Only one element is necessary.  Any undefined colors will be
                set to the color of the main area of the button.
                
            text - See definitions under define_text()  
            border - two element list, color and size of the button border
            delay_time - The amount of time to deactivate button between clicks.
        """
        
        
        self.x = position[0]
        self.y = position[1]
        self.w = size[0]
        self.h = size[1]
        if len(size) == 3:
            self.b = size[2]
        else:
            self.b = 0
        
        if type(colors) == tuple and type(colors[0]) == int:
            colors = [colors]
        
        if type(colors) != list:
            colors = [colors]
        
        self.color_up   = colors[0]
        if len(colors) > 1:
            self.color_down = colors[1]
        else:
            self.color_down = colors[0]
        if len(colors) > 2:
            if colors[2] == None:
                self.color_off = "Invisible"
            else:
                self.color_off  = colors[2]
        else:
            self.color_off = colors[0]
        
        self.relabel(text)
        
        if border:
            self.b = border[1]
            self.color_edge = border[0]
        else:
            self.b = 0
            self.color_edge = colors[0]
        
        self.execute = False
        
        self.active = True
        self.delay = False
        self.timer = 0
        self.delay_time = delay_time
        
        pass
    
    def set_position(self,value):
        
        dx = self.x - value[0]
        dy = self.y - value[1]
        
        self.x = value[0]
        self.y = value[1]
        
        px = self.label_up_pos[0] - dx
        py = self.label_up_pos[1] - dy
    
        self.label_up_pos = (px,py)
    
    def is_clicked(self,position):
        ''' Checks if the button has been pressed.
            Returns True if mouse is in field of the button
                and the button is active.
            Returns False if the mouse is not in the field or
                the button is not active. '''
        
        if not self.active or self.delay:
            return False
        
        
        is_clicked = False
        
        x = position[0]
        y = position[1]
        
        in_x = 0 < x - self.x < self.w
        in_y = 0 < y - self.y < self.h
        is_clicked = in_x and in_y
        
        if is_clicked and self.delay_time > 0:
            self.timer = self.delay_time
            self.delay = True
            self.execute = True
        
        return is_clicked
    
    def is_active(self):
        ''' Returns the activation status of the button. '''
        
        return self.active
    
    def activate(self):
        ''' Sets the activation status of the button to active. '''
        
        self.active = True
        
        pass
    
    def deactivate(self):
        ''' Sets the activation status of the button to inactive. '''
        
        self.active = False
        
        pass
    
    def relabel(self,text = None):
        #
        # text[0] - button label
        #       Maybe single label, may be list of [on label,off label]
        # text[1] - size 
        # text[2] - color
        # text[3] - font
        #
        
        if type(text) == None:
            text = self.text
        elif type(text) == str:
            text = [text]
        
        if len(text) < 4:
            if text == []:
                text = [""]
            if len(text) == 1:
                text.append(self.h//2)
            if len(text) == 2:
                text.append(BLACK)
            text.append("Arial")
        center = (self.x+self.w/2,self.y+self.h/2)
        
        font = pygame.font.SysFont(text[3],text[1])
        
        if (type(text[0]) == list or type(text[0]) == tuple) and len(text[0]) == 2:
            self.label_up = font.render(text[0][0],1,text[2])
            self.label_down = font.render(text[0][1],1,text[2])
        elif type(text[0]) == str:
            self.label_up = font.render(text[0],1,text[2])
            self.label_down = self.label_up
        else:
            print "Error: Incorrect input for button text."
            print "       Button text should be either a single string or"
            print "       or a list of two strings."
            self.label_up = ""
            self.label_down = ""
        
        n = self.label_up.get_size()
        self.label_up_pos = (center[0]-n[0]/2,center[1]-n[1]/2)
        n = self.label_down.get_size()
        self.label_down_pos = (center[0]-n[0]/2,center[1]-n[1]/2)
        
        pass
    
    def update(self,time):
        
        if self.delay:
            self.timer -= time
            if self.timer < 0:
                self.timer = 0
                self.delay = False
    
    def draw(self,screen):
        
        if self.active and self.timer == 0:
            color = self.color_up
        elif self.active and self.timer > 0:
            color = self.color_down
        else:
            color = self.color_off
        
        u_in = (self.x,self.y)
        w_in = (self.w,self.h)
        u_out = (self.x - self.b,self.y-self.b)
        w_out = (self.w + 2 * self.b, self.h + 2 * self.b)
        
        pygame.draw.rect(screen,self.color_edge,(u_out,w_out))
        pygame.draw.rect(screen,color,(u_in,w_in))
        
        if self.timer > 0:
            screen.blit(self.label_down,self.label_down_pos)
            self.timer -= 1
            if self.timer == 0:
                self.delay = False
        else:
            screen.blit(self.label_up,self.label_up_pos)
        
        pass

class Light:
    
    def __init__(self,position=(0,0),size=100,colors=[WHITE,GRAY]):
        """ Creates a button on the screen 
        
            position - 2 element list, x and y position of upper-left corner
            size - 2 element list, radius and border width of the light.
                    If two elements are specified, then border is assumed zero
            colors - 4 color constants:
                0 - color of main area of active light
                1 - color of main area of deactivated light
                2 - color of the button edge
                
                Only the first two elements are necessary.  Any undefined 
                colors will be set to the color of the main area of the 
                button.
                
            text - See definitions under define_text  """
        
        
        if type(size) == int or type(size) == float:
            size = [int(size)]
            
        self.light_radius = size[0]
        if len(size) == 2:
            self.edge_radius = size[1] + self.light_radius
        else:
            self.edge_radius = self.light_radius
        
        self.x = position[0] + self.edge_radius 
        self.y = position[1] + self.edge_radius 
        
        self.color_on = colors[0]
        self.color_off = colors[1]
        
        if len(colors) > 2:
            self.color_edge = colors[2]
        else:
            self.color_edge = colors[0]
        
        self.on = False
        
        pass
    
    def is_active(self):
        ''' Returns the activation status of the light. '''
        
        return self.on
    
    def activate(self):
        ''' Sets the activation status of the button to active. '''
        
        self.on = True
        
        pass
    
    def deactivate(self):
        ''' Sets the activation status of the button to inactive. '''
        
        self.on = False
        
        pass
    
    def toggle(self):
        ''' Switches from on state to off state or vice-versa. '''
        
        self.on = not self.on
        
        pass
    
    def draw(self,screen):
        ''' Displays the light in its current status. '''
        
        pos = (self.x,self.y)
        
        if self.on:
            color = self.color_on
        else:
            color = self.color_off
            
        pygame.draw.circle(screen,self.color_edge,pos,self.edge_radius)
        pygame.draw.circle(screen,color,pos,self.light_radius)
        
        pass

class Impulsebar:
    """ Creates a bar that cycles through values low to high at a 
        given rate when pressed once.  When pressed again, returns
        the value at that point. """ 
        
    def __init__(self,pos,size,low = 0.0,high = 50.0,rate = 1.59):
        """ Initializes the impulse bar.  Variables:
                pos - a two element array for the x- and y- position
                        of the impulse bar's upper lefthand corner.
                size - a two element array representing the width
                        and height of the impulse bar.
                low -
                high-
                rate -
                
        """
        
        self.x = pos[0]
        self.y = pos[1]
        self.w = size[0]
        self.h = size[1]
        
        self.min = float(low)
        self.current = float(low)
        self.max = float(high)
        
        self.rate = float(rate)
        self.on = False
        
        pass
        
    def start(self):
        
        self.on = True
        self.current = self.min
        
        pass
    
    def stop(self):
        
        self.on = False
        
        return self.current
    
    def is_on(self):
        
        return self.on
    
    def is_clicked(self,pos):
        
        in_x = self.x < pos[0] < self.x + self.w
        in_y = self.y < pos[1] < self.y + self.h
        
        return in_x and in_y
    
    def set_value(self,value):
        
        if value < self.min:
            self.current = self.min
        elif value > self.max:
            self.current = self.max
        else:
            self.current = value
        
        pass

    def get_value(self):
        
        return self.current
        
    def update(self,interval = 1.0):
        
        if self.on:
            self.current += self.rate * interval
            if self.current > self.max:
                self.current = self.min
        
        pass
        
    def draw(self,screen):
        
        edge_color = WHITE
        fill_color = YELLOW
        lc_pos = (self.x,self.y)
        frame_size = (self.w,self.h)
        fill = int(float(self.w) * self.current/self.max)
        bar_size = (fill,self.h)
        
        pygame.draw.rect(screen,fill_color,[lc_pos,bar_size])
        pygame.draw.rect(screen,edge_color,[lc_pos,frame_size],3)
        
        pass
        