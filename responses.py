import configparser
import json
import os

def new_ask(message):

    config_parser = configparser.ConfigParser.read(open(os.path.dirname(os.path.abspath(__file__)+".conf")))

    questions_channel = config_parser.get("GLOBAL", "QUESTIONS_CHANNEL")

    if message.channel != questions_channel:
        return "Solo es posible crear preguntas dentro del canal: **"+questions_channel+"**"

    question = " ".join(message.split()[1:])
    return json.dumps({
        "id": "question",
        "status": 0,
        "created_at": message.created_at,
        "user": message.display_name,
        "question": question,
        "answered_by": ""
    }, indent=4)


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
    "pregunta": new_ask,
    "ayuda": 0
}

def handle_message(message:str):
    
    command = message.split(" ")[0]
    
    if command not in command_list:
        return f"El comando '{command}' no existe. Para conocer los comandos utilice >ayuda"

    return command_list[command](message)