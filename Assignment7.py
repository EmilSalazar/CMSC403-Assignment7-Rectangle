import tkinter as tk
import sys


class CustomCanvas:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, height=self.height, width=self.width)
        self.canvas.pack()

    def draw_rectangle(self, rect, color='blue'):
        self.canvas.create_rectangle(rect.x, rect.y, rect.x + rect.width, rect.y + rect.height, outline='black',
                                     fill=color)

    def show(self):
        self.root.mainloop()


class Rectangle:
    def __init__(self, height, width, x=0, y=0):
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Rectangle({self.height}, {self.width}, {self.x}, {self.y})"


def pack(allRect, canvasSize):
    canvas_height, canvas_width = canvasSize
    placed_rectangles = []
    for rect in allRect:
        placed = False
        for x in range(canvas_width):
            if placed:
                break
            for y in range(canvas_height):
                if all(not (r.x < x + rect.width and r.x + r.width > x and r.y < y + rect.height and r.y + r.height > y)
                       for r in placed_rectangles):
                    rect.x, rect.y = x, y
                    placed_rectangles.append(rect)
                    placed = True
                    break
    return placed_rectangles


def main():
    if len(sys.argv) < 2:
        print("Usage: python Assignment7.py <filepath>")
        return

    filepath = sys.argv[1]
    with open(filepath, 'r') as file:
        lines = file.readlines()
        canvas_height, canvas_width = map(int, lines[0].strip().split(','))
        rectangles = [Rectangle(*map(int, line.strip().split(','))) for line in lines[1:]]

    canvas = CustomCanvas(canvas_height, canvas_width)
    packed_rectangles = pack(rectangles, (canvas_height, canvas_width))

    for rect in packed_rectangles:
        canvas.draw_rectangle(rect)

    canvas.show()


if __name__ == "__main__":
    main()
