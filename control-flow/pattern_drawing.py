#!/usr/bin/env python3
"""
Drawing Patterns with Nested Loops
This script draws a square pattern of asterisks using nested loops.
"""

def main():
    # Prompt user for pattern size
    try:
        size = int(input("Enter the size of the pattern: "))
        
        # Validate that the size is positive
        if size <= 0:
            print("Error: Please enter a positive integer.")
            return
            
    except ValueError:
        print("Error: Please enter a valid positive integer.")
        return
    
    # Draw the pattern using nested loops
    row = 0
    while row < size:
        # Use for loop to print asterisks in the current row
        for col in range(size):
            print("*", end="")
        
        # Move to the next line after completing the row
        print()
        row += 1

if __name__ == "__main__":
    main()