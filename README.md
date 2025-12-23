# 🧮 Calculadora Python - Clean Code & UX

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Estado-Funcional-success?style=for-the-badge)

> Una calculadora de escritorio robusta, construida no solo para calcular, sino para demostrar buenas prácticas de programación, separación de responsabilidades y manejo de errores.

---

## 📸 Demo

![Captura de pantalla de la calculadora](screen-calculadora.png)


## 🚀 Características

Este proyecto va más allá de una calculadora básica, implementando lógica de **Backend** separada del **Frontend**:

* **Operaciones Básicas:** Suma, Resta, Multiplicación, División.
* **Funciones Científicas:**
    * Raíz Cuadrada (`√`).
    * Potencia al Cuadrado (`x²`).
    * Inverso Multiplicativo (`1/x`).
    * Constante PI (`π`).
* **Manejo de Errores Robusto:**
    * Detecta y avisa si intentas dividir por cero (`ZeroDivisionError`).
    * Captura errores de sintaxis matemática (`SyntaxError`).
    * Valida raíces negativas.
* **Experiencia de Usuario (UX):**
    * Función de borrado inteligente (carácter por carácter).
    * Interfaz limpia usando `Tkinter`.

## 🛠️ Tecnologías y Conceptos Aplicados

* **Lenguaje:** Python 3.14
* **Librería Gráfica:** Tkinter (Nativa).
* **Lógica Matemática:** Módulo `math` y función `eval()` controlada.
* **Principio DRY (Don't Repeat Yourself):** Centralización de la lógica de operaciones especiales en una única función manejadora para evitar redundancia de código.
* **Patrón de Diseño:** Separación básica entre la lógica de negocio (funciones de cálculo) y la capa de presentación (configuración de la ventana y widgets).

## 🔧 Instalación y Uso

Este proyecto no requiere librerías externas (como pandas o numpy), por lo que es muy ligero y fácil de ejecutar.

1.  **Clonar el repositorio:**
    ```bash
    git clone [TU_LINK_DEL_REPO_AQUI]
    ```

2.  **Navegar a la carpeta:**
    ```bash
    cd [NOMBRE_DE_LA_CARPETA]
    ```

3.  **Ejecutar:**
    ```bash
    python calculadora.py
    ```
    *(Asegúrate de que tu archivo principal tenga ese nombre o cámbialo en el comando)*

## 🧠 Lógica del Código

El núcleo del proyecto se basa en una función centralizada para el manejo de excepciones:

```python
# Ejemplo simplificado de la lógica interna
def operacion_especial(tipo):
    try:
        # Cálculo seguro
    except ZeroDivisionError:
        # Feedback al usuario
    except SyntaxError:
        # Feedback al usuario
