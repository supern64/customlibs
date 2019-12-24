from PIL import ImageTk, Image, ImageDraw
import PIL
from tkinter import *

class UCanvas:
    def __init__(self, width=400, height=400, color="black", bg=(255, 255, 255), filename="default.jpg", thickness=5):
        self.width = width
        self.height = height
        self.color = color
        self.bg = bg
        self.filename = filename
        self.thickness = thickness

    def _save(self):
        self.output_image.save(self.filename)
        self.master.destroy()

    def _paint(self, event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, width=self.thickness)
        self.draw.line([x1, y1, x2, y2], fill=self.color, width=self.thickness)

    def init_and_takeover(self):
        self.master = Tk()

        self.canvas = Canvas(self.master, width=self.width, height=self.height, bg='white')
        self.canvas.pack()

        self.output_image = PIL.Image.new("RGB", (self.width, self.height), self.bg)
        self.draw = ImageDraw.Draw(self.output_image)
        self.canvas.pack(expand=YES, fill=BOTH)
        self.canvas.bind("<B1-Motion>", self._paint)

        button = Button(text="OK",command=self._save)
        button.pack()

        self.master.mainloop()

        return self.filename