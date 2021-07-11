from canvas import Canvas
from errors import OutOfCanvasBounds

class Rectangle:
    """A rectangle shape that can be drawn on a Canvas object"""
    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
    
    def draw(self, canvas):
        """Draws itself into the canvas"""
        # We change a slice of the numpy array with the new values
        if self.x + self.height <= canvas.height + 1:
            canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color
        else:
            raise OutOfCanvasBounds()


class Square(Rectangle):
    """A square shape that inherits from Rectangle class and can be drawn on a Canvas object"""
    def __init__(self, x, y, side, color):
        super().__init__(x, y, side, side, color)


