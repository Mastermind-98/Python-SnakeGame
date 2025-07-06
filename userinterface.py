import pygame

class UserInterface:
    def __init__(self, screen):
        self.screen = screen
        self.options = ["easy", "medium", "hard"]
        self.selected_index = 0
        self.font = pygame.font.SysFont("Times New Roman", 40)
        self.instruction_font = pygame.font.SysFont("Times New Roman", 24)
        self.colors = {
            "blue": (0, 0, 255),
            "gold": (255, 179, 0),
            "white": (255, 255, 255)
        }

    def draw(self):
        self.screen.fill(self.colors["blue"])
        pygame.draw.rect(self.screen, self.colors["gold"], (0, 0, 720, 480), 15)

        title_surf = self.font.render("Python SnakeGame", True, self.colors["gold"])
        title_rect = title_surf.get_rect(center=(360, 50))
        self.screen.blit(title_surf, title_rect)

        for i, option in enumerate(self.options):
            color = self.colors["gold"] if i == self.selected_index else self.colors["white"]
            option_surf = self.font.render(option, True, color)
            option_rect = option_surf.get_rect(center=(360, 130 + i * 60))
            self.screen.blit(option_surf, option_rect)

        instructions = [
            "Use UP / DOWN arrow keys to select difficulty",
            "Press ENTER to start",
            "Use ARROW KEYS to control the snake",
        ]
        for i, line in enumerate(instructions):
            line_surf = self.instruction_font.render(line, True, self.colors["white"])
            line_rect = line_surf.get_rect(center=(360, 350 + i * 30))
            self.screen.blit(line_surf, line_rect)

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_index = (self.selected_index - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected_index = (self.selected_index + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                chosen = self.options[self.selected_index]
                print("difficulty selected:", chosen)
                return "start", chosen
        return None
