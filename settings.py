class Settings:
    def __init__(self, difficulty):
        if difficulty == "easy":
            self.snake_speed = 15
            self.block_size = 13
            self.color_background = (0, 33, 71)
            self.color_snake = (255, 179, 0)
            self.color_fruit = (255, 255, 255)
            self.color_score = (255, 179, 0)
        elif difficulty == "medium":
            self.snake_speed = 20
            self.block_size = 10
            self.color_background = (2, 48, 32)
            self.color_snake = (94, 44, 4)
            self.color_fruit = (255, 255, 255)
            self.color_score = (94, 44, 4)
        elif difficulty == "hard":
            self.snake_speed = 25
            self.block_size = 8
            self.color_background = (0, 0, 0)
            self.color_snake = (255, 255, 255)
            self.color_fruit = (255, 255, 255)
            self.color_score = (255, 255, 255)

        self.font_name = "Georgia"
        self.font_size = 25
        self.window_x = 720
        self.window_y = 480

        self.window_x = 720
        self.window_y = 480