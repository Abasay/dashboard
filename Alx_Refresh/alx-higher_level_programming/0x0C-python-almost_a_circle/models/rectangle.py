from base import Base

class Rectangle(Base):
    """Class Rectangle that inherits from the base class"""
    

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Instantiate a class

        
            Args:
                width (int): This is the width of the rectagle
                height (int): This is the height of the rectangle
                x (int): x axis
                y (int): y axis

            Raises:
                TypeError: If ay of the args is not an instance of an integer
                ValueError (width or height): If width or height is under or equals 0
                ValueError (x or y): If x or y is under 0
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)
        """Calling the super class (Base) with id"""

    @property
    def width(self):
        """sets/gets the width"""

        return self.__width
    @width.setter
    def width(self, value):
        """Validating the width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0") 
        self.__width = value

    
    @property
    def height(self):
        """sets/gets the height"""
        return self.__height
    @height.setter
    def height(self, value):
        """validating the height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0") 
        self.__height = value

    
    @property
    def x(self):
        """sets/gets the value of x"""
        return self.__x
    @x.setter
    def x(self, value):
        """validating the value of x"""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0") 
        self.__x = value
    @property
    def y(self):
        """sets/gets y"""

        return self.__y
    @y.setter
    def y(self, value):
        """validating y"""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0") 
        self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """
            prints in stdout the Rectangle instance with the character # while x signifies the number of space before printing the # and y prints a new line
        """

        [print() for i in range(0, self.__y)]
        
        for a in range(0, self.__height):
            [print(" ", end="") for j in range(0, self.__x)]
            [print("#", end="") for b in range(0, self.__width)]
            print()
    
    def update(self, *args, **kwargs):
        """
                function that assigns an argument to each attribute

                args: no-keyword argument
                kwargs: keyword argument, omitt this when args is present
        """
        if not args:
            for key, value in kwargs.items():
                setattr(self, key, value)
        if len(args) == 1:
            self.id = args[0]
        elif len(args) == 2:
            self.id = args[0]
            self.__width = args[1]
        elif len(args) == 3:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
        elif len(args) == 4:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
        elif len(args) == 5:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]

    def __str__(self):
        """rewritting the __str__ function"""
        return f"{[__class__.__name__]} ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
    
    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }
    
    
    

