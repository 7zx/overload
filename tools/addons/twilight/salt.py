# Importa os modulos
from random import choice


# Add salt to data
def protect(message, salt):
    # Variables
    eData = ''
    salt = list(salt)
    saltChars = []

    # Adiciona salt á lista de caracteres
    for char in message:
        if not char in saltChars:
            saltChars.append(char)

    # Adiciona salt á menssagem
    for index, secretChar in enumerate(message):
        for _ in range(int(salt[index])):
            eData += choice(saltChars)
        eData += secretChar

    return eData


# Remove salt da data
def unprotect(message, salt):
    # Variables
    p = 0
    dData = ''

    # Remove os caracteres salt da string
    for secretSalt in salt:
        message = message[int(secretSalt) + p:]
        # If not data - stop
        if not message:
            break

        dData += message[0]
        p = 1

    return dData
