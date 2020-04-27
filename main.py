import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

HEIGHT=720
WIDTH=1280




def close_window():
    window.destroy()


def change(*args):
    print("Running change!")

def RBGAImage(path):
    return Image.open(path).convert("RGBA")


def setOptionOne():
    answer=combo2.get()
    answer2=combo3.get()
    answer3=combo1.get()

    fileName=('baubles.s/'+answer3+answer+answer2+'.png')
    if answer in options2 and answer2 in options3 and answer3 in options1:
        setOption1 = tk.PhotoImage(file=fileName)
        canvasScene.create_image(0,0,image=setOption1,anchor='nw')
        canvasScene.image=setOption1
    elif answer !=options2 and answer2!=options3:
        setOption1 = tk.PhotoImage(file='sadsnowman.png')
        canvasScene.create_image(0,0,image=setOption1,anchor='nw')
        canvasScene.image=setOption1



window=tk.Tk()

window.title("Bombka Wydziału Zarządzania")

options1=['A','B','C','D','E']
options2=['Red','Blue','Pink','Gold','Silver']
options3=['Gold','Silver','White','Red']

canvas=tk.Canvas(window,height=HEIGHT,width=WIDTH)
canvas.pack()


background_image=tk.PhotoImage(file='menu_bg.png')
background_label=tk.Label(window,image=background_image)
background_label.place(relheight=1, relwidth=1)


frame=tk.Frame(window,bg='#941B23')
frame.place(relx=0.3,rely=0.15,relwidth=0.4,relheight=0.6,anchor='n')



canvasScene=Canvas(height=430,width=500,bg='#941B23')
canvasScene.pack()
canvasScene.place(relx=0.75,rely=0.15,anchor='n')


bg_Label=tk.Frame(frame,bg='#941B23',bd=14)
bg_Label.place(relx=0.5,rely=0,relwidth=1,relheight=0.2,anchor='n')

wLabel_image=tk.PhotoImage(file='Banner.png')
wLabel_label=tk.Label(bg_Label,image=wLabel_image,text="Stwórz własną bombkę WZ!",font=('Times New Roman',22,'bold'),fg='black',bg='white', compound=tk.CENTER)
wLabel_label.place(relx=0.5,rely=0.0,relwidth=1,relheight=1,anchor='n')



button6 = tk.Button(frame, text='GENERUJ',font=('Times New Roman',16),
                    width=25,fg="black",bg='white',bd=10,command = setOptionOne)
button6.pack()
button6.place(relx=0.25,rely=0.8,relwidth=0.4,relheight=0.15,anchor='n')
button6.config(width=5,font=('Times New Roman', 20))

combo1=ttk.Combobox(window, values=options1,state='readonly')
combo1.config(width=30,font=('Times New Roman', 20))
combo1.set('Wybierz tło')
combo1.place(relx=0.3,rely=0.32,anchor='n')

combo2=ttk.Combobox(window,values=options2,state='readonly')
combo2.config(width=30,font=('Times New Roman', 20))
combo2.set('Wybierz kolor bombek')
combo2.place(relx=0.3,rely=0.43,anchor='n')


combo3=ttk.Combobox(window,values=options3,state='readonly')
combo3.config(width=30,font=('Times New Roman', 20))
combo3.set('Wybierz kolor napisu')
combo3.place(relx=0.3,rely=0.54,anchor='n')


button_close=tk.Button(frame,text='Zamknij okno',
            font=('Times New Roman',16),bg='white',bd=10,command=close_window)
button_close.place(relx=0.75,rely=0.8,relwidth=0.4,relheight=0.15,anchor='n')


window.mainloop()
