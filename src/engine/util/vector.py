class Vec2(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __mul__(self, other):
        return Vec2(self.x*other.x, self.y*other.y)
    
    def toTuple(self):
        return (self.x, self.y)
    
    def __str__(self):
        return str(self.toTuple())