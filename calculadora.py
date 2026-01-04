# Podemos aclarar con from de donde queremos importar, y con import que es lo que vamos a importar
from tkinter import *
import math

# -----------------|Funciones de la calculadora (BACKEND)|-----------------

class Calculadora:
    """
    Clase principal que maneja la lógica y la interfaz de la calculadora.
    Utiliza Tkinter para la GUI y encapsula el estado de las operaciones.
    """

    def __init__(self, ventana):
        self._ventana = ventana
        self._digito = ""
        self._calculo = StringVar()
        self._datos = None
        
        # Configuración de estilos
        self._paddingX = 8
        self._paddingY = 9
        self._fuente_botones = ("Arial", 10, "bold")
        
        # Inicialización de componentes
        self._configurar()
        
    def _configurar(self):
        #Orquesta la configuración inicial de la ventana y widgets.
        self._configurar_ventana()
        self._configurar_input_datos()
        self._configurar_layout_botones()
    
    def _configurar_ventana(self):
        self._ventana.configure(bg="#EFF3C9") 
        self._ventana.title("Calculadora Básica") 
        self._ventana.geometry("358x355") 
        self._ventana.resizable(False, False)
        # Para escuchar el teclado
        self._ventana.bind("<Key>", self._evento_teclado)
    
    def _evento_teclado(self, event):
        acciones_especiales = {
           "Return": lambda: self._operacion_especial("igual"),
           "BackSpace": lambda: self._borrar_ultimo(),
           "Escape": lambda: self._limpiar_completo(),
           "p": lambda: self._tomar_digito(math.pi),
           "i": lambda: self._operacion_especial("inverso"),
           "c": lambda: self._operacion_especial("cuadrado"),
           "r": lambda: self._operacion_especial("raiz"),
        }

        accion = acciones_especiales.get(event.keysym)
        if accion:
            accion()
        else :
            permitidos = "0123456789.+-*/()"
            if event.char in permitidos and event.char != "":
                self._tomar_digito(event.char)
        
        # TODO Cuando hagamos el historial, mostrar un breve msj de q esa tecla no esta permitida

    def _configurar_input_datos(self):
        #Configura el display de entrada de datos.
        self._datos = Entry(
            self._ventana, 
            bg="black", 
            fg="white", 
            font=self._fuente_botones, 
            textvariable=self._calculo
        )
        self._datos.grid(columnspan=10, ipadx=108, ipady=18)
    
    def _configurar_layout_botones(self):
        """
        Genera la grilla de botones dinámicamente iterando sobre una matriz de configuración.
        Maneja anchos variables (como el botón '=') usando un contador de columna visual.
        """
        lista_botones = [
            [
                {"texto": "1", "command": lambda: self._tomar_digito(1)}, 
                {"texto": "2", "command": lambda: self._tomar_digito(2)},
                {"texto": "3", "command": lambda: self._tomar_digito(3)},
                {"texto": "+", "command": lambda: self._tomar_digito("+")},  
                {"texto": "←", "command": lambda: self._borrar_ultimo()}
            ],
            [
                {"texto": "4", "command": lambda: self._tomar_digito(4)}, 
                {"texto": "5", "command": lambda: self._tomar_digito(5)},
                {"texto": "6", "command": lambda: self._tomar_digito(6)}, 
                {"texto": "-", "command": lambda: self._tomar_digito("-")},
                {"texto": "x²", "command": lambda: self._operacion_especial("cuadrado")}
            ],
            [
                {"texto": "7", "command": lambda: self._tomar_digito(7)}, 
                {"texto": "8", "command": lambda: self._tomar_digito(8)},
                {"texto": "9", "command": lambda: self._tomar_digito(9)}, 
                {"texto": "*", "command": lambda: self._tomar_digito("*")},
                {"texto": "√", "command": lambda: self._operacion_especial("raiz")}
            ],
            [
                {"texto": "0", "command": lambda: self._tomar_digito(0)}, 
                {"texto": ".", "command": lambda: self._tomar_digito(".")},
                {"texto": "Limpiar", "command": lambda: self._limpiar_completo()}, 
                {"texto": "/", "command": lambda: self._tomar_digito("/")},
                {"texto": "1/x", "command": lambda: self._operacion_especial("inverso")}
            ],
            [
                {"texto": "(", "command": lambda: self._tomar_digito("(")}, 
                {"texto": "=", "command": lambda: self._operacion_especial("igual"), "sticky": "ew"},
                {"texto": ")", "command": lambda: self._tomar_digito(")")}, 
                {"texto": "π", "command": lambda: self._tomar_digito(math.pi)}
            ]
        ]


        for i in range(len(lista_botones)):
            # Cursor para manejar botones de distinto ancho
            columna_visual = 0
            
            for j in range(0, len(lista_botones[i])):
                btn_actual_info = lista_botones[i][j]

                btn = Button(self._ventana, 
                    text=btn_actual_info["texto"], 
                    font=self._fuente_botones,
                    fg="black", 
                    bg="white",
                    height=2, 
                    width=6,
                    padx=f"{self._paddingX}", 
                    pady=f"{self._paddingY}",
                    command=btn_actual_info["command"]
                )

                # Determinamos el ancho del botón (el '=' ocupa 4 columnas, el resto 2)
                ancho = 4 if btn_actual_info["texto"] == "=" else 2
                btn.grid(
                    columnspan= ancho, 
                    row=i+1, 
                    column=columna_visual, 
                    sticky=btn_actual_info.get("sticky", None)
                )

                # Avanzamos el cursor visual
                columna_visual += ancho

    def _tomar_digito(self, n):
        """Concatena el nuevo dígito o símbolo a la expresión actual."""
        self._digito =  self._digito + str(n)
        self._calculo.set(self._digito)

    def _operacion_especial(self, tipo:str = "igual"):
        """
        Maneja operaciones complejas y evaluación de resultados.
        Incluye manejo centralizado de excepciones (ZeroDivision, Syntax, etc).
        """
        if not self._digito: return # no hace nada

        try:
            valor_float = float(eval(self._digito))
            if tipo == "raiz":
                if valor_float < 0: raise ValueError("Raíz Negativa")
                res = valor_float ** 0.5
            elif tipo == "cuadrado":
                res = valor_float ** 2
            elif tipo == "inverso":
                res = 1 / valor_float
            elif tipo == "igual":
                res = eval(self._digito)
            
            # Actualizamos estado
            resultado_str = str(res)
            self._digito = resultado_str
            self._calculo.set(resultado_str)
            
        except ZeroDivisionError:
            self._manejar_error("No se puede dividir por 0")
            
        except SyntaxError:
            self._manejar_error("Error de sintaxis")
            
        except Exception:
            self._manejar_error("Operación inválida")

        
    def _manejar_error(self, mensaje:str):
        self._calculo.set(mensaje)
        self._digito = ""

    def _limpiar_completo(self):
        self._digito = ""
        self._calculo.set("")

    def _borrar_ultimo(self):
        self._digito = self._digito[:-1]
        self._calculo.set(self._digito) 


if __name__ == "__main__":
    root = Tk()
    app = Calculadora(root)
    root.mainloop()