# Funciones útiles (ej. limpiar texto, convertir precios, etc.)
def limpiar_precio(precio_str):
    return float(precio_str.replace("€", "").replace(",", ".").strip())
