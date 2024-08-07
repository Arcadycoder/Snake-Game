import pygame
from pygame.locals import *
import random
import time

SIZE = 20
class Apple:
    def __init__(self, parent_screen):
        self.image = pygame.transform.scale(pygame.image.load("E:/Python/Python Projects/Snake/Resources/apple.jpg").convert(),(SIZE,SIZE))
        self.parent_screen = parent_screen
        self.x = SIZE*3
        self.y = SIZE*3

    def draw(self):
        self.parent_screen.blit(self.image,(self.x,self.y))

    def move(self):
        self.x = random.randint(0,34)*SIZE
        self.y = random.randint(0,34)*SIZE


class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.transform.scale(pygame.image.load("E:/Python/Python Projects/Snake/Resources/block.jpg").convert(),(SIZE,SIZE))
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        self.direction = 'down'

    def walk(self):

        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == 'up':
            self.y[0] -= SIZE

        if self.direction == 'down':
            self.y[0] += SIZE

        if self.direction == 'left':
            self.x[0] -= SIZE

        if self.direction == 'right':
            self.x[0] += SIZE

        self.draw_block()

    def draw_block(self):
        self.parent_screen.fill((110, 110, 5))
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i], self.y[i]))


    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'


    def increase_length(self):
        self.length+=1
        self.x.append(-1)
        self.y.append(-1)

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((700, 700))
        self.snake = Snake(self.surface, 3)
        self.snake.draw_block()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.update()

        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()

        for i in range(1, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                print("Game over")

    def display_score(self):
        font = pygame.font.SysFont('corbel', 30)
        score = font.render(f"Score:{self.snake.length-3}", True, (255,255,255))
        self.surface.blit(score,(600,10))

    def run(self):

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_w or event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_s or event.key == K_DOWN:
                        self.snake.move_down()

                    if event.key == K_a or event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_d or event.key == K_RIGHT:
                        self.snake.move_right()

                elif event.type == QUIT:
                    running = False

            self.play()
            time.sleep(.10)



if __name__ == "__main__":
    game = Game()
    game.run()