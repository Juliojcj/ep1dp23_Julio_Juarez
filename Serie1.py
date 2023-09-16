def ingresartext(numerotext):
    while True:
        texto = input(f"Ingrese el Texto {numerotext}: ")
        if len(texto.strip()) == 0:
            print("El texto no puede estar vacío. Intente de nuevo.")
        else:
            return texto


texto1 = ingresartext(1)
texto2 = ingresartext(2)
texto3 = ingresartext(3)
texto4 = ingresartext(4)

longitudes = [len(texto1), len(texto2), len(texto3), len(texto4)]
if len(set(longitudes)) != 4:
    print("Las longitudes de los textos deben ser distintas.")
else:

    suma_longitudes = sum(longitudes)

    texto_mas_largo = max([(texto1, len(texto1)), (texto2, len(texto2)), (texto3, len(texto3)), (texto4, len(texto4))], key=lambda x: x[1])

    promedio_longitudes = suma_longitudes / 4

    suma_segundo_y_cuarto = len(texto2) + len(texto4)

    print(f"La suma de todas las longitudes es: {suma_longitudes}")
    print(f"El texto con la mayor cantidad de caracteres es: '{texto_mas_largo[0]}' con {texto_mas_largo[1]} caracteres.")
    if promedio_longitudes > suma_segundo_y_cuarto:
        print("El promedio de las longitudes es mayor que la suma de las longitudes del segundo y cuarto texto.")
    elif promedio_longitudes < suma_segundo_y_cuarto:
        print("El promedio de las longitudes es menor que la suma de las longitudes del segundo y cuarto texto.")
    else:
        print("El promedio de las longitudes es igual a la suma de las longitudes del segundo y cuarto texto.")