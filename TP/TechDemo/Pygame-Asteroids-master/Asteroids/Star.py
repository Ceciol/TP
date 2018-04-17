import pygame 
from GameObject import GameObject

class Star(GameObject):
        
    def __init__(self,x,y):
        self.image = pygame.transform.rotate(pygame.transform.scale(
            pygame.image.load('images/star.png').convert_alpha(),
            (100, 100)), 0)
        self.x = x
        self.y = y
        super(Star, self).__init__(self.x,self.y, self.image, 10)
    
    def update(self):
        for events in pygame.event.get(): #look at all events
            if events.type == pygame.MOUSEMOTION:
                mouse_position = pygame.mouse.get_pos()
                self.x = mouse_position[0]
                self.y = mouse_position[1]
                super(Star, self).__init__(self.x,self.y, self.image, 1)

        