from tkinter import DISABLED, RIGHT, Frame, ttk, messagebox, Tk, PhotoImage, Label, Canvas, Button, NORMAL
from rutas import lineas, seg
ventana = Tk()
ventana.title("UMAPS")
ventana.iconbitmap("img/icono.ico")
ventana.geometry("1170x500")
ventana.resizable(0,0)
ventana.config(bg="#4952b9")
imagen=PhotoImage(file="img/mapita.png")
location=["A","B","D","E","F","G","H","I","J","K","L","N","EA","Biblioteca","Lab. Teleco","Lab. Fisica","Lab. Industrial",]
mapa =Canvas(ventana,width=1024,height=500)
mapa.grid(row=0, column=1, rowspan=8)
mapa.create_image( 0, 0, image = imagen,  
                   anchor = "nw") 
view = 0
def buscar1(event):
    value = event.widget.get()
    if value == '':
        ubic['value']=location
    else:
        data = []

        for item in location:
            if value.lower() in item.lower():
                data.append(item)
        ubic['values'] = data
def buscar2(event):
    value = event.widget.get()
    if value == '':
        dest['value']=location
    else:
        data = []

        for item in location:
            if value.lower() in item.lower():
                data.append(item)
        dest['values'] = data
def lines():
    global view
    if view == 0:
        labs=["Lab. Fisica","Lab. Industrial"]
        selection = ubic.get()
        selection2 = dest.get()
        messagebox.showinfo(
            message=f"Las opciones seleccionada son: {selection,selection2}",
            title="Selección"
        )
        avanc = 0
        for i in labs:
            if selection2 == i:
                lblpiso.config(text="Piso")
                lblnum.config(text="4")
        for i in range(seg):
            mapa.create_line(lineas[avanc+0],lineas[avanc+1],lineas[avanc+2],lineas[avanc+3],width=4,fill='#cb1085', tag= "ruta")
            avanc =avanc + 2
        view = 1
    else:
        messagebox.showinfo(
        message="Es necesario borrar la ruta anterior para generar una nueva",
        title="Error"
    )

def erase():
    mapa.delete("ruta")
    lblpiso.config(text="")
    lblnum.config(text="")
    global view
    view = 0

lblpiso = Label(ventana,text="",background="#4952b9")
lblpiso.config(font=("Verdana",24))
lblpiso.grid(row=4,column=0)
lblnum = Label(ventana,text="",background="#4952b9")
lblnum.config(font=("Verdana",24))
lblnum.grid(row=5,column=0)
lblubic = Label(ventana,text="Ubicación",bg="#4952b9",fg="white").grid(row=0,column=0)
ubic= ttk.Combobox(
    values=location
)
ubic.set('Buscar')
ubic.bind('<KeyRelease>',buscar1)
ubic.grid(row=1,column=0)
lbldest = Label(ventana,text="Destino",bg="#4952b9",fg="white").grid(row=2,column=0)
dest= ttk.Combobox( 
    values=location
)
dest.grid(row=3,column=0)
dest.set('Buscar')
dest.bind('<KeyRelease>',buscar2)



btn = Button(ventana,text="Buscar",width=19,command=lines, state="normal").grid(row=6,column=0)
btn2 = Button(ventana,text="Borrar",width=19,command=erase, state="normal").grid(row=7,column=0)


ventana.mainloop()
