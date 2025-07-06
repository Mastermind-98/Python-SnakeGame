import pygame
import sys
from userinterface import UserInterface
from settings import Settings
from sound import Sound
from game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((720, 480))
    pygame.display.set_caption("Snake Game")

    ui = UserInterface(screen)
    difficulty = None

    while difficulty is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            result = ui.handle_input(event)
            if result:
                action, data = result
                if action == "start":
                    difficulty = data

        ui.draw()
        pygame.display.flip()

    settings = Settings(difficulty)
    sound = Sound()
    game = Game(screen, settings, sound)
    game.run()

if __name__ == "__main__":
    main()
