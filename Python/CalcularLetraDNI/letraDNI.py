def calcularLetraDNI(dni):
    calLetra= str(dni)
    if len(calLetra) !=8:
        print("El dni debe tener 8 dígitos.")
    else:
        Opciones_Letras_DNI ='TRWAGMYFPDXBNJZSQVHLCKE'
        return f"{dni}{Opciones_Letras_DNI[int(dni)%23]}"

inputDNI=input("Indique el número de DNI a calcular la letra:\n ")

print("El DNI completo con la letra es: "+calcularLetraDNI(inputDNI))
    