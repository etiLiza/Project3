from tkinter import *
from PIL import Image? ImageTk
import requests
from io import BytesIO


def loade_image():#
    try:
        response = requests.get()#делаем запрос по ссылке.кладем в переменную респонс
        response.raise_for_status()# если будет какая то ошибка то мы получим её вэтой строке
        image_data = BytesIO(response.content)#в эту переменную положим обработанную картинку



window = Tk()
window.title("Cats!")
window.geometry("600x480")

label = Label()
label.pack()

url = "https://cataas.com/cat"
img = load_image(url)

if img:
    label.config(image=img)
    label.image = img #присваиваем картинку лайблу чтобы сборщик мусора его не удалил

window.mainloop()