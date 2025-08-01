def aplicar_filtros(productos, filtros):
    filtrados = []
    for producto in productos:
        if filtros["proteina"] and producto["categoria"] == "proteina":
            filtrados.append(producto)
        if filtros["lacteos"] and producto["categoria"] == "lacteo":
            filtrados.append(producto)
        if filtros["verduras"] and producto["categoria"] == "verdura":
            filtrados.append(producto)
    return filtrados
