import pygame
import time
from snake import Snake
from fruit import Fruit
from collisions import Collisions
from sound import Sound

class Game:
    def __init__(self, screen, settings, sound):
        self.screen = screen
        self.settings = settings
        self.sound = sound
        self.sound.play_sound('backgroundMusic')
        self.snake = Snake()
        self.fruit = Fruit(settings.window_x, settings.window_y, settings.block_size)
        self.score = 0
        self.collisions = Collisions(self.snake, self.settings)
        self.last_speed_increase_score = 0   
    
    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            running = self.handle_events()
            self.update()
            self.draw(self.screen)
            pygame.display.flip()
            clock.tick(self.settings.snake_speed)

        self.sound.stop_background_music()
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                self.snake.change_direction(event.key)
        return True
    
    def speed_scaling(self):
        if self.score >= self.last_speed_increase_score + 40:
            if self.settings.snake_speed < 60:  
                self.settings.snake_speed += 3
                self.last_speed_increase_score = self.score
                self.sound.play_sound('speedIncrease')

    def update(self):
        self.snake.move()
        self.fruit.update()
        self.speed_scaling()

        if self.snake.body[0] == self.fruit.position:
            self.snake.grow()
            self.sound.play_sound('consumption')
            self.score += 10
            self.fruit.respawn(snake_body=self.snake.body)

        if self.score % 50 == 0 and self.score > 0 and not self.fruit.blink_fruit_active:
          self.fruit.spawn_blinking_fruit(self.snake.body)

        if self.fruit.blink_fruit_active and self.score % 50 != 0:
          self.fruit.blink_fruit_active = False
          self.fruit.blink_fruit_position = None

        if self.fruit.blink_fruit_active and self.fruit.blink_visible:
          if self.snake.position == self.fruit.blink_fruit_position:
            self.snake.grow()
            self.score += 40
            self.sound.play_sound('ultraconsumption')
            self.fruit.blink_fruit_active = False
            self.fruit.blink_fruit_position = None
          


        if self.fruit.special_active and self.snake.position == self.fruit.special_position:
            self.snake.grow()
            self.sound.play_sound('consumption')
            self.score += 20
            self.fruit.special_active = False
            self.fruit.special_position = None

        if self.score % 30 == 0 and self.score > 0 and not self.fruit.special_active:
            self.fruit.special_fruit_respawn(self.snake.body)

        if self.collisions.is_collision():
            self.game_over()

    def draw(self, screen):
        screen.fill(self.settings.color_background)
        self.fruit.draw(screen)


        for position in self.snake.body:
            pygame.draw.rect(screen, self.settings.color_snake,
                             pygame.Rect(position[0], position[1], self.settings.block_size, self.settings.block_size))


        font = pygame.font.SysFont(self.settings.font_name, self.settings.font_size)
        score_surface = font.render("Score: " + str(self.score), True, self.settings.color_score)
        score_rect = score_surface.get_rect()
        screen.blit(score_surface, score_rect)

    def game_over(self):
      self.sound.stop_background_music()
      self.sound.play_sound('game_over')

      font = pygame.font.SysFont("Times new roman", 50)
      surface = font.render("Final Score: " + str(self.score), True, (255, 255, 255))
      rect = surface.get_rect()
      rect.midtop = (self.settings.window_x / 2, self.settings.window_y / 4)

      screen = pygame.display.get_surface()
      screen.fill((0, 0, 0))  
      screen.blit(surface, rect)
      pygame.display.flip()

      pygame.time.delay(2000)  
      pygame.quit()
      quit()
