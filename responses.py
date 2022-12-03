'''
This dictionary has the avalaibles commands as key and an integer
as value, the value represent:
1: Admin command
0: Members command
'''
command_list = {
    "crear_evento": 1,
    "ver_eventos": 1,
    "entrar_evento": 0,
    "ayuda": 0
}

def handle_message(message:str):
    
    command = message.split(" ")[0]
    
    if command not in command_list:
        return f"El comando '{command}' no existe. Para conocer los comandos utilice >ayuda"