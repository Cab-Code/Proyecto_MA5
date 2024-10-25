from numpy import *
import matplotlib.pyplot as plt
import tkinter as tk

#Crear Plano 

def graficar(f, xa, xb):
    a = linspace(3*xa,3*xb, 500)
    b= linspace(3*xa, 3*xb, 500)

    x, y = meshgrid(a, b)

    z = x + 1j*y

    omega = eval(f)
    print("omega:",f)
    try:
        plt.figure(figsize=(10, 5))

        plt.subplot(1,2,2) 
        imaginaria = plt.contour(x, y, omega.imag, levels=50)
        plt.colorbar()
        plt.title('Imaginario{\u03A9} = \u03A8')

        plt.subplot(1, 2, 1) 
        real = plt.contour(x, y, omega.real, levels=50)
        plt.colorbar()
        plt.title('Real{\u03A9} = \u03A6')
        plt.tight_layout()
        plt.show()

    except:
        Error = tk.Tk()
        Error.title("Graficador de Diritchlet")
        label_error = tk.Label(Error, text="El mapeo debe tener formato numpy")
        label_error.pack(pady=10)    
        Error.mainloop()
        return




def crear_omega(array, mapeo):


    funcion = f'{array[-1][0]} - (1j/pi)*('
    
    n = len(array)

    for i in range(n):
        if i == 0:
            continue
        try:
            z = array[i-1][1]
            xi = eval(mapeo)
        except:
            Error = tk.Tk()
            Error.title("Graficador de Diritchlet")
            label_error = tk.Label(Error, text="El mapeo debe tener formato numpy")
            label_error.pack(pady=10)    
            Error.mainloop()
        str = f'({array[i-1][0]}-{array[i][0]})*log({mapeo}-{xi})+'
        funcion = f'{funcion}{str}'

    funcion = f'{funcion}0)'


    z = array[1][1]
    xa = eval(mapeo)

    z = array[-1][1]
    xb = eval(mapeo)


    graficar(funcion, xa, xb)



    
    crear_omega(array, map)

def numerico(string):
    try:
        complejo= complex(string)  # Intenta convertir la cadena a float
        return True
    except ValueError:
        return False

def get_datos(array, entry_map):
    i = 0
    nuevo_array = []
    for dat in array:
        i = i + 1
        if i != len(array):
            dat1 = dat[1].get()
            dat2 = dat[2].get()
        else:
            dat1 = dat[1].get()
            dat2 = "0"
        if(numerico(dat1) and numerico(dat2)):

            nuevo_array.append([complex(dat1), complex(dat2)])
        else:
            Error = tk.Tk()
            Error.title("Ejemplo de Tkinter")
            label_error = tk.Label(Error, text="Los datos deben ser numericos")
            label_error.pack(pady=10)    
            Error.mainloop()
            return
    mapeo = entry_map.get()

    crear_omega(nuevo_array, mapeo)
    quitar_entry(array)
    anadir_entry(array)
    

def anadir_entry(array):
    if (len(array) <= 7):
        for boton in array:
            boton[0].destroy()
        array.append([0,0,0])
        crear_entry(array)

def quitar_entry(array):
    for boton in array:
        boton[0].destroy()
    array.pop()
    crear_entry(array)


def crear_entry(array):
    i = 0
    for boton in array:
        boton[0] = tk.Frame(root, padx=10, pady=10)
        boton[0].pack(side = tk.LEFT, padx=10, pady=10)
        label = tk.Label(boton[0], text="Condicion de frontera")
        label.pack(pady=10)
        boton[1]= tk.Entry(boton[0])
        boton[1].pack(pady=10)
        if i != len(array)-1:
            label2 = tk.Label(boton[0], text="Posicion 'x'")
            label2.pack(pady=20)
            boton[2] = tk.Entry(boton[0])
            boton[2].pack(pady=20)
            


        i = i + 1



root = tk.Tk()
root.title("Graficador de Diritchlet con mapeo")

label_map = tk.Label(root, text="Mapeo:")
label_map.pack(pady=10)
Entry_map = tk.Entry(root)
Entry_map.pack(pady=10)

entrada_datos = [[0,0,0],[0,0,0],[0,0,0]]





crear_entry(entrada_datos)


frame2 = tk.Frame(root)
frame2.pack(side = tk.TOP, pady=5)
button_menos = tk.Button(frame2, text=" - ", command=lambda:quitar_entry(entrada_datos))
button_menos.pack(side = tk.LEFT, pady=5)


button_mas = tk.Button(frame2, text=" + ", command=lambda:anadir_entry(entrada_datos))
button_mas.pack(side = tk.LEFT, pady=5)

# Iniciar el bucle principal de la interfaz

button_mas = tk.Button(root, text=" graficar ", command=lambda:get_datos(entrada_datos, Entry_map))
button_mas.pack(pady=5)

root.mainloop()