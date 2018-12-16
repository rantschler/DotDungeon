
import gameclass as gc
import pygame as pg
from pygame.locals import *
from sys import exit

class Controller:

    def __init__(self):
        
        self.screen = None
        self.buttons = []
        self.player = None
    
    def subscribe_to(self,player):
        
        self.player = player

    def add_button(self,button):
        
        self.buttons.append(button)
        
    
    def get_buttons(self):
        
        return tuple(self.buttons)
    
    
    def resolve(self,interval):
        
        events = pg.event.get()
        for event in events:
            if event.type == QUIT:
                exit()
            if event.type == VIDEORESIZE:
                self.size = tuple(event.size)
                self.resize()
            if self.screen:
                if event.type == pg.KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.screen = None
            elif self.player:
                if event.type == pg.KEYDOWN:
                    if event.key == K_KP1:
                        prospect = self.player.get_prospect(1)
                        self.player.move_into(prospect)
                    if event.key == K_KP2:
                        prospect = self.player.get_prospect(2)
                        self.player.move_into(prospect)
                    if event.key == K_KP3:
                        prospect = self.player.get_prospect(3)
                        self.player.move_into(prospect)
                    if event.key == K_KP4:
                        prospect = self.player.get_prospect(4)
                        self.player.move_into(prospect)
                    if event.key == K_KP6:
                        prospect = self.player.get_prospect(6)
                        self.player.move_into(prospect)
                    if event.key == K_KP7:
                        prospect = self.player.get_prospect(7)
                        self.player.move_into(prospect)
                    if event.key == K_KP8:
                        prospect = self.player.get_prospect(8)
                        self.player.move_into(prospect)
                    if event.key == K_KP9:
                        prospect = self.player.get_prospect(9)
                        self.player.move_into(prospect)
                    if event.key == K_i:
                        self.player.get_inventory().print_inventory()
                        
            else: 
                
                pass
                