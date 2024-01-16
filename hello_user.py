# Nome do autor: Walter Souza - Full-Stack
# Data: 16:01:2024


import getpass

user_name = input("Por favor, Digite seu nome: ")

system_user = getpass.getuser()
print(f"Olá, {user_name}! Seu nome de usuario do sistema é {system_user}.")
