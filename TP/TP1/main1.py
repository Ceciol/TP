import pygame
import os

class PygameGame(object):
    def initColor(self):
        self.grey = (184,184,173)
        self.purple = (129,132,179)
        self.orange = (231,159,114)
        self.lightGrey = (214,214,204)
    
    def initImg(self):
        self.bgImg = pygame.image.load('image/bg.png')
        self.setImg = pygame.image.load('image/set.png')
        self.quitImg = pygame.image.load('image/quit.png')
        

#############################
#all button
#############################
def mainbuttons(self):
    r = 50
    w2 = 300
    h2 = 50
    self.settingBtn = [530,20,r,self.lightGrey]
    self.quitBtn = [530,530,r,self.lightGrey]
    self.mainBtn1=[70,150,w2,h2,self.lightGrey]
    self.mainBtn2=[70,250,w2,h2,self.lightGrey]
    self.mainBtn3=[70,350,w2,h2,self.lightGrey]

#########################
### Main Framework ######
#########################

    def init(self):
        self.initColor()
        self.initImg()
        self.mode = "main"
        self.modeLst = ["main","settings","game","gamePause","gameOver","instructions"]
        
    
    #### MousePressed ####
    def mousePressed(self,x,y):
        pass
        
#### MouseReleased ####
    def mousePressed(self,x,y):
        pass
        
#### MouseMotion ####
    def mouseMotion(self, x, y):
        pass
        
#### timerFried ####
    def timerFired(self, dt):
        pass
        
###########################
#draw
###########################
    def drawSettingBtn(self,screen):
        pygame.draw.circle(screen,self.settingBtn[3],(self.settingBtn[0],self.settingBtn[1]),self.settingBtn[2])
        screen.blit(self.setImg, (self.settingBtn[0],self.settingBtn[1]))
        
    def drawQuitBtn(self,screen):
        pygame.draw.circle(screen,self.quitBtn[3],(selfquitBtn[0],self.quitBtn[1]),self.quitBtn[2])
        screen.blit(self.quitImg, (selfquitBtn[0],self.quitBtn[1]))
    


############### redraw ####
    def redrawMain(self,screen):
        if self.mode == "main":
            screen.blit(self.bgImg,(0,0))
            self.drawSettingBtn(screen)
            self.drawQuitBtn(screen)
            pygame.draw.rect(screen,self.mainBtn1[4],self.mainBtn1[:4])    
            pygame.draw.rect(screen,self.mainBtn2[4],self.mainBtn2[:4])  
            pygame.draw.rect(screen,self.mainBtn3[4],self.mainBtn3[:4])          
        
    def redrawAll(self, screen):
        self.redrawMain(screen)
        
    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)
        
    def __init__(self, width, height, fps=50, title="Arrow"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (231,159,114)

        pygame.init()
        




    def run(self):
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()

        playing = True
        while playing:
            time = clock.tick(self.fps)
            self.timerFired(time)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                    print(event.pos)
                    self.currentPos=event.pos
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                # elif (event.type == pygame.MOUSEMOTION and
                #       event.buttons[0] == 1):
                #     self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False
            screen.fill(self.bgColor)
            self.redrawAll(screen)
            pygame.display.flip()

        pygame.quit()



def main():
    game = PygameGame(600,600)
    game.run()

if __name__ == '__main__':
    main()