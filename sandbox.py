import tkinter as tk
import Image, ImageDraw


root = tk.Tk()

white = (255, 255, 255)
width = 400
height = 300


cv = tk.Canvas(width=400, height=300, bg='white')
cv.pack()

image1 = Image.new("RGB", (width, height), white)
draw = ImageDraw.Draw(image1)


root.mainloop()