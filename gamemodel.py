import gameview
import random

class Model:
    
    def __init__(self,map = None, player = None):
        
        end_tile = self.create_map()
        
        self.player = Dude(self.map.get_square((2,2)))
        self.player.set_name("Player")
        self.player.set_viewer(gameview.classic_dude)
        
        macguffin = Item("Maltese MacGuffin")
        macguffin.set_viewer(gameview.classic_useless)
        end_room = self.map.get_room(2)
        tile = end_room.get_random()
        tile.add_item(macguffin)
        
        stairway = self.map.get_square((0,2))
        quest = Quest(stairway,macguffin)
        self.player.add_quest(quest)
        
        
        monster = Dude(self.map.get_square((29,21)))
        monster.set_name("Wizard of Guff")
        monster.set_viewer(gameview.classic_badass)
        monster.set_control(AI(monster,random_walk))
        self.map.add_occupant(monster)
        
        guffy = Dude(end_tile)
        guffy.set_name("Guffy McGufface")
        guffy.set_viewer(gameview.inverse_statue)
        guffy.make_immortal()
        guffy.set_control(AI(guffy,stay_put))
        self.map.add_occupant(guffy)
        
        x,y = guffy.get_position()
        if y > 20:
            door = self.map.get_square(-5)
        else:
            door = self.map.get_square(-6)
        door.set_viewer(gameview.classic_door)
        
        self.add_room(Room(3),(x-6,y-6))
        
        if y > 20:
            door.get_neighbor(8).make_open()
            
        else:
            door.get_neighbor(4).make_open()
            
        
        key = Item("Guffy's Key")
        key.set_viewer(gameview.classic_key)
        quest_room = self.map.get_room(3)
        tile = quest_room.get_random()
        tile.add_item(key)
            
        quest = Quest(guffy,key)
        guffy.add_quest(quest)
        quest.set_unlockable(door)
        print quest.unlockable
        
    
    def add_room(self,room,pos):
        
        data = [ [0,0,0,0,0],[0,1,1,1,0],[0,1,1,1,0],[0,1,1,1,0],[0,0,0,0,0]]
        
        self.map.add_room(room)
        off_x , off_y = pos
        for row in range(len(data)):
            for column in range(len(data[row])):
                square = Square(self.map,[row+off_x,column+off_y])
                if data[column][row]:
                    square.make_open()
                    square.set_room(room)
                self.map.add_square(square)
        
        room.set_center(self.map.get_square((off_x+2,off_y + 2)))
    
    def create_map(self):
        
        self.map = Map()
        
        room1 = Room(1)
        
        self.add_room(room1,(0,0))
        
        stairway = self.map.get_square((0,2))
        stairway.set_name("Exit")
        stairway.set_viewer(gameview.classic_up)
        
        choices = [self.map.get_square((2,4)),self.map.get_square((4,2))]
        start = random.choice(choices)
        start.make_open()
        
        room2 = Room(2)
        self.add_room(room2,(27,19))
                
        choices = [self.map.get_square((27,21)),self.map.get_square((29,19))]
        end = random.choice(choices)
        end.make_open()
        
        st_x,st_y = start.get_position()
        ed_x,ed_y = end.get_position()
        
        if st_x == 2 and ed_x == 27:
            
            for i in range(ed_y - st_y+1):
                square = Square(self.map,(st_x,st_y+i))
                square.make_open()
                self.map.add_square(square)
                
            for j in range(ed_x - st_x):
                square = Square(self.map,(st_x+j,st_y+i))
                square.make_open()
                self.map.add_square(square)
        
        elif st_x == 2 and ed_x == 29:
            
            for i in range((ed_y - st_y)//2+1):
                square = Square(self.map,(st_x,st_y+i))
                square.make_open()
                self.map.add_square(square)
                
                
            for j in range(ed_x - st_x+1):
                square = Square(self.map,(st_x+j,st_y+i))
                square.make_open()
                self.map.add_square(square)
            
            for k in range((ed_y - st_y)//2+1):
                square = Square(self.map,(st_x+j,st_y+i+k))
                square.make_open()
                self.map.add_square(square)
                
        
                
        elif st_x == 4 and ed_x == 29:
            
            for i in range(ed_x - st_x+1):
                square = Square(self.map,(st_x+i,st_y))
                square.make_open()
                self.map.add_square(square)
                
            
            for j in range(ed_y - st_y):
                square = Square(self.map,(st_x+i,st_y+j))
                square.make_open()
                self.map.add_square(square)
        
        elif st_x == 4 and ed_x == 27:
            
            for i in range((ed_x - st_x)//2+1):
                square = Square(self.map,(st_x+i,st_y))
                square.make_open()
                self.map.add_square(square)
            
            
            for j in range(ed_y - st_y+1):
                square = Square(self.map,(st_x+i,st_y+j))
                square.make_open()
                self.map.add_square(square)
        
            for k in range((ed_x - st_x)//2+1):
                square = Square(self.map,(st_x+i+k,st_y+j))
                square.make_open()
                self.map.add_square(square)
        
        self.map.fill_walls()
        
        return end
    
    def get_map(self):
        
        return self.map
    
    def get_player(self):
        
        return self.player
    
    def update(self,dt):
        
        death = self.map.update(dt)
        
        return death

class Map:
    
    def __init__(self, seed = 0):
        
        self.seed = seed
        
        self.squares = []
        self.rooms = []
        
        self.board = gameview.Board()
        
        self.occupants = []
        
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
    
    def get_square(self,pos):
        """ Searches map for a square at a given position. """
        
        if type(pos) == int:
            return self.squares[pos]
        else:
            for square in self.squares:
                if square.get_position() == pos:
                    return square
        
        return None
    
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

    def view(self,scale=1):
        
        for square in self.squares:
            position = square.get_position()
            picture = square.view(square,scale)
            self.board.draw_object(picture,position,scale)
            
        map = self.board.view()
        
        return map
        
class Room:
    
    def __init__(self,id):
        
        self.id = id
        self.center = None
        
        self.members = []
    
    def __str__(self):
        
        return str(self.id)
    
    def set_center(self,square):
        
        self.center = square
        
    def get_center(self):
        
        return self.center
    
    def get_squares(self):
        
        return self.members
    
    def add_square(self,square):
        
        if not square in self.members:
            self.members.append(square)
        
    def get_random(self):
        """ Returns a random tile from the room. """
        ## Warning: don't know if extra tiles yet.
        ## Need to correct for overwrites and deletions. 
        
        if self.members:
            return random.choice(self.members)
        
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
        
        self.set_viewer(gameview.filled_square)
    
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
        
        return tuple(self.neighbors)
    
        
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

class Dude:
    
    def __init__(self,square = None):
        
        self.name = None
        
        self.mortal = True
        
        self.ready = False
        
        self.inventory = Inventory(self,26)
        
        self.square = square
        square.set_occupant(self)
        
        
        self.quests = []
        
        self.control = None   ## None - Player , else AI class
        
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
        
        return self.square
    
    def get_inventory(self):
        
        return self.inventory
    
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
        

class AI:
    
    def __init__(self,owner,orders):
        
        self.owner = owner
        
        self.orders = orders
        
    def get_orders(self,knowledge = None):
        
        return self.orders(self.owner,knowledge)
        

def random_walk(owner,knowledge = None):
    
    square = owner.get_square()
    
    target = random.choice(square.get_neighbors())

    return target
    
def stay_put(owner,knowledge = None):
    
    return None
        