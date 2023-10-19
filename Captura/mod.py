# Abre el archivo de entrada para lectura en modo binario y especifica la codificación
with open('rockyou.txt', 'rb') as file:
    # Lee todas las contraseñas en una lista, eliminando líneas en blanco
    passwords = [line.decode('latin-1').strip() for line in file.readlines() if line.strip()]

# Filtra las contraseñas que no comienzan con un número
passwords = [password for password in passwords if password and not password[0].isdigit()]

# Modifica las contraseñas y las almacena en una nueva lista
modified_passwords = [password[0].capitalize() + password[1:] + '0' for password in passwords]

# Guarda las contraseñas modificadas en un nuevo archivo
with open('rockyou_mod.dic', 'w') as file:
    file.write('\n'.join(modified_passwords))

# Imprime la cantidad de contraseñas en el archivo modificado
print(f'Se han modificado {len(modified_passwords)} contraseñas y se han guardado en "rockyou_mod.dic".')
