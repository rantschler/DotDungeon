import gameview 

class Model:
    
    def __init__(self,map = None, player = None):
        
        self.random = Random(99)
        
        end_tile = self.create_map()
        
        room = self.map.get_room(0)
        square = room.get_random()
        
        self.player = Dude(square,self.random.new())
        self.player.set_name("Player")
        self.player.set_viewer(gameview.classic_dude)
##         
##         macguffin = Item("Maltese MacGuffin")
##         macguffin.set_viewer(gameview.classic_useless)
##         end_room = self.map.get_room(2)
##         tile = end_room.get_random()
##         tile.add_item(macguffin)
##         
##         stairway = self.map.get_square((0,2))
##         quest = Quest(stairway,macguffin)
##         self.player.add_quest(quest)
##         
##         
##         monster = Dude(self.map.get_square((29,21)),self.random.new())
##         monster.set_name("Wizard of Guff")
##         monster.set_viewer(gameview.classic_badass)
##         monster.set_control(AI(monster,random_walk))
##         self.map.add_occupant(monster)
##         
##         guffy = Dude(end_tile,self.random.new())
##         guffy.set_name("Guffy McGufface")
##         guffy.set_viewer(gameview.inverse_statue)
##         guffy.make_immortal()
##         guffy.set_control(AI(guffy,stay_put))
##         self.map.add_occupant(guffy)
##         
##         x,y = guffy.get_position()
##         if y > 20:
##             door = self.map.get_square(-5)
##         else:
##             door = self.map.get_square(-6)
##         door.set_viewer(gameview.classic_door)
##         
##         self.add_room(Room(3,self.random.new()),(x-6,y-6))
##         
##         if y > 20:
##             door.get_neighbor(8).make_open()
##             
##         else:
##             door.get_neighbor(4).make_open()
##             
##         
##         key = Item("Guffy's Key")
##         key.set_viewer(gameview.classic_key)
##         quest_room = self.map.get_room(3)
##         tile = quest_room.get_random()
##         tile.add_item(key)
##             
##         quest = Quest(guffy,key)
##         guffy.add_quest(quest)
##         quest.set_unlockable(door)
        
    

    
    def create_map(self):
        
        map = MapMaker((35,35),4)
        self.map = map.make_map(1) ## Nmber is size of dude.
        
    
    def get_map(self):
        
        return self.map
    
    def get_player(self):
        
        return self.player
    
    def update(self,dt):
        
        # print "Model.update()"
        
        death = self.map.update(dt)
        self.map.line_of_sight(self.player)
        
        return death

#
#  Map Classes
#

class Map:
    
    """ A single level's map. 
        A level can include multiple z-levels.   """
    
    def __init__(self, size = (25,25),seed = 0):
        
        self.seed = seed
        
        self.squares = []
        self.rooms = []
        
        self.board = gameview.Board(self,size)
        
        self.occupants = []
        
        #
        # Kludges
        #
        
        self.ready = True  ## If true, redraws map.
        
    def add_square(self,square):
        
        self.assign_neighbors(square)
        self.squares.append(square)
    
    def add_room(self,room):
        
        self.rooms.append(room)
    
    def assign_neighbors(self,new_square):
        """ Take a new square and determine it it has any neighbors.
            If so, add neighbors to direction list. """
            
        x0,y0 = new_square.get_position()
        for square in self.squares:
            pos = square.get_position()
            if ( x0 - 1 , y0 + 1 ) == pos:
                new_square.set_neighbor(square,1)
                square.set_neighbor(new_square,9)
            elif ( x0 , y0 + 1 ) == pos:
                new_square.set_neighbor(square,2)
                square.set_neighbor(new_square,8)
            elif ( x0 + 1 , y0 + 1 ) == pos:
                new_square.set_neighbor(square,3)
                square.set_neighbor(new_square,7)
            elif ( x0 - 1 , y0 ) == pos:
                new_square.set_neighbor(square,4)
                square.set_neighbor(new_square,6)
            elif ( x0 + 1 , y0  ) == pos:
                new_square.set_neighbor(square,6)
                square.set_neighbor(new_square,4)
            elif ( x0 - 1 , y0 - 1 ) == pos:
                new_square.set_neighbor(square,7)
                square.set_neighbor(new_square,3)
            elif ( x0 , y0 - 1 ) == pos:
                new_square.set_neighbor(square,8)
                square.set_neighbor(new_square,2)
            elif ( x0 + 1 , y0 - 1 ) == pos:
                new_square.set_neighbor(square,9)
                square.set_neighbor(new_square,1)
    
    def fill_walls(self):
        """ Find places where squares have no neighbors.
            Add walls to those places. """
        
        for square in self.squares:
            if square.is_open():
                x0,y0 = square.get_position()
                if not square.get_neighbor(1):
                    new_square = Square(self,( x0 - 1 , y0 + 1 ))
                    self.add_square(new_square)
                if not square.get_neighbor(2):
                    new_square = Square(self,( x0  , y0 + 1 ))
                    self.add_square(new_square)
                if not square.get_neighbor(3):
                    new_square = Square(self,( x0 + 1 , y0 + 1 ))
                    self.add_square(new_square)
                if not square.get_neighbor(4):
                    new_square = Square(self,( x0 - 1 , y0  ))
                    self.add_square(new_square)
                if not square.get_neighbor(6):
                    new_square = Square(self,( x0 + 1 , y0 ))
                    self.add_square(new_square)
                if not square.get_neighbor(7):
                    new_square = Square(self,( x0 - 1 , y0 - 1 ))
                    self.add_square(new_square)
                if not square.get_neighbor(8):
                    new_square = Square(self,( x0 , y0 - 1 ))
                    self.add_square(new_square)
                if not square.get_neighbor(9):
                    new_square = Square(self,( x0 + 1 , y0 - 1  ))
                    self.add_square(new_square)

    def add_occupant(self,occupant):
        
        if not occupant in self.occupants:
            self.occupants.append(occupant)
    
    def remove_occupant(self,occupant):
        
        if occupant in self.occupants:
            self.occupants.remove(occupant)
    
    def get_square(self,pos=None):
        """ Searches map for a square at a given position. """
        
        if type(pos) == int:
            return self.squares[pos]
        elif pos == None:
            return random.choice(self.squares)
        else:
            for square in self.squares:
                if square.get_position() == pos:
                    return square
        
        return None
    
    def get_board(self):
        
        return self.board
    
    def get_room(self,id):
        """ Searches for a room with a given integer ID. """
        
        for room in self.rooms:
            if room.get_id() == id:
                return room
        
        return None
    
    def update(self, dt = 1):
        
        death = None
        for occupant in self.occupants:
            death = occupant.update(dt)
        
        return death

    def preview(self,scale=1):
        
        for square in self.squares:
            position = square.get_position()
            picture = square.view(square,scale)
            self.board.draw_object(picture,position,scale)
        
        map = self.board.view()
        
        return map
    
    
    def line_of_sight(self,dude,scale = 25):
        
        los = dude.get_line_of_sight()
        
        # print "Map.line_of_sight",los
        
        for square in los:
            position = square.get_position()
            picture = square.view(square,scale)
            self.board.draw_object(picture,position,scale)
            
        
    def view(self,scale = 1):
        
        if self.ready:
            self.preview(scale)
            self.ready = False
        
        return self.board.view()
        
 




class Room:
    
    def __init__(self,id,random):
        
        self.id = id
        self.center = None
        if random:
            self.random = random
        else:
            self.random = Random(12345)
            print "gamemodel.Room.__init__","Error: No RNG in declaration"
            
        self.members = []
        self.exits = []
    
    def __str__(self):
        
        return str(self.id)
    
    def set_center(self,square):
        """ Either a tuple for a position or
                   a square for a central tile. """
        
        self.center = square
        
    def get_center(self):
        """ Either a tuple for a position or
                   a square for a central tile. """
        
        return self.center
    
    def get_squares(self):
        
        return self.members
    
    def add_exit(self,square):
        """ Adds a square that is adjacent to the room and is
            in an acceptible place for a door or similar barrier. """
            
        self.exits.append(square)
    
    def add_square(self,square):
        
        if not square in self.members:
            self.members.append(square)
        
    def get_random(self):
        """ Returns a random tile from the room. """
        ## Warning: don't know if extra tiles yet.
        ## Need to correct for overwrites and deletions. 
        
        if self.members:
            return self.random.choice(self.members)
        
        return None
    
    def get_id(self):
        
        return self.id

class Square:
     
    def __init__(self,map,pos = [0,0]):
        
        self.name = "Wall"
        self.room = None
        self.map = map
        
        self.x = pos[0]
        self.y = pos[1]
        self.z = 0
        
        self.open = False
        self.locked = False
        
        self.occupant = None
        self.contains = []
        
        self.neighbors = [None]*10
        
        self.set_viewer(gameview.classic_hash)
    
    def set_room(self,room):
        
        self.room = room
        room.add_square(self)
    
    def is_open(self):
        
        return self.open
    
    def is_locked(self):
        
        return self.locked
    
    def unlock(self):
        
        self.locked = False
    
    def lock(self):
        
        self.locked = True
    
    def get_occupant(self):
        
        return self.occupant
    
    def get_neighbor(self,dir):
        
        return self.neighbors[dir]
    
    def get_neighbors(self):
        
        return list(self.neighbors)
    
    def get_neighboring_squares(self):
        
        out = list(set(list(self.neighbors)))
        if None in out:
            out.remove(None)
        
        return out
        
    def get_position(self):
        
        return self.x,self.y
    
    def set_neighbor(self,square,pos):
        
        self.neighbors[pos] = square
        
    def set_name(self,name):
        
        self.name = name
        
    def set_position(self,position):
        
        self.x , self.y = position
    
    def set_occupant(self,occupant):
        
        self.occupant = occupant
        if occupant:
            for item in self.contains:
                inventory = occupant.get_inventory()
                if inventory.add_item(item):
                    self.contains.remove(item)
    
    def delete_occupant(self):
        
        if self.occupant:
            occupant = self.occupant
            self.map.remove_occupant(occupant)
            self.occupant = None
    
    def add_item(self,item):
        
        self.contains.append(item)
    
    def make_open(self):
        """ Allows travel through a square. """
        
        self.name = "Room"
        self.open = True
        self.set_viewer(gameview.empty_square)
    
        
    def set_viewer(self,viewer):
        
        self.view = viewer


#
# Map Constructors
#

class MapMaker:
    
    def __init__(self,size=(35,35),zones = 1,random = None,level = 1,file = "blank.txt"):
        
        #
        # size - tuple of no. of tiles in a zone
        # zones - number of zones
        # random - random number generator
        # level - level reference
        # file - style for the map
        #
        
        self.scale = 1
        self.x,self.y = size

        self.level = level
        self.file = file
        
        self.zones = zones
        #
        #  Random(99) = hv,hv   **
        #  Random(125) = hv,hh
        #  Random(529) = vv,vh
        #
        self.random = Random(111)


        self.initilize_map(zones)
        
        
    def initilize_map(self,zones):
        """ Makes a map of blank squares. """
        
        scales = ((1,1),(2,1),(2,2),(2,2))
        
        sx,sy = scales[zones-1]
        
        self.map = []
        
        for i in range(self.y*sy):
            row = []
            for j in range(self.x*sx):
                row.append(None)
            self.map.append(list(row))
            
        
        self.zones = []
        offsets = [(0,0),(self.x,0),(0,self.y),(self.x,self.y)]
        for i in range(zones):
            self.zones.append(Zone(self.random.new(),offsets[i]))
            
    def add_room(self,room,pos):
        
        data = [ [2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]]
        
        n =  0
        x,y = 0,0
        off_x , off_y = pos
        for row in range(len(data)):
            for column in range(len(data[row])):
                n += 1
                type = data[column][row]
                px = row+off_x
                py = column+off_y
                self.map[py][px] = Tile(type,(px,py),room)
                y += column + off_y
                x += row + off_x
        
        x //= n
        y //= n
        
        room.set_center((off_x+2,off_y + 2))
    
    def add_corridor_segment(self,start,end,begin = False):
        """ Adds a linear corridor segment to map. """
        
        #
        # Does bad, bad things if dx != 0 or dy != 0
        # To make diagonal corridors, must change.
        #
        
        st_x,st_y = start
        en_x,en_y = end
        
        dx = en_x - st_x
        dy = en_y - st_y
        dist = max([abs(dx),abs(dy)])
        
        if dx == 0:
            sgn_x = 0
        else:
            sgn_x = dx/abs(dx)
        if dy == 0:
            sgn_y = 0
        else:
            sgn_y = dy/abs(dy)
        
        if begin:
            last = 2
        else:
            last = 1
            
        for i in range(dist):
            x,y = st_x+i*sgn_x,st_y+i*sgn_y
            if not self.map[y][x]:
                if last != 2:
                    self.map[y][x] = Tile(1,(x,y))
                else:
                    room = self.map[y-i*sgn_y][x-i*sgn_x].get_room()
                    self.map[y][x] = Tile(3,(x,y),room)
                    last = 1
            else:
                if last != 2:
                    if self.map[y][x]== 2:  
                        room = self.map[y][x].get_room()
                        x1,y1= x-i*sgn_x,y-i*sgn_y
                        self.map[y1][x1].set_type(3)
                        self.map[y1][x1].set_room(room)
                        last = 2
                ##
                ## Uncomment to remove corridor door tiles.
                ##
                ## elif self.map[st_y+i*sgn_y][st_x+i*sgn_x]== 1:
                ##   last = 1
                    
    
    def add_corridor(self,room1,room2):
        """ Adds a randomly shaped corridor between rooms. """
        
        st_x,st_y = room1.get_center()
        ed_x,ed_y = room2.get_center()
        
        dx = ed_x - st_x
        dy = ed_y - st_y
        
        if dx != 0:
            sgn_x = dx/abs(dx)
        else: 
            sgn_x = 0
            
        if dy != 0:
            sgn_y = dy/abs(dy)
        else: 
            sgn_y = 0
        
        
        directions = ["hh","vv"]
        if abs(dx) > 5:
            directions.append("vh")
        if abs(dy) > 5:
            directions.append("hv")
            
        
        dir = self.random.choice(directions)
        
        if dir == "hh":
            
            i = dx // 2
            start = st_x,st_y
            end = st_x + i,st_y
            self.add_corridor_segment(start,end,True)
            
            j = dy
            start = end
            end = st_x + i,st_y + j
            self.add_corridor_segment(start,end)
            
            k = dx 
            start = end
            end = st_x + k,st_y + j
            self.add_corridor_segment(start,end)
        
        elif dir == "hv":
            
            i = dx
            start = st_x,st_y
            end = st_x + i,st_y
            self.add_corridor_segment(start,end,True)
            
            j = dy
            start = end
            end = st_x + i,st_y + j
            self.add_corridor_segment(start,end)
                
        elif dir == "vh":
            
            i = dy
            start = st_x,st_y
            end = st_x,st_y+i
            self.add_corridor_segment(start,end,True)
            
            j = dx
            start = end
            end = st_x + j,st_y +i
            self.add_corridor_segment(start,end)
        
        elif dir == "vv":
            
            
            i = dy // 2
            start = st_x,st_y
            end = st_x,st_y + i
            self.add_corridor_segment(start,end,True)
            
            j = dx
            start = end
            end = st_x + j,st_y + i
            self.add_corridor_segment(start,end)
            
            k = dy
            start = end
            end = st_x + j,st_y + k
            self.add_corridor_segment(start,end)
                    
    def place_rooms(self,zone,number):
        
        x1,y1 = zone.get_offset()
        
        high = False
        
        division = self.x // number
        dx = division - 5
        
        rooms= []
        
        for i in range(number):
            x0 = division * i + x1 + 1
            if high:
                y0 = self.y - 16 + y1 + 1
            else:
                y0 = y1 +1
            high = not high
            
            x = x0 + self.random.choice(range(dx))
            y = y0 + self.random.choice(range(10))
            
            room = Room(i,None)
            self.add_room(room,(x,y))
            rooms.append(room)
            zone.append(room)
            
        
        return  rooms
    
    def place_corridors(self,zone):
        
        placed = [zone.get_room(0)]
        unplaced = list(zone.get_last_rooms())
        
        for room in unplaced:
            n = 0
            possibles = list(placed)
            old = self.random.choose(possibles)
            self.add_corridor(old,room)
            if possibles:
                n += 1
                apply = [True] + n*[False]
                if self.random.choice(apply):
                    old = self.random.choose(possibles)
                    self.add_corridor(old,room)
            placed.append(room)
            
                    
    
    
    def connect_zones(self,exclued = False):
        
        #
        # Excluded excludes quest rooms from connecting between zones.
        #
        
        if len(self.zones) == 1:
            
            return None
            
        elif len(self.zones) == 4:
            
            zone1r = self.zones[0].get_rightmost()
            zone2l = self.zones[1].get_leftmost()
            zone1d = self.zones[0].get_bottomost()
            zone3u = self.zones[2].get_topmost()
            zone3r = self.zones[2].get_rightmost()
            zone4l = self.zones[3].get_leftmost()
            
            
            self.add_corridor(zone1r,zone2l)
            self.add_corridor(zone1d,zone3u)
            self.add_corridor(zone3r,zone4l)
            if self.random.choice([True,False]):
                zone2d = self.zones[1].get_bottomost()
                zone4u = self.zones[3].get_topmost()
                
                self.add_corridor(zone2d,zone4u)
                


    def make_map(self,scale = 1):
        
        
        for zone in self.zones:
            rooms = self.place_rooms(zone,3)
            self.place_corridors(zone) 
        
        self.connect_zones()
        
        
        m,n = 2,2  ## Turn into self.m, self.n decided on generation
        
        x = self.x * m * scale
        y = self.y * n * scale
        
        map = Map((x,y))
        
        self.imprint(map,scale)
        map.fill_walls()
        
        return map
    
    def imprint(self,map,scale):
        
        for line in self.map:
            for space in line:
                if space:
                    space.imprint(map,scale)
                    
        for zone in self.zones:
            for room in zone.get_rooms():
                map.add_room(room)
    
    def out_text(self):
        
        for i in self.map:
            for j in i:
                if j :                
                    print j,
                else:
                    print ".",
            print
        
class Tile:
    
    def __init__(self,type,pos,room = None):
        
        self.room = room
        self.x,self.y = pos
        self.type = type
    
    def __str__(self):
        
        return str(self.type)
    
    def __eq__(self,other):
        
        return self.type == other
    
    def get_room(self):
        
        return self.room
    
    def set_type(self,type):
        
        self.type = type
    
    def set_room(self,room):
        
        self.room = room
    
    def imprint(self,map,scale = 1):
        
        for i in range(scale):
            for j in range(scale):
                x,y = scale * self.x + i , scale * self.y + j
                square = Square(map,(x,y))
                square.make_open() 
                if self.type == 2:
                    square.set_room(self.room)
                    self.room.add_square(square)
                if self.type == 3:
                    self.room.add_exit(square)
                map.add_square(square)
        
class Zone:
    
    def __init__(self,random,offset = (0,0)):
        
        self.rooms = []
        self.random = random
        
        self.x,self.y = offset
        
    def append(self,new):
        
        self.rooms.append(new)
        
    def get_random(self):
        
        return self.random.choice(self.rooms)
    
    def get_offset(self):
        
        return self.x,self.y
    
    def get_room(self,n):
        
        return self.rooms[n]
    
    def get_rooms(self):
        
        return list(self.rooms)
    
    def get_last_rooms(self):
        
        return list(self.rooms[1:])
    
    def get_leftmost(self):
        
        x0 = 10000
        out = None
        
        for room in self.rooms:
            x,y = room.get_center()
            if x < x0:
                x0 = x
                out = room
        
        return room
        
    def get_rightmost(self):
        
        x0 = -1
        out = None
        
        for room in self.rooms:
            x,y = room.get_center()
            if x > x0:
                x0 = x
                out = room
        
        return room
        
    def get_topmost(self):
        
        y0 = -1
        out = None
        
        for room in self.rooms:
            x,y = room.get_center()
            if y > y0:
                y0 = y
                out = room
        
        return room

    def get_bottomost(self):
        
        y0 = 10000
        out = None
        
        for room in self.rooms:
            x,y = room.get_center()
            if y < y0:
                y0 = y
                out = room
        
        return room


#
# Monster Classes
#

class Dude:
    
    def __init__(self,square = None,random = None):
        
        self.name = None
        
        self.mortal = True
        
        self.ready = False
        
        self.inventory = Inventory(self,26)
        
        self.square = square
        square.set_occupant(self)
        
        self.random = random
        self.quests = []
        
        self.size = 1
        
        self.los = []
        
        self.control = None   ## None - Player , else AI class
        
    def get_line_of_sight(self):
        
        return self.los
    
    def set_name(self,name):
        
        self.name = name
    
    def add_quest(self,quest):
        
        self.quests.append(quest)
        
    def set_control(self,ai):
        
        self.control = ai 
    
    def make_immortal(self):
        
        self.mortal = False
    
    def get_mortal(self):
        
        return self.mortal
    
    def get_prospect(self,dir):
        
        return self.square.get_neighbor(dir)
    
    def get_position(self):
        
        return self.square.get_position()
    
    def get_square(self):
        """ Returns the upper-left square occupied by the dude. """
        
        return self.square
    
    def get_inventory(self):
        
        return self.inventory
        
    def get_occupied_squares(self):
        """ Returns a list of all squares occupied by the dude. """
        
        rows = [self.square]
        for i in range(self.size-1):
            square = rows[i].get_neighbor(2)
            rows.append(square)
        out = []
        for row in rows:
            temp = [row]
            for j in range(self.size-1):
                temp.append(temp[j].get_neighbor(6))
            
            out += temp
        
        return out
        
    
    def line_of_sight(self):
        
        out = self.get_occupied_squares()
        
        neighbors = []
        for square in out:
            neighbors += self.square.get_neighbors()
        print neighbors
        out += neighbors
        
        out = list(set(list(out)))
        out.remove(None)
        
        self.los = out
        
        return self.los
                
    
    def move_into(self,square):
        
        
        if self.quests:
            
            for quest in self.quests:
                if quest.get_target() == square:
                    if quest.check(self):
                        self.quests.remove(quest)
            
        if not square or not square.is_open():
            return None
        
        elif not square.is_open():
            
            if square.has_quest():
                self.get_quest(square)
                
            
        elif square.get_occupant() == None:
            self.square.set_occupant(None)
            self.square = square
            square.set_occupant(self)
            self.ready = True
            self.line_of_sight()
            return None
        
        else:
            old = square.get_occupant()
            if old.get_mortal():
                old.kill()
            else:
                if not old.transfer_quest(self):
                    for quest in self.quests:
                        if quest in old.get_quests():
                            quest.resolve(self) 
            return old
    
    def make_open(self):
        
        self.kill()
    
    def get_quests(self):
        
        return tuple(self.quests)
    
    def transfer_quest(self,other):
        
        if other.control:
            return False
        
        for quest in self.quests:
            if not quest in other.get_quests():
                quest.transfer(other)
                return True
            return False
    
    def kill(self):
        
        self.inventory.empty(self.square)
        self.square.delete_occupant()
    
    def update(self,dt = 1):
        
        self.los = self.line_of_sight()
        
        target = self.control.get_orders()
        
        death = self.move_into(target)
        
        return death
        
    def set_viewer(self,viewer):
        
        self.view = viewer

class Item:
    
    def __init__(self,name = "Thing"):
        
        self.set_name(name)
        
    def __str__(self):
        
        return self.get_name()
    
    def get_name(self):
        
        return self.name
    
    def set_name(self,name):
        
        self.name = name
    
    def set_viewer(self,viewer):
        
        self.view = viewer
        
        
class Inventory:
    
    def __init__(self,owner,size):
        
        self.owner = owner
        
        self.slots = dict([])
    
        self.init_slots(size)
    
    def init_slots(self,size):
        
        for i in range(size):
            self.make_slot()
        
    def make_slot(self):
        
        num = len(self.slots)
        
        if num < 26:
            key = chr(num + 97)
            self.slots[key] = None
        
    def get_item(self,key):
        
        return self.slots[key]
    
    def get_items(self):
        
        return self.slots.values()
    
    def add_item(self,item):
        
        keys = self.slots.keys()
        placed = False
        i = 0
        while not placed:
            if self.slots[keys[i]] == None:
                self.slots[keys[i]] = item
                return True
            i += 1
        
        return False
    
    def remove_item(self,item):
        
        pass
    
    def empty(self,square):
        
        for thing in self.slots.values():
            if thing:
                square.add_item(thing)
                self.remove_item(thing)
    
    def print_inventory(self):
        
        print self.slots
        
class AI:
    
    def __init__(self,owner,orders):
        
        self.owner = owner
        
        self.orders = orders
        
    def get_orders(self,knowledge = None):
        
        return self.orders(self.owner,knowledge)





#
# Story Classes
#

class Quest:
    
    def __init__(self,target,goal):
        
        self.target = target  ## Square or dude to resolve quest.
        self.goal = goal      ## Item or result to resolve quest.
        self.unlockable = None
    
    def get_target(self):
        
        return self.target
    
    def set_unlockable(self,target):
        
        self.unlockable = target
    
    def transfer(self,other):
        
        other.add_quest(self)
        if self.unlockable:
            self.unlockable.unlock()
            self.unlockable.make_open()
    
    def check(self,dude):
        
        if self.goal in dude.get_inventory().get_items():
            self.resolve(dude)
            return True
        
        else:
            return False
        
    def resolve(self,dude):
        
        self.target.make_open()
        




#
# Utilities
#


class Random:
    
    def __init__(self,seed = 1):
        
        self.seed = seed
        
        self.prime = 15485863   ## Prime number no. 1 million
        self.current = seed
        self.iteration = 0
        
        
    def next(self):
        """ Generate next prime. """
        
        self.iteration += 1
        new = self.current * self.prime
        new %= 100000000
    
        self.current = new
        
        return self.current
    
    def choice(self,stuff):
        
        """ Returns one member of a list. """
        
        index = self.next() * len(stuff) / 100000000
        
        return stuff[index]
    
    def choose(self,stuff):
        """ Removes random member, returns it. """
        
        member = self.choice(stuff)
        
        stuff.remove(member)
        
        return member
        
    
    def new(self):
        """ Returns a new random number generator with a random seed. """
        
        return Random(self.next())
    



        


def random_walk(owner,knowledge = None):
    
    square = owner.get_square()
    
    target = owner.random.choice(square.get_neighbors())

    return target
    
def stay_put(owner,knowledge = None):
    
    return None
        