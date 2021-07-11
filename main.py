from shapes import Square, Rectangle
from canvas import Canvas
from errors import OutOfCanvasBounds

if __name__ == '__main__':
    # Get the height (rows) and the width (columns) of the canvas from the user:
    canvas_height = int(input("Enter the canvas height: "))
    canvas_width = int(input("Enter the canvas width: "))

    # Make a dictionary of color codes and prompt for the color that the canvas will have
    colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
    canvas_color = input("Enter the canvas color (white or black): ")

    # Create the canvas based on the user's input
    canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])


    while True:
        shape_type = input("What shape do you like to draw? Square of Rectangle? Enter quit to quit. ")

        # Ask for the rectangle data and create the rectangle if the user entered "rectangle"
        if shape_type.lower() == "rectangle":
            rect_x = int(input("Enter the row where the rectangle starts: "))
            rect_y = int(input("Enter the column where the rectangle starts: "))
            rect_height = int(input("Enter the height of the rectangle: "))
            rect_width = int(input("Enter the width of the rectangle: "))
            red = int(input("How much red should the rectangle color have? "))
            green = int(input("How much green should the rectangle color have? "))
            blue = int(input("How much blue should the rectangle color have? "))

            # Create the rectangle based on the above user values
            rectangle = Rectangle(x=rect_x, y=rect_y, height=rect_height, width=rect_width, color=(red, green, blue))
            rectangle.draw(canvas)


        # Ask for the square data and create the square if the user entered "square"
        if shape_type.lower() == "square":
            rect_x = int(input("Enter the row where the square starts: "))
            rect_y = int(input("Enter the column where the square starts: "))
            rect_side = int(input("Enter the side of the square: "))
            red = int(input("How much red should the square color have? "))
            green = int(input("How much green should the square color have? "))
            blue = int(input("How much blue should the square color have? "))

            # Create the square based on the above user values
            square = Square(x=rect_x, y=rect_y, side=rect_side, color=(red, green, blue))
            try:
                square.draw(canvas)
            except OutOfCanvasBounds as err:
                print(err)
            finally:
                continue

        if shape_type.lower() == "quit":
            print("You are exiting the program...")
            break

canvas.make("canvas.png")
