# collisions.py
class Collisions:
    def __init__(self, snake, settings):
        self.snake = snake
        self.settings = settings

    def is_collision(self):
        head = self.snake.body[0]  # Get current head of the snake

        # Wall collision
        if head[0] < 0 or head[0] >= self.settings.window_x:
            return True
        if head[1] < 0 or head[1] >= self.settings.window_y:
            return True

        # Self collision
        if head in self.snake.body[1:]:
            return True

        return False
