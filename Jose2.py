import flet as ft

tasas_conversion = {
    ("USD", "PYG"): 7250,   # 1 USD = 7250 PYG (tasa de cambio estimada)
    ("PYG", "USD"): 0.00014,  # 1 PYG = 0.00014 USD
    ("USD", "EUR"): 0.85,   # 1 USD = 0.85 EUR (tasa de cambio estimada)
    ("EUR", "USD"): 1.18,   # 1 EUR = 1.18 USD
    ("PYG", "EUR"): 0.00012, # 1 PYG = 0.00012 EUR
    ("EUR", "PYG"): 8400,   # 1 EUR = 8400 PYG
}

# Función para realizar la conversión de monedas
def convertir_monedas(cantidad, moneda_origen, moneda_destino):
    try:
        cantidad = float(cantidad)
        if cantidad <= 0:
            return "La cantidad debe ser positiva."

        if moneda_origen == moneda_destino:
            return f"No es necesario convertir {cantidad:.2f} {moneda_origen} a {moneda_destino}."

        # Buscar la tasa de conversión
        tasa = tasas_conversion.get((moneda_origen, moneda_destino))
        if tasa is None:
            return "No se encontró la tasa de conversión para estas monedas."

        cantidad_convertida = cantidad * tasa
        return f"{cantidad:.2f} {moneda_origen} son {cantidad_convertida:.2f} {moneda_destino}."
    
    except ValueError:
        return "Por favor, introduce una cantidad válida."

# Función que se activa al hacer clic en 'Convertir'
def convertir_click(e, page):
    cantidad = cantidad_input.value
    moneda_origen = moneda_origen_input.value
    moneda_destino = moneda_destino_input.value

    if not cantidad or not moneda_origen or not moneda_destino:
        resultado_text.value = "Por favor, completa todos los campos."
    else:
        resultado_text.value = convertir_monedas(cantidad, moneda_origen, moneda_destino)

    page.update()

# Función que se activa al hacer clic en 'Limpiar'
def limpiar_click(e, page):
    cantidad_input.value = ""
    moneda_origen_input.value = ""
    moneda_destino_input.value = ""
    resultado_text.value = ""
    page.update()

# Función para mostrar la ventana principal del conversor de monedas
def mostrar_conversor(page):
    global cantidad_input, moneda_origen_input, moneda_destino_input, resultado_text

    # Limpiar la ventana actual
    page.controls.clear()

    # Crear elementos del conversor
    cantidad_input = ft.TextField(label="Cantidad", width=300, keyboard_type=ft.KeyboardType.NUMBER)
    moneda_origen_input = ft.Dropdown(
        label="Moneda de origen",
        options=[
            ft.dropdown.Option("USD"),
            ft.dropdown.Option("EUR"),
            ft.dropdown.Option("PYG")
        ],
        width=300,
    )
    moneda_destino_input = ft.Dropdown(
        label="Moneda de destino",
        options=[
            ft.dropdown.Option("USD"),
            ft.dropdown.Option("EUR"),
            ft.dropdown.Option("PYG")
        ],
        width=300,
    )
    resultado_text = ft.Text()

    # Botón de "Convertir" con sombra y bordes redondeados
    convertir_boton = ft.ElevatedButton(
        text="Convertir", 
        on_click=lambda e: convertir_click(e, page), 
        bgcolor=ft.colors.GREEN_700, 
        color=ft.colors.WHITE,
        elevation=5,
    )
    
    # Botón de "Limpiar" con sombra y bordes redondeados
    limpiar_boton = ft.ElevatedButton(
        text="Limpiar", 
        on_click=lambda e: limpiar_click(e, page), 
        bgcolor=ft.colors.RED_700, 
        color=ft.colors.WHITE,
        elevation=5,
    )

    # Panel de entrada y botones, con sombras y bordes redondeados
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text("Conversor de Monedas", style="headlineMedium", text_align="center", color=ft.colors.BLUE_900),
                    cantidad_input,
                    moneda_origen_input,
                    moneda_destino_input,
                    ft.Row([convertir_boton, limpiar_boton], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                    resultado_text,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=20,
            width=400,
            border_radius=ft.border_radius.all(15),
            shadow=ft.BoxShadow(blur_radius=15, spread_radius=1, color=ft.colors.with_opacity(ft.colors.BLACK, 0.25)),
            alignment=ft.alignment.center,
        )
    )
    page.update()

# Función que se activa cuando el usuario acepta los términos
def aceptar_terminos(e, page):
    # Redirigir a la ventana principal del conversor de monedas
    mostrar_conversor(page)

# Ventana de bienvenida
def main(page: ft.Page):
    page.title = "Bienvenido al Conversor de Monedas"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Crear ventana de bienvenida con borde redondeado y sombra
    bienvenida_text = ft.Text("¡Bienvenido al Conversor de Monedas!", style="headlineMedium", text_align="center", color=ft.colors.YELLOW_800)
    terminos_text = ft.Text("Al usar esta app, aceptas nuestros términos y condiciones.", text_align="center", color=ft.colors.BLUE_800)
    aceptar_boton = ft.ElevatedButton(
        text="Aceptar y Continuar", 
        on_click=lambda e: aceptar_terminos(e, page), 
        bgcolor=ft.colors.BLUE_700, 
        color=ft.colors.WHITE,
        elevation=5,  # Quitamos el argumento 'shape'
    )

    # Contenedor de bienvenida con bordes redondeados y sombra
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    bienvenida_text,
                    terminos_text,
                    aceptar_boton,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=40,
            width=400,
            border_radius=ft.border_radius.all(15),
            shadow=ft.BoxShadow(blur_radius=15, spread_radius=1, color=ft.colors.with_opacity(ft.colors.BLACK, 0.25)),
            alignment=ft.alignment.center,
        )
    )

# Iniciar la aplicación
ft.app(target=main)
