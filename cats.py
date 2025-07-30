from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


def load_image(url):#
    try:
        response = requests.get(url)#делаем запрос по ссылке.кладем в переменную респонс
        response.raise_for_status()# если будет какая то ошибка то мы получим её вэтой строке
        image_data = BytesIO(response.content)#в эту переменную положим обработанную картинку
        img = Image.open(image_data)# из библиотеки пилой
        return ImageTk.PhotoImage(img)#функция вернет картинку
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

def set_image():
    img = load_image(url)

    if img:
        label.config(image=img)
        label.image = img  # присваиваем картинку лайблу чтобы сборщик мусора его не удалил

window = Tk()
window.title("Cats!")
window.geometry("600x480")

label = Label()
label.pack()

update_button = Button(text="Обновить", command=set_image)

url = "https://cataas.com/cat"
set_image()

window.mainloop()