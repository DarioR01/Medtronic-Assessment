class ImageSample:
    x: int
    y: int
    width: int
    height: int

    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move(self, dx: int, dy: int):
        self.x += dx
        self.y += dy

    def get_bounds(self):
        return self.x, self.y, self.x + self.width, self.y + self.height
