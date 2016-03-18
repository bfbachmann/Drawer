import pickle
from Line import *
from GUI import Document


#Define a class that will be our document model
class LineDocument(Document):
    
    lines = None
    
    def new_contents(self):
        self.lines = []
        
    def read_contents(self, file):
        self.lines = pickle.load(file)
        
    def write_contents(self, file):
        pickle.dump(self.lines, file)
        
    def add_line(self, line):
        self.lines.append(line)
        self.changed()
        self.notify_views()
        
    def move_line(self, line, dx, dy):
        line.move(dx, dy)
        self.changed()
        self.notify_views()
    
    def remove_line(self, line):
        self.lines.remove(line)
        self.changed()
        self.notify_views()
        
    def find_line(self, x, y):
        for line in self.lines:
            if line.contains(x, y):
                return line
        return None
    
    def change_line(self, line, x, y):
        for aline in self.lines:
            if aline.equals(line):
                aline.update_coordinates(x, y)
                self.changed()
                self.notify_views()
                return
        
