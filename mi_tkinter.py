# Podemos aclarar con from de donde queremos importar, y con import que es lo que vamos a importar
from tkinter import *


"""
    El paquete tkinter («interfaz Tk») es la interfaz por defecto de Python para el kit de herramientas de GUI Tk. Tanto Tk como tkinter están disponibles en la mayoría de las plataformas Unix, así como en sistemas Windows (Tk en sí no es parte de Python, es mantenido por ActiveState)
"""
# -----------------|Ventana|-----------------
paddingX = 8
paddingY = 9
fuente_botones = ("Arial", 10, "bold")


ventana = Tk() # -> Creamos la ventana
ventana.configure(bg="#EFF3C9") # -> Este es el metodo que debe ir primero
ventana.title("Calculadora Básica") # -> Configuramos el titulo de la ventana
ventana.geometry("358x355") # -> Le damos un tamaño por defecto

# -> Este metodo sirve para indicar el si usuario puede editar el tamaño (width, height), no lo podrá editar con el valor False
ventana.resizable(False, False)

# -----------------|Entrada de datos|-----------------
datos = Entry(ventana, bg="black", fg="white", font=fuente_botones) #Le indicamos la ventana
datos.grid(columnspan=10, ipadx=108, ipady=18)
"""
   Entry normal tiene un ancho base de unos 140 píxeles (aprox).
    Le pusiste ipadx=150. Esto agrega 150px a la izquierda + 150px a la derecha.
    Suma de relleno: 300 px.
    Total: 140 (base) + 300 (relleno) = 440 píxeles

    columnspam: cantidad de columnas que ocupa
    padx: margen eje X
    pady: margen eje Y
    ipadx: padding eje X
    ipady: padding eje Y

    El columnspan solo se ve cuando tienes otros elementos abajo que definen el ancho de las columnas individuales.
"""
# -----------------|Botones|-----------------



btn1 = Button(ventana, text="1", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}")
btn1.grid(columnspan=2, row=1, column=0)

btn2 = Button(ventana, text="2", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}")
btn2.grid(columnspan=2, row=1, column=2)

btn3 = Button(ventana, text="3", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}")
btn3.grid(columnspan=2, row=1, column=4)

btnMas = Button(ventana, text="+", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}")
btnMas.grid(columnspan=2, row=1, column=6)

btnBorrar = Button(ventana, text="←", font=fuente_botones, fg="red", bg="white", height=2, width=6, padx=paddingX, pady=paddingY)
btnBorrar.grid(columnspan=2, row=1, column=8)

# Fila 2
btn4 = Button(ventana, text="4", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}")
btn4.grid(columnspan=2, row=2, column=0)

btn5 = Button(ventana, text="5", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}")
btn5.grid(columnspan=2, row=2, column=2)

btn6 = Button(ventana, text="6", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}")
btn6.grid(columnspan=2, row=2, column=4)

btnMenos = Button(ventana, text="-", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}")
btnMenos.grid(columnspan=2, row=2, column=6)

btnCuadrado = Button(ventana, text="x²", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=paddingX, pady=paddingY)
btnCuadrado.grid(columnspan=2, row=2, column=8)

#Fila 3
btn7 = Button(ventana, text="7", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}")
btn7.grid(columnspan=2, row=3, column=0)

btn8 = Button(ventana, text="8", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}")
btn8.grid(columnspan=2, row=3, column=2)

btn9 = Button(ventana, text="9", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}")
btn9.grid(columnspan=2, row=3, column=4)

btnMultiplicacion = Button(ventana, text="*", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}")
btnMultiplicacion.grid(columnspan=2, row=3, column=6)

btnRaiz = Button(ventana, text="√", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=paddingX, pady=paddingY)
btnRaiz.grid(columnspan=2, row=3, column=8)

#Fila 4
btn0 = Button(ventana, text="0", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}")
btn0.grid(columnspan=2, row=4, column=0)

btnPunto = Button(ventana, text=".", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}")
btnPunto.grid(columnspan=2, row=4, column=2)

btnLimpiar = Button(ventana, text="Limpiar", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}")
btnLimpiar.grid(columnspan=2, row=4, column=4)

btnDividir = Button(ventana, text="/", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}")
btnDividir.grid(columnspan=2, row=4, column=6)

btnInverso = Button(ventana, text="1/x", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=paddingX, pady=paddingY)
btnInverso.grid(columnspan=2, row=4, column=8)

#Fila 5
btnParentesisIzquierdo = Button(ventana, text="(", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}")
btnParentesisIzquierdo.grid(columnspan=2, row=5, column=0)

btnIgual = Button(ventana, text="=", font=fuente_botones, fg="black", bg="white", height=2, width=6, pady=f"{paddingY}")
btnIgual.grid(columnspan=4, row=5, column=2, sticky="ew")

btnParentesisDerecho = Button(ventana, text=")", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}")
btnParentesisDerecho.grid(columnspan=2, row=5, column=6)

btnPi = Button(ventana, text="π", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=paddingX, pady=paddingY)
btnPi.grid(columnspan=2, row=5, column=8)

ventana.mainloop() # -> Abrimos la ventana, debe ir al final de todo, una vez qeu ya esta configurada la ventana