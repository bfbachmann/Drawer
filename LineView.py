from LineDocument import *
from Line import *
from GUI import Cursor, rgb, ScrollableView
from GUI.Geometry import pt_in_rect, offset_rect, rects_intersect
from GUI.StdColors import black, red


#Define the view with the following responsibilities:
#   1. Display the data contained in the Document
#   2. Handle user actions
class LineView(ScrollableView):
    
    cursors = {'eraser': Cursor("eraser.tiff"), 'crosshair': Cursor("crosshair.tiff"), 'fist': Cursor("fist.tiff")}
    
    def draw(self, canvas, update_rect):
        canvas.erase_rect(update_rect)
        canvas.fillcolor = red
        canvas.pencolor = black
        for line in self.model.lines:
            line.draw(canvas)
            
    def mouse_down(self, event):
        
        x, y = event.position
        line = self.model.find_line(x, y)
        
        if event.button is 'right':
            self.delete_lines()
        elif event.control:
            if line:
                self.drag_line(line, x, y)
        elif event.shift:
            if line:
                self.copy_line(line, x, y)
        else:
            self.draw_line(x, y)
            
    def copy_line(self, line, x, y):
        new_line = Line(x, y)
        new_line.copy(line)
        self.model.add_line(new_line)
        self.drag_line(new_line, x, y)
            
    def delete_lines(self):
        self.cursor = self.cursors['eraser']
        for event in self.track_mouse():
            x, y = event.position
            line = self.model.find_line(x, y)
            if line:
                self.model.remove_line(line)
        self.cursor = self.cursors['crosshair']
            
    def drag_line(self, line, x0, y0):
        self.cursor = self.cursors['fist']
        for event in self.track_mouse():
            x, y = event.position
            self.model.move_line(line, x - x0, y - y0)
            x0 = x
            y0 = y
        self.cursor = self.cursors['crosshair']
            
    def draw_line(self, x0, y0):
        line = Line(x0, y0)
        self.model.add_line(line)
        for event in self.track_mouse():
            x, y = event.position
            self.model.change_line(line, x, y)
    
    def line_changed(self, model, line):
        self.invalidate_rect(line.line) 