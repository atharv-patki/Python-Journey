import qrcode
from tkinter import *
from PIL import Image, ImageTk
f = ("Cambria", 20, "italic")
root = Tk()
root.configure(bg="lightblue")

def generate_qr():
    url = entry.get()
    img = qrcode.make(url)
    img.save("res.png")
    img_display = Image.open("res.png")
    img_display = img_display.resize((350, 350))
    img_tk = ImageTk.PhotoImage(img_display)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk
root.title("QR Code Generator App By Atharv Patki")

entry = Entry(root, width=80)
entry.pack(pady=50)
button = Button(root, text="Generate QR Code", font=f, command=generate_qr)
button.pack(pady=70)
qr_label = Label(root)
qr_label.pack(pady=50)

root.mainloop()import qrcode
from tkinter import *
from PIL import Image, ImageTk
f = ("Cambria", 20, "italic")
root = Tk()
root.configure(bg="lightblue")

def generate_qr():
    url = entry.get()
    img = qrcode.make(url)
    img.save("res.png")
    img_display = Image.open("res.png")
    img_display = img_display.resize((350, 350))
    img_tk = ImageTk.PhotoImage(img_display)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk
root.title("QR Code Generator App By Atharv Patki")

entry = Entry(root, width=80)
entry.pack(pady=50)
button = Button(root, text="Generate QR Code", font=f, command=generate_qr)
button.pack(pady=70)
qr_label = Label(root)
qr_label.pack(pady=50)

root.mainloop()