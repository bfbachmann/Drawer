import math

class Line(object):
    
    def __init__(self, x0, y0):
        self.line = (x0, y0, x0, y0)
        
    def copy(self, line):
        self.line = (line.line[0], line.line[1], line.line[2], line.line[3])
    
    def equals(self, aline):
        if self.line == aline.line:
            return True
        return False
    
    def update_coordinates(self, x, y):
        self.line = (self.line[0], self.line[1], x, y)
        
    def move(self, dx, dy):
        self.line = (self.line[0] + dx, self.line[1] + dy, self.line[2] + dx, self.line[3] + dy)
        
    def contains(self, x, y):
        xmax = max(self.line[0], self.line[2])
        xmin = min(self.line[0], self.line[2])
        ymax = max(self.line[1], self.line[3])
        ymin = min(self.line[1], self.line[3])
        
        if ymax - ymin < 4 and x < xmax and x > xmin:
                return self.shortest_distance(x, y) < 9
        elif xmax - xmin < 4 and y < ymax and y > ymin:
                return self.shortest_distance(x, y) < 9
        elif x >= xmin and x <= xmax and y >= ymin and y <= ymax:
            return self.shortest_distance(x, y) < 5
        return False
    
    def draw(self, canvas):
        x0, y0, x1, y1 = self.line
        canvas.newpath()
        canvas.moveto(x0, y0)
        canvas.lineto(x1, y1)
        canvas.stroke()
        
    def get_slope(self):
        try:
            slope = (self.line[3] - self.line[1])/(self.line[2] - self.line[0])
        except ZeroDivisionError:
            return None
        return slope
    
    def shortest_distance(self, x, y):
        slope = self.get_slope()
        if not slope: return self.line[0]-x
        a = slope
        b = -1
        c = self.line[1] - slope*self.line[0]
        return abs(a*x + b*y + c)/math.sqrt(a**2 + 1)
 