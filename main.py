
import copy
from tkinter import * 
import os
from tkinter.ttk import *
import image as image_l
import mimesis
from mimesis.builtins import RussiaSpecProvider as Rsp
from mimesis.enums import Gender
import base
import sqlite3
from PIL import ImageTk, Image
import io
import time
import datetime



def get_page_people(id):

    global window, dwd, img
    l = base.get_peop(id)
    img = Image.open(io.BytesIO(l[-1])).resize((200, 200))
    img = ImageTk.PhotoImage(img)
    dwd["surname"]["text" ] = l[1]
    dwd["name"]["text" ]  =l[2]
    dwd["patronymic"]["text" ]  = l[3]
    dwd["phone"]["text" ]  = f"Phone: {l[7]}"
    dwd["email"]["text" ]  = f"E-mail: {l[8]}"
    dwd["adr"]["text" ]  = f"Address: {l[6]}"
    dwd["date"]["text" ]  = f"Birthday: {l[5]}"
    dwd["age"]["text" ]  = f"Age: {year-int(l[5][0:4])}"
    dwd["gender"]["text" ]  = f"Gender: {l[4]}"
    dwd["image"]["image" ] =img

def t():
    d = base.get_people()
    for i in d:
        if i[1] == variable.get():
            get_page_people(i[0])
            break



window = Tk()
root = Tk()
window.geometry("800x500")

now = datetime.datetime.now()
year = int(now.year)
person = mimesis.Person("ru")
rus_person = Rsp()
date = mimesis.Datetime()
adress = mimesis.Address("ru")
r = ["None"] + base.get_families()
variable = StringVar(root)
variable.set(r[0])
w = OptionMenu(root, variable, *r)
btn = Button(root, text="Find", command=t)
lt = base.get_peop(0)
img = Image.open(io.BytesIO(lt[-1])).resize((200, 200))
img = ImageTk.PhotoImage(img)
dwd = {
        "surname" : Label(window, text=lt[1], font="Courier 20"),
        "name" : Label(window, text=lt[2], font="Courier 20 "),
        "patronymic" : Label(window, text=lt[3], font="Courier 20"),
        "phone" : Label(window, text=f"Phone: {lt[7]}", font="Courier 20"),
        "email" : Label(window, text=f"E-mail: {lt[8]}", font="Courier 20"),
        "adr" : Label(window, text=f"Address: {lt[6]}", font="Courier 20"),
        "date" : Label(window, text=f"Birthday: {lt[5]}", font="Courier 20"),
        "age" : Label(window, text=f"Age: {year-int(lt[5][0:4])}", font="Courier 20"),
        "gender" : Label(window, text=f"Gender: {lt[4]}", font="Courier 20"),
        "image" : Label(window, image=img)
}



for i in range(30): 
    gender = person.gender()
    gender_opt = Gender.MALE
    if gender == "Жен.":
        gender_opt = Gender.FEMALE
    person_id = base.get_last_id()
    surname = person.surname(gender=gender_opt)
    name = person.first_name(gender=gender_opt)
    patronymic = rus_person.patronymic(gender=gender_opt)
    birthday = date.date(start=1960, end=2021)
    adr = adress.city() + " " + adress.address()
    phone = person.telephone()
    email = person.email()
    img=image_l.get_avatar()
    image = sqlite3.Binary(img)
    l =[person_id, surname, name, patronymic, gender, birthday, adr, phone, email, image]
    base.ins(l)
    time.sleep(1)




dwd["image"].place(x=0,y=0)
dwd["surname"].place(x=225,y=15)
dwd["name"].place(x=225,y=80)
dwd["patronymic"].place(x=225,y=145)
dwd["phone"].place(x=0,y=225)
dwd["email"].place(x=0,y=275)
dwd["adr"].place(x=0,y=325)
dwd["date"].place(x=0,y=375)
dwd["age"].place(x=350,y=375)
dwd["gender"].place(x=0,y=425)
w.pack()
btn.pack()





window.mainloop()
root.mainloop()