import pygame

class Snake:
    def __init__(self):
        self.body = [
            [100, 50],
            [90, 50],
            [80, 50],
            [70, 50]
        ]
        self.direction = "RIGHT"
        self.change_to = self.direction
        self.position = list(self.body[0])

    def change_direction(self, key):
        if key == pygame.K_UP and self.direction != "DOWN":
            self.change_to = "UP"
        elif key == pygame.K_DOWN and self.direction != "UP":
            self.change_to = "DOWN"
        elif key == pygame.K_LEFT and self.direction != "RIGHT":
            self.change_to = "LEFT"
        elif key == pygame.K_RIGHT and self.direction != "LEFT":
            self.change_to = "RIGHT"

    def move(self, grow=False):
        if self.change_to == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        elif self.change_to == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"
        elif self.change_to == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif self.change_to == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"

        head_x, head_y = self.body[0]

        if self.direction == "UP":
            head_y -= 10
        elif self.direction == "DOWN":
            head_y += 10
        elif self.direction == "LEFT":
            head_x -= 10
        elif self.direction == "RIGHT":
            head_x += 10

        new_head = [head_x, head_y]
        self.body.insert(0, new_head)

        if not grow:
            self.body.pop()

        self.position = list(self.body[0])

    def grow(self):
        self.move(grow=True)
