from tkinter import *
from tkinter import messagebox
import pymysql

def Menu_principal():

    # Creando ventana del inicio
    global pantalla
    pantalla = Tk()
    pantalla.geometry("350x445")
    pantalla.title("Bienvenido")
    pantalla.iconbitmap("inicio.ico")


    # Agregando una iamgen
    image = PhotoImage(file = "iniciar.gif")
    image = image.subsample(4, 4)
    label = Label(image = image)
    label.pack()

    # creando etiqueta
    Label(text = "Acceso al Sistema", bg = "navy", font = ("Cambria", 15),
          fg = "white", width = "350", height = "3").pack()
    Label(text = "").pack()

    # Creando los botones
    Button(text = "Iniciar Seccion", command = inicio_seccion,font = "Cambria", width = "30", height = "2").pack()
    Label(text = "").pack()
    Button(text = "Registrarse", command = registrar,font = "Cambria", width = "30", height = "2").pack()
    Label(text = "").pack()
    Button(text = "Salir", font = "Cambria", width = "30", height = "2", command = pantalla.quit).pack()

    pantalla.mainloop()



# Funcion para la pantalla de iniciar seccion
def inicio_seccion():
    global pantalla1
    pantalla1 = Toplevel(pantalla)
    pantalla1.geometry("400x350")
    pantalla1.title("Inicio de Seccion")
    pantalla1.iconbitmap("inicio.ico")


    Label(pantalla1, text = "Por favor ingrese su usuario y contraseña\n a continuacion", bg = "navy", font = ("Cambria", 15),
          fg = "white", width = "350", height = "3").pack()
    Label(pantalla1, text = "").pack()

    global nombreUsuario_verify
    global password_verify

    nombreUsuario_verify = StringVar()
    password_verify = StringVar()

    global nombre_usuario_entry
    global password_usuario_entry

    # Dandole entrada a el usuario y la contaseña
    Label(pantalla1, text = "Usuario", font = ("Cambria", 15),
          fg = "Black", width = "20", height = "2").pack()
    nombre_usuario_entry = Entry(pantalla1, textvariable = nombreUsuario_verify, width = "40")
    nombre_usuario_entry.pack()
    Label(pantalla1).pack()

    Label(pantalla1, text="Contraseña", font = ("Cambria", 15),
          fg = "Black", width = "20", height = "2").pack()
    password_usuario_entry= Entry(pantalla1, textvariable = password_verify, width = "40", show = "*")
    password_usuario_entry.pack()
    Label(pantalla1).pack()

    # Creando boton de la pantalla1 para iniciar seccion
    Button(pantalla1, text = "Iniciar Seccion", font = "Cambria", width = "30", height = "2").pack()

# Funcion que contiene la ventana para hacer el registro
def registrar():
    # Creando la ventana de registro
    global pantalla2
    pantalla2 = Toplevel(pantalla)
    pantalla2.geometry("410x350")
    pantalla2.title("Registrarse")
    pantalla2.iconbitmap("inicio.ico")

    global nombreUsuario_entry
    global password_entry

    nombreUsuario_entry = StringVar()
    password_entry = StringVar()

    # Creando etiqueta
    Label(pantalla2, text = "Por favor ingrese un usuario y una contraseña,\n para el Registrarse en el Sitema ",
          bg="navy", font=("Cambria", 15), fg="white", width="350", height="3").pack()
    Label(pantalla2, text="").pack()

    # Dandole entrada para el registro
    Label(pantalla2, text="Usuario", font=("Cambria", 15),
          fg="Black", width="20", height="2").pack()
    nombreUsuario_entry = Entry(pantalla2,width="40")
    nombreUsuario_entry.pack()
    Label(pantalla2).pack()

    Label(pantalla2, text="Contraseña", font=("Cambria", 15),
          fg="Black", width="20", height="2").pack()
    password_entry = Entry(pantalla2, width="40", show = "*")
    password_entry.pack()
    Label(pantalla2).pack()

    # Creando boton de la pantalla2 para Registrarse
    Button(pantalla2, text="Registrarse", command = insertar_datos, font="Cambria", width="30", height="2").pack()

# Esta funcion realiza la conexion a la base de datos e inserta los datos de la ventana registro en la tabla login
def insertar_datos():
    bd = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "",
        db = "bd_inicioseccion"

    )
    fcursor = bd.cursor()
    sql = "INSERT INTO login (Usuario ,Contraseña) VALUES ('{0}','{1}')".format(nombreUsuario_entry.get(), password_entry.get())

    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message= "Registro exitoso", title= "Aviso")

    except:
        bd.rollback()
        messagebox.showinfo(message="No se pudo Registrar", title="Aviso")

    bd.close()

Menu_principal()


















