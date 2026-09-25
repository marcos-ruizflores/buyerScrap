# Small helpers (text cleanup, price parsing, etc.)
def limpiar_precio(precio_str):
    return float(precio_str.replace("€", "").replace(",", ".").strip())
