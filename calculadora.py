# Podemos aclarar con from de donde queremos importar, y con import que es lo que vamos a importar
from tkinter import *
import math

# -----------------|Funciones de la calculadora (BACKEND)|-----------------

digito = ""
def tomar_digito(n):
    global digito
    digito = digito + str(n)
    calculo.set(digito)

def operacion_especial(tipo:str = "igual"):
    global digito
    if not digito: return # no hace nada

    try:
        valor = float(eval(digito))
        if tipo == "raiz":
            res = valor ** 0.5
        elif tipo == "cuadrado":
            res = valor ** 2
        elif tipo == "inverso":
            res = 1 / valor
        elif tipo == "igual":
            res = eval(digito)
        
        # final comun para todas las operaciones
        resultado_str = str(res)
        digito = resultado_str
        calculo.set(resultado_str)
        
    except ZeroDivisionError:
        calculo.set("No se puede dividir por 0")
        digito = ""
        
    except SyntaxError:
        calculo.set("Error de sintaxis")
        digito = ""
        
    except Exception:
        calculo.set("Operación inválida")
        digito = ""

def limpiar_completo():
    global digito
    digito = ""
    calculo.set("")

def calcular_raiz():
    global digito
    if digito:
        resultado = str(float(digito) ** 0.5)
        digito = resultado
        calculo.set(resultado)

def calcular_cuadrado():
    global digito
    if digito:
        resultado = str(float(digito) * float(digito))
        digito = resultado
        calculo.set(resultado)

def calcular_inverso():
    global digito
    if digito:
        resultado = str(1 / float(digito))
        digito = resultado
        calculo.set(resultado)

def borrar_ultimo():
    global digito
    digito = digito[:-1]
    calculo.set(digito) 

# -----------------|UX de la calculadora (FRONTEND)|-----------------

"""
    El paquete tkinter («interfaz Tk») es la interfaz por defecto de Python
    para el kit de herramientas de GUI Tk. Tanto Tk como tkinter están 
    disponibles en la mayoría de las plataformas Unix, así como en 
    sistemas Windows (Tk en sí no es parte de Python, es mantenido por ActiveState)
"""
# -----------------|Ventana|-----------------
paddingX = 8
paddingY = 9
fuente_botones = ("Arial", 10, "bold")


ventana = Tk() # -> Creamos la ventana
ventana.configure(bg="#EFF3C9") # -> Este es el metodo que debe ir primero
ventana.title("Calculadora Básica") # -> Configuramos el titulo de la ventana
ventana.geometry("358x355") # -> Le damos un tamaño por defecto

calculo = StringVar()

# -> Este metodo sirve para indicar el si usuario puede editar el tamaño (width, height), no lo podrá editar con el valor False
ventana.resizable(False, False)

# -----------------|Entrada de datos|-----------------
datos = Entry(ventana, bg="black", fg="white", font=fuente_botones, textvariable=calculo) #Le indicamos la ventana
datos.grid(columnspan=10, ipadx=108, ipady=18)

# -----------------|Botones|-----------------

lista_botones = [
    [
        {"texto": "1", "command": lambda: tomar_digito(1)}, 
        {"texto": "2", "command": lambda: tomar_digito(2)},
        {"texto": "3", "command": lambda: tomar_digito(3)},
        {"texto": "+", "command": lambda: tomar_digito("+")},  
        {"texto": "←", "command": borrar_ultimo}
    ],
    [
        {"texto": "4", "command": lambda: tomar_digito(4)}, 
        {"texto": "5", "command": lambda: tomar_digito(5)},
        {"texto": "6", "command": lambda: tomar_digito(6)}, 
        {"texto": "-", "command": lambda: tomar_digito("-")},
        {"texto": "x²", "command": lambda: operacion_especial("cuadrado")}
    ],
    [
        {"texto": "7", "command": lambda: tomar_digito(7)}, 
        {"texto": "8", "command": lambda: tomar_digito(8)},
        {"texto": "9", "command": lambda: tomar_digito(9)}, 
        {"texto": "*", "command": lambda: tomar_digito("*")},
        {"texto": "√", "command": lambda: operacion_especial("raiz")}
    ],
    [
        {"texto": "0", "command": lambda: tomar_digito(0)}, 
        {"texto": ".", "command": lambda: tomar_digito(".")},
        {"texto": "Limpiar", "command": limpiar_completo}, 
        {"texto": "/", "command": lambda: tomar_digito("/")},
        {"texto": "1/x", "command": lambda: operacion_especial("inverso")}
    ],
    [
        {"texto": "(", "command": lambda: tomar_digito("(")}, 
        {"texto": "=", "command": lambda: operacion_especial("igual"), "sticky": "ew"},
        {"texto": ")", "command": lambda: tomar_digito(")")}, 
        {"texto": "π", "command": lambda: tomar_digito(math.pi)}
    ]
]


for i in range(len(lista_botones)):
    columna_visual = 0
    
    for j in range(0, len(lista_botones[i])):
        btn = Button(ventana, 
                     text=lista_botones[i][j]["texto"], 
                     font=fuente_botones,
                     fg="black", bg="white",
                     height=2, width=6,
                     padx=f"{paddingX}", pady=f"{paddingY}",
                     command=lista_botones[i][j]["command"]
        )
        ancho = 4 if lista_botones[i][j]["texto"] == "=" else 2
        btn.grid(
            columnspan= ancho, 
            row=i+1, column=columna_visual, 
            sticky= lista_botones[i][j].get("sticky", None)
        )

        columna_visual += ancho














'''
btn1 = Button(ventana, text="1", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}", command = lambda: tomar_digito(1))
btn1.grid(columnspan=2, row=1, column=0)

btn2 = Button(ventana, text="2", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}", command = lambda: tomar_digito(2))
btn2.grid(columnspan=2, row=1, column=2)

btn3 = Button(ventana, text="3", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}", command = lambda: tomar_digito(3))
btn3.grid(columnspan=2, row=1, column=4)

btnMas = Button(ventana, text="+", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}", command = lambda: tomar_digito("+"))
btnMas.grid(columnspan=2, row=1, column=6)

btnBorrar = Button(ventana, text="←", font=fuente_botones, fg="red", bg="white", height=2, width=6, padx=paddingX, pady=paddingY, command=borrar_ultimo)
btnBorrar.grid(columnspan=2, row=1, column=8)

# Fila 2
btn4 = Button(ventana, text="4", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}", command = lambda: tomar_digito(4))
btn4.grid(columnspan=2, row=2, column=0)

btn5 = Button(ventana, text="5", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}", command = lambda: tomar_digito(5))
btn5.grid(columnspan=2, row=2, column=2)

btn6 = Button(ventana, text="6", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}", command = lambda: tomar_digito(6))
btn6.grid(columnspan=2, row=2, column=4)

btnMenos = Button(ventana, text="-", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}", command = lambda: tomar_digito("-"))
btnMenos.grid(columnspan=2, row=2, column=6)

btnCuadrado = Button(ventana, text="x²", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=paddingX, pady=paddingY, command = lambda: operacion_especial("cuadrado"))
btnCuadrado.grid(columnspan=2, row=2, column=8)

#Fila 3
btn7 = Button(ventana, text="7", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}", command = lambda: tomar_digito(7))
btn7.grid(columnspan=2, row=3, column=0)

btn8 = Button(ventana, text="8", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}", command = lambda: tomar_digito(8))
btn8.grid(columnspan=2, row=3, column=2)

btn9 = Button(ventana, text="9", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}", command = lambda: tomar_digito(9))
btn9.grid(columnspan=2, row=3, column=4)

btnMultiplicacion = Button(ventana, text="*", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}", command = lambda: tomar_digito("*"))
btnMultiplicacion.grid(columnspan=2, row=3, column=6)

btnRaiz = Button(ventana, text="√", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=paddingX, pady=paddingY, command = lambda: operacion_especial("raiz"))
btnRaiz.grid(columnspan=2, row=3, column=8)
#Fila 4
btn0 = Button(ventana, text="0", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}", command = lambda: tomar_digito(0))
btn0.grid(columnspan=2, row=4, column=0)

btnPunto = Button(ventana, text=".", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}", command = lambda: tomar_digito("."))
btnPunto.grid(columnspan=2, row=4, column=2)

btnLimpiar = Button(ventana, text="Limpiar", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}", command = limpiar_completo)
btnLimpiar.grid(columnspan=2, row=4, column=4)

btnDividir = Button(ventana, text="/", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}", command = lambda: tomar_digito("/"))
btnDividir.grid(columnspan=2, row=4, column=6)

btnInverso = Button(ventana, text="1/x", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=paddingX, pady=paddingY, command = lambda: operacion_especial("inverso"))
btnInverso.grid(columnspan=2, row=4, column=8)
#Fila 5
btnParentesisIzquierdo = Button(ventana, text="(", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}", command = lambda: tomar_digito("("))
btnParentesisIzquierdo.grid(columnspan=2, row=5, column=0)

btnIgual = Button(ventana, text="=", font=fuente_botones, fg="black", bg="white", height=2, width=6, pady=f"{paddingY}", command = lambda: operacion_especial("igual"))
btnIgual.grid(columnspan=4, row=5, column=2, sticky="ew")

btnParentesisDerecho = Button(ventana, text=")", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=f"{paddingX}", pady=f"{paddingY}", command = lambda: tomar_digito(")"))
btnParentesisDerecho.grid(columnspan=2, row=5, column=6)

btnPi = Button(ventana, text="π", font=fuente_botones, fg="black", bg="white", height=2, width=6, padx=paddingX, pady=paddingY, command= lambda: tomar_digito(math.pi))
btnPi.grid(columnspan=2, row=5, column=8)
'''


# -> Abrimos la ventana, debe ir al final de todo, 
# -> Una vez que ya esta configurado todo lo que tendra la misma
ventana.mainloop() 
