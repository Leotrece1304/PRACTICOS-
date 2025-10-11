def redondear(numero):
    parte_entera = int(numero)
    parte_decimal = numero - parte_entera

    if parte_decimal >= 0.5:
        return parte_entera + 1
    else:
        return parte_entera
    
