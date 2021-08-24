# Importar modulos
from random import choice


# Adiciona salt aos dados
def protect(message, salt):
    # Variaveis
    eData = ''
    salt = list(salt)
    saltChars = []

    # Adiciona salt a lista de caracteres
    for char in message:
        if not char in saltChars:
            saltChars.append(char)

    # Adiciona salt a menssagem
    for index, secretChar in enumerate(message):
        for _ in range(int(salt[index])):
            eData += choice(saltChars)
        eData += secretChar

    return eData


# Remove salt dos dados
def unprotect(message, salt):
    # Variables
    p = 0
    dData = ''

    # Remove os caracteres salt a string
    for secretSalt in salt:
        message = message[int(secretSalt) + p:]
        # If not data - stop
        if not message:
            break

        dData += message[0]
        p = 1

    return dData
