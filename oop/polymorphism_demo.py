# polymorphism_demo.py
import math

class Shape:
    """
    Base class representing a geometric shape.
    """
    def area(self):
        """
        Calculates the area of the shape.
        
        Returns:
            float: Area of the shape
            
        Raises:
            NotImplementedError: This method must be overridden in derived classes
        """
        raise NotImplementedError("Subclasses must implement the area() method")


class Rectangle(Shape):
    """
    Derived class representing a rectangle.
    Inherits from Shape class.
    """
    def __init__(self, length, width):
        """
        Initialize a Rectangle instance.
        
        Args:
            length (float): Length of the rectangle
            width (float): Width of the rectangle
        """
        self.length = length
        self.width = width
    
    def area(self):
        """
        Calculates the area of the rectangle.
        Overrides the area() method from Shape class.
        
        Returns:
            float: Area of the rectangle (length × width)
        """
        return self.length * self.width


class Circle(Shape):
    """
    Derived class representing a circle.
    Inherits from Shape class.
    """
    def __init__(self, radius):
        """
        Initialize a Circle instance.
        
        Args:
            radius (float): Radius of the circle
        """
        self.radius = radius
    
    def area(self):
        """
        Calculates the area of the circle.
        Overrides the area() method from Shape class.
        
        Returns:
            float: Area of the circle (π × radius²)
        """
        return math.pi * (self.radius ** 2)