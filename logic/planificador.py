from scraping.market_scraper import obtener_productos_condis

def generar_plan(presupuesto, filtros):
    productos_scrapeados = obtener_productos_condis()

    # parse prices into floats
    productos = []
    for p in productos_scrapeados:
        try:
            precio_float = float(p["precio"].replace("€", "").replace(",", "."))
            productos.append({"producto": p["nombre"], "precio": precio_float})
        except:
            continue

    total = 0
    seleccionados = []
    for p in productos:
        if total + p["precio"] <= presupuesto:
            seleccionados.append(p)
            total += p["precio"]

    resultado = "Productos seleccionados:\n"
    for p in seleccionados:
        resultado += f"- {p['producto']} ({p['precio']} €)\n"
    resultado += f"\nTotal: {round(total, 2)} €"
    return resultado
