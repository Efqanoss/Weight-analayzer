import tkinter as tk
import os
from PIL import ImageTk, Image


# functions
def distur():
    try:
        b = float(boy.get())
        w = float(ceki.get())
        vki = w / b ** 2

        if vki < 18.5:
            cevap = f"zayıf {vki}"
        elif 18.5 <= vki < 24.9:
            cevap = f"normal {vki}"
        elif 25 <= vki < 29.9:
            cevap = f"kilolu {vki}"
        else:
            cevap = f"obez {vki}"

        ex.config(text=cevap, background="lioght blue")
    except:
        ex.config(text="sayı giriniz", background="red")


# Dosya yolları
alan = os.path.dirname(os.path.abspath(__file__))
imag_path = os.path.join(alan, "photos", "main logo.ico")
# arka fon
image_background = os.path.join(alan, "photos", "background.jpg")

# Ekran
window = tk.Tk()
window.minsize(width=294, height=294)
window.title("Weight Tester")
window.iconbitmap(imag_path)

# Arka plan resmini yükle
background_image = Image.open(image_background)
background_photo = ImageTk.PhotoImage(background_image)

# Arka planı yerleştir
background_label = tk.Label(window, image=background_photo)
background_label.place(relwidth=1, relheight=1)

# Worker area
check = tk.IntVar()

kadın = tk.Checkbutton(window, text="Kadın", variable=check, onvalue=0, offvalue=1)
kadın.place(relx=0.3, rely=0.1)

erkek = tk.Checkbutton(window, text="Erkek", variable=check, onvalue=1, offvalue=0)
erkek.place(relx=0.6, rely=0.1)

boy_l = tk.Label(window, text="boy(m)", background="light blue")
boy_l.place(relx=0.1, rely=0.4)

ceki = tk.Entry(window)
ceki.place(relx=0.3, rely=0.3)

ceki_l = tk.Label(window, text="ceki(kq)", background="light blue")
ceki_l.place(relx=0.1, rely=0.3)

boy = tk.Entry(window)
boy.place(relx=0.3, rely=0.4)

click = tk.Button(window, text="hesapla", command=distur)
click.place(relx=0.5, rely=0.6)

ex = tk.Label(window, )
ex.place(relx=0.5, rely=0.7)

# Main
window.mainloop()
