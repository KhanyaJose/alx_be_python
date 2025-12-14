# class_static_methods_demo.py

class Calculator:
    """
    A class demonstrating the difference between class methods and static methods.
    """
    
    # Class attribute
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        """
        Static method that returns the sum of two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The sum of a and b
        """
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """
        Class method that returns the product of two numbers.
        Also prints the calculation type from the class attribute.
        
        Args:
            cls: Reference to the class itself
            a: First number
            b: Second number
            
        Returns:
            The product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b