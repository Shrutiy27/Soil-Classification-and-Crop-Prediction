import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk
from subprocess import call

def shift():
    x1, y1, x2, y2 = canvas.bbox("marquee")
    if x2 < 0 or y1 < 0:
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height() // 2
        canvas.coords("marquee", x1, y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(1000 // fps, shift)

def cnn_prediction():
    call(["python", "GUI_Master_crop.py"])

def svm_prediction():
    call(["python", "Check_crop.py"])

root = tk.Tk()
root.title("Soil and Crop Prediction Using Machine Learning")
root.geometry("1600x900")
root.configure(bg="#1E1E1E")

bg = Image.open("image4.jpg")
bg = bg.resize((1600, 900), Image.LANCZOS)
bg_img = ImageTk.PhotoImage(bg)
bg_lbl = tk.Label(root, image=bg_img)
bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

canvas = Canvas(root, bg="#000000")
canvas.pack()
text_var = "Soil and Crop Prediction Using Machine Learning"
text = canvas.create_text(0, -2000, text=text_var, font=('Raleway', 25, 'bold'), fill='white', tags=("marquee",), anchor='w')
x1, y1, x2, y2 = canvas.bbox("marquee")
canvas['width'] = 1600
canvas['height'] = 100
fps = 40
shift()

info_label = tk.Label(root, text='''If we grow more food, there will be enough food to feed everyone. If we cultivate the land to grow enough crops, humanity will not go hungry.''', font=("Calibri", 14), fg="white", bg="#1E1E1E", wraplength=600, justify="left")
info_label.place(x=50, y=150)

quote_label = tk.Label(root, text='''Agriculture is our wisest pursuit because it will in the end contribute most to real wealth, good morals, and happiness.''', font=("Calibri", 14), fg="white", bg="#1E1E1E", wraplength=600, justify="left")
quote_label.place(x=50, y=300)

d2 = tk.Button(root, text="CNN Prediction", command=cnn_prediction, width=20, height=2, bd=0, bg="#007ACC", fg="white", font=("Arial", 14, "bold"))
d2.place(x=1100, y=350)

d3 = tk.Button(root, text="SVM Prediction", command=svm_prediction, width=20, height=2, bd=0, bg="#E63946", fg="white", font=("Arial", 14, "bold"))
d3.place(x=1100, y=450)

root.mainloop()
