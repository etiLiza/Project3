from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO

Allowed_tags = ['sleep','jump','fight','black','white','cute',]#это список поэтому в квадратных скобках


def load_image(url):#
    try:
        response = requests.get(url)#делаем запрос по ссылке.кладем в переменную респонс
        response.raise_for_status()# если будет какая то ошибка то мы получим её вэтой строке
        image_data = BytesIO(response.content)#в эту переменную положим обработанную картинку
        img = Image.open(image_data)# из библиотеки пилой
        img.thumbnail((600,480), Image.Resampling.LANCZOS)#задаем размер изображения,
        # способ изменения размера чтобы картинка не сильно страдала
        return ImageTk.PhotoImage(img)#функция вернет картинку
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

def open_new_window():
    tag = tag_combobox.get()
    url_tag = f"https://cataas.com/cat/{tag}" if tag else "https://cataas.com/cat"
    img = load_image(url_tag)
    if img:
        new_window = Toplevel()
        new_window.title("Картинка с котиком")
        new_window.geometry("600x480")
        label = Label(new_window, image=img)
        label.pack()
        label.image = img  # присваиваем картинку лайблу чтобы сборщик мусора его не удалил


def exit():
    window.destroy()

window = Tk()
window.title("Cats!")
window.geometry("600x480")

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="загрузить фото", command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit)

url = "https://cataas.com/cat"

tag_label = Label(text="Выбери тег")
tag_label.pack()


tag_combobox = ttk.Combobox(values=Allowed_tags)#в ттк очень много виджетов
tag_combobox.pack()

load_button = Button(text="Загрузить по тегу", command=open_new_window)
load_button.pack()

window.mainloop()