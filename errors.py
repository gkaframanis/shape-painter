class OutOfCanvasBounds(Exception):
    """Error raised when the shape can't fit into the canvas"""
    def __init__(self, message="The shape you try to draw doesn't fit inside the canvas..."):
        self.message = message
        super().__init__(self.message)
