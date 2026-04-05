class Smoother:
    def __init__(self, factor=5):
        self.factor = factor
        self.prev_x = 0
        self.prev_y = 0

    def smooth(self, x, y):
        smooth_x = self.prev_x + (x - self.prev_x) / self.factor
        smooth_y = self.prev_y + (y - self.prev_y) / self.factor

        self.prev_x = smooth_x
        self.prev_y = smooth_y

        return int(smooth_x), int(smooth_y)