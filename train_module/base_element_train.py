"""
Based train module
version: v1.0
author: benjo

"""
import sys, pygame
from pygame.locals import*

direction = 'left'
WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)

"""
    desc: draw a fixed position train
    param(): 
        screen: obj
        length: train length
        x: train coordinate x
        y: train coordinate y

"""

class Train():
    def __init__(self, coordinate, length, direction):
        self.train_high = 30
        self.train_min_length = 160
        self.wheel_radius = 7
        
        self.color = pygam.Color(0, 245, 255)
        self.


def draw_base_train(screen, length, x, y):
    #rect = pygame.Rect(x, y, length, 5)
    color = pygame.Color(0, 245, 255)
    rect = pygame.Rect(x, y, length, 30)
    triangle = [[0, 0], [0, 29], [29, 29]]

    x_offset = x + length
    y_offset = y
    for i in range(len(triangle)):
        #print('triangle[%d] is %d %d' % (i, triangle[i][0], triangle[i][1]))
        triangle[i][0] += x_offset
        triangle[i][1] += y_offset
    pygame.draw.rect(screen, color, rect)
    pygame.draw.polygon(screen, color, triangle)
    
    










def main():
    pygame.init()
    screen = pygame.display.set_mode((1280,720))
    pygame.display.set_caption('train test')
    clock = pygame.time.Clock()

    coordinate_x = 200
    coordinate_y = 200
    train_length = 200
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)
        if direction=="right":
            if (coordinate_x + train_length) < 1200:
                coordinate_x += 1
        elif direction == 'left':
            if (coordinate_x > 0):
                coordinate_x -= 1
        draw_base_train(screen, train_length, coordinate_x, coordinate_y)
        pygame.display.update()
        clock.tick(90)



if __name__ == '__main__' :
    main()