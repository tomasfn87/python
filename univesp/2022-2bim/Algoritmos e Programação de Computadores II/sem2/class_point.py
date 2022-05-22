class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def setx(self, x):
        self.x = x 
        
    def sety(self, y):
        self.y = y
        
    def get(self):
        return self.x, self.y
    
    def move(self, offsetx, offsety):
        self.x += offsetx
        self.y += offsety
        
    def __repr__(self):
        return f'(X={self.x}, Y={self.y})'
    
    def __add__(self, other):
        if type(other) == Point:
            return Point(self.x + other.x, self.y + other.y)
        else:
            return Point(self.x + other, self.y + other)
        
    def __sub__(self, other):
        if type(other) == Point:
            return Point(self.x - other.x, self.y - other.y)
        else:
            return Point(self.x - other, self.y - other)

p = Point(10, 5)
p.x = p.x * 2
p.y = p.y * 3
print(p)

p +=  Point(3, 3)
print(p)

p += 2
print(p)

p -= Point(1, 1)
print(p)

p -= 10
print(p)

