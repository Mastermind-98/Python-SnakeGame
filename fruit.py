import random
import time
import pygame
class Fruit:
    def __init__(self, window_x, window_y, block_size):
        self.window_x = window_x
        self.window_y = window_y
        self.blink_fruit_position = None
        self.blink_fruit_active = False
        self.blink_fruit_spawn_time = 0
        self.last_blink_toggle = 0
        self.blink_visible = True
        self.blink_interval = 0.5
        self.block_size = block_size
        self.position = [random.randrange(1, (window_x // 10)) * 10,
                         random.randrange(1, (window_y // 10)) * 10]
        self.spawn = True
        self.special_active = False

    def spawn_blinking_fruit(self, snake_body):
        while True:
            pos = [random.randrange(1, (self.window_x // 10)) * 10,
                   random.randrange(1, (self.window_y // 10)) * 10]
            if pos not in snake_body:
                self.blink_fruit_position = pos
                self.blink_fruit_active = True
                self.blink_fruit_spawn_time = time.time()
                self.last_blink_toggle = time.time()
                self.blink_visible = True
                break


    def respawn(self, snake_body):
      while True:
        x = random.randrange(1, (self.window_x // 10)) * 10
        y = random.randrange(1, (self.window_y // 10)) * 10
        if [x, y] not in snake_body:  
            self.position = [x, y]    
            break                     

    def special_fruit_respawn(self, snake_body):
      while True:
        new_position = [random.randrange(1, (self.window_x // 10)) * 10,
                        random.randrange(1, (self.window_y // 10)) * 10]
        if new_position not in snake_body:
            self.special_position = new_position
            self.special_spawn_time = time.time()
            self.special_active = True
            break


    def update(self):
      current_time = time.time()
      if self.special_active and time.time() - self.special_spawn_time > 3:
        self.special_active = False
        self.special_position = None
        self.special_spawn_time = None
      elif current_time - self.last_blink_toggle > self.blink_interval:
            self.blink_visible = not self.blink_visible
            self.last_blink_toggle = current_time


    def draw(self, screen):
      pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(
        self.position[0], self.position[1], self.block_size, self.block_size
    ))

      if self.special_active and self.special_position:
        pygame.draw.rect(screen, (94, 44, 4), pygame.Rect(
            self.special_position[0], self.special_position[1], self.block_size, self.block_size
        ))
      if self.blink_fruit_active and self.blink_visible and self.blink_fruit_position:
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(
                self.blink_fruit_position[0],
                self.blink_fruit_position[1],
                self.block_size,
                self.block_size
            ))


      
    