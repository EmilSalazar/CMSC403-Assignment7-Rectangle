# Emil Baez Salazar

import tkinter as tk
import sys
from rectpack import newPacker


class CustomCanvas:  # create canvas
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, height=self.height, width=self.width)
        self.canvas.pack()

    def draw_rectangle(self, rect, color='purple'):  # 2nd favorite color (since I can't use black)
        # Draw rectangle on canvas using coordinates
        self.canvas.create_rectangle(rect[0],
                                     rect[1],
                                     rect[0] +
                                     rect[2],
                                     rect[1] +
                                     rect[3],
                                     outline='black',
                                     fill=color)

    def show(self):
        self.root.mainloop()  # start loop to display the canvas


class Rectangle:  # class to define a rectangle
    def __init__(self, height, width, x=0, y=0):  # x & y origin point
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    def __repr__(self):
        # print rect details
        return f"Rectangle({self.height}, {self.width}, {self.x}, {self.y})"


# Function to pack rectangles on canvas using rectpack
def pack(rectangles, canvas_size):
    packer = newPacker()

    for r in rectangles:  # Add rect to packer for processing
        packer.add_rect(r.height, r.width)

    packer.add_bin(*canvas_size)  # Add bin to packer for canvas size
    packer.pack()  # Start the packing process

    # Get the packed rectangles
    packed_rectangles = []
    for abin in packer:
        for rect in abin:
            if rect.x + rect.width <= canvas_size[1] and rect.y + rect.height <= canvas_size[0]:
                # If rectangle fits create instance with position and size
                packed_rectangles.append(Rectangle(rect.height, rect.width, rect.x, rect.y))
            else:
                # If rectangle don't fit print warning
                print(f"Warning: Rectangle at index {len(packed_rectangles)} is partly off the canvas and will not be drawn.")

    return packed_rectangles


def main():
    if len(sys.argv) < 2:
        # If no input print message
        print("Usage: python script.py <filepath>")
        return

    filepath = sys.argv[1]  # has input file
    with open(filepath, 'r') as file:
        lines = file.readlines()
        # Extract the canvas height and width from input file
        canvas_height, canvas_width = map(int, lines[0].strip().split(','))

    # make list of Rectangles based on file input
    rectangles = [Rectangle(int(line.split(',')[0]), int(line.split(',')[1])) for line in lines[1:]]

    # initialize CustomCanvas function
    canvas = CustomCanvas(canvas_height, canvas_width)

    # pack rectangles and draw them on the canvas
    packed_rectangles = pack(rectangles, (canvas_height, canvas_width))
    for rect in packed_rectangles:
        canvas.draw_rectangle((rect.x, rect.y, rect.width, rect.height), 'purple')

    canvas.show()  # Display the canvas


if __name__ == "__main__":
    main()
