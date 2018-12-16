#6
# Project Title: 
#
# Author:  
#

#
# PACKAGES
#

import gamemodel,gameview,gamecontrol
import pygame as pg


#
# CLASSES
#66

class Main:
    
    def __init__(self):
        
        self.size = (1280,720)
        
        self.screen = gameview.Viewer(self.size)
        self.control = gamecontrol.Controller()
        self.game = True
        self.model = None
        
        self.clock = pg.time.Clock()
    
    def run(self):
        
        while True:
            #
            # Update the time at the beginning of the loop.
            #
        
            interval = float(self.clock.tick(30))/1000.0
            
            #
            #     Model: All game mechanics
            ## Send physics problems to the engine.
            ## Resolve other mechanics (scoring, etc) here or in
            ## other functions
            #
            
            
            
            if self.model:
                """ Play the game. """
                if self.model.player.ready:
                    death = self.model.update(interval)
                    if self.model.player == death:
                        self.game = False
                    self.model.player.ready = False
            
            elif not self.game:
                
                pass
            
            else:
                """ Choose game options. """
                
                # 
                # self.screen subsribes to map and player
                # self.control subscribes to player66
                #
                
                self.model = gamemodel.Model()
                
                self.screen.subscribe_to_map(self.model.get_map())
                self.screen.subscribe_to_player(self.model.get_player())
                self.control.subscribe_to(self.model.get_player())
        
                
            #
            # View: Draw all objects
            ## Send objects to the view function.
            #
            
            self.screen.update(interval)
            self.screen.view()
        
            #
            # Control: Take input from the user.
            ## Provide control of game state in the event loop.
            ## Call the control() function to control the avatar.
            #
        
            if self.game:
                self.control.resolve(interval)


pg.init()
main = Main()
main.run()


