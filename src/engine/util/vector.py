class Vec2(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __mul__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x*other.x, self.y*other.y)
        else:
            return Vec2(other*self.x, other*self.y)
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __add__(self, other):
        return Vec2(self.x+other.x, self.y+other.y)
    def __radd__(self, other):
        return self.__add__(other)
    
    def toTuple(self):
        return (self.x, self.y)
    
    def __str__(self):
        return str(self.toTuple())