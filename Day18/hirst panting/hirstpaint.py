import colorgram
import turtle as t
import random

def extract_colors(image_path, num_colors):
    # Extract a specified number of colors from an image.
    
    # Args:
    #     image_path (str): The path to the image file.
    #     num_colors (int): The number of colors to extract.
        
    # Returns:
    #     list: A list of tuples representing RGB values of the extracted colors.
    
    colors = colorgram.extract("G:\Python Practices\PythonZero to Master\Day18\hirst panting\HirstPainting.jpg", 50)
    return [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

def create_painting(colors, rows=10, cols=10, dot_size=20, spacing=50):
    """Create a painting of dots using the turtle module.
    
    Args:
        colors (list): A list of tuples representing RGB values.
        rows (int): Number of rows of dots.
        cols (int): Number of columns of dots.
        dot_size (int): The diameter of each dot.
        spacing (int): The distance between each dot.
    """
    t.colormode(255)
    painter = t.Turtle()
    painter.penup()
    painter.hideturtle()
    painter.speed("fastest")
    
    start_x, start_y = -250, -250
    painter.setpos(start_x, start_y)
    
    for row in range(rows):
        for col in range(cols):
            painter.dot(dot_size, random.choice(colors))
            painter.forward(spacing)
        painter.setpos(start_x, painter.ycor() + spacing)

def main():
    """Main function to extract colors and create a painting using turtle."""
    image_path = "hirst.jpeg"
    num_colors = 20
    colors = extract_colors("G:\Python Practices\PythonZero to Master\Day18\hirst panting\HirstPainting.jpg", 50)
    
    create_painting(colors)
    
    screen = t.Screen()
    screen.exitonclick()

if __name__ == "__main__":
    main()