from rectangle import Rectangle

class Square(Rectangle):
    """A class named Sqaure that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """
         Instantiates a class

         Args:
              size (int): size of the square
              x (int): 
              y (int): 
              id: id of the instance
        """
        self.size = size
        super().__init__(size, size, x, y, id)
        """
           Calling the super class with id, x, y, width, height with width and height set to size
        """
        
    @property
    def size(self):
        return self.height
    @size.setter
    def size(self, value):
        """Validating the size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if not args:
            for key, value in kwargs.items():
                setattr(self, key, value)
        if len(args) == 1:
            self.id = args[0]
        elif len(args) == 2:
            self.id = args[0]
            self.size = args[1]
        elif len(args) == 3:
            self.id = args[0]
            self.size = args[1]
        elif len(args) == 4:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]

    def __str__(self):
            return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
    
    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }