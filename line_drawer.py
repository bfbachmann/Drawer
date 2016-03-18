from LineDocument import *
from LineView  import *
from GUI import Application, Window, Cursor
from GUI.Files import FileType



#Define an application class that inherits Application
class LineDrawerApp(Application):
        
    #initialize the app
    def __init__(self):
        Application.__init__(self)
        
        #define a file type for the app's files
        #this allows us to the app to recognize the files it can open
        self.file_type = FileType(name = 'Line Document', suffix = 'ln')
        
        #we can create new cursors to use in our views
        self.line_cursor = Cursor("crosshair.tiff")
        
    #Overrides its super's same function
    #tells the application what to do when it is first opened    
    def open_app(self):
        #tell the application to open a new document
        self.new_cmd()
        
    #tell the app how to make a new Document object of the kind we want
    #fileref is a reference to an existing file, this parameter is 
    #None when a new document is first created 
    #Returns an instance of the Document class
    def make_document(self, fileref):
        return LineDocument()
    
    #tell our app how to create a window
    def make_window(self, document):
        
        window_width = 800
        window_height = 600
        
        #create a Window object and associate it with our document 
        #so when the window is closed the doc can ask the user if
        #he wants to save
        app_window = Window(size = (window_width, window_height), document = document)
        
        #make a view for the window
        app_view = LineView(model = document, extent = (window_width, window_height), printable = False, cursor = self.line_cursor)
        
        #place the view in the window, make it resizeable
        app_window.place(app_view, left = 0, top = 0, right = 0, bottom = 0, sticky = 'nsew')
        
        #display the window when we are done initializing
        app_window.show()
        
        
        
LineDrawerApp().run()
    
    
    
    
    
    