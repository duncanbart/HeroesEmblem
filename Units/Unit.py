import sys, pygame, os
from pygame.locals import *

class Unit(pygame.sprite.Sprite):
    dist = 31
    
    def __init__(self, art, x , y, movement, health, attack, minimumRange, maximumRange, team):
        pygame.sprite.Sprite.__init__(self)
        self.dist = Unit.dist
        
        self.movement = movement
        self.temp_movement = movement
        self.x = x * self.dist
        self.y = y * self.dist
        self.minimumRange = minimumRange
        self.maximumRange = maximumRange
        self.team = team
        self.tapped = False

        self.image = pygame.image.load(art)
        self.art = art
        self.rect = self.image.get_rect()


    def draw(self, surface, animationState, tapped):
        imageAttributes = self.art.split("-")
        imageAttributes[2] = str(animationState)
        self.image = pygame.image.load("-".join(imageAttributes))

        if(tapped):
            self.image.fill((255, 255, 255, 128), None, pygame.BLEND_RGBA_MULT)

        surface.blit(self.image, (self.x, self.y))
    
    def movement_clac(self):
        self.temp_movement -= 1

    def reset_movement(self):
        self.temp_movement = self.movement

    def get_location(self):
        current_space = (self.x/self.dist, self.y/self.dist)
        return current_space

    def get_team(self):
        return self.team

    def get_movement(self):
        return self.movement

    def get_minimumRange(self):
        return self.minimumRange

    def get_maximumRange(self):
        return self.maximumRange

    def tap(self):
        self.tapped = True

    def untap(self):
        self.tapped = False

