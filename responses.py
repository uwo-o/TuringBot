import config
import json
import os

def new_ask(message):

    questions_channel = config.QUESTIONS_CHANNEL

    if str(message.channel) != questions_channel:
        return {
            "id": "question",
            "message": f"Solo es posible crear preguntas dentro del canal: **{questions_channel}**"
            }

    if len(str(message.content).split()) == 1:
        return {
            "id": "question",
            "message": f"**{str(message.author.display_name)}** debes escribir tu pregunta luego del comando, de la forma:\n`>pregunta Esto es realmente un ejemplo?`"
        }

    question = " ".join(str(message.content).split()[1:])
    
    with open(f"{config.QUESTIONS_PATH}{str(message.created_at)}.json", "w") as file:
        json.dump({
            "id": "question",
            "status": 0,
            "created_at": str(message.created_at),
            "user": str(message.author.display_name),
            "question": question,
            "answered_by": ""
        }, file)

    position = len([file for file in os.listdir(config.QUESTIONS_PATH) if os.path.isfile(config.QUESTIONS_PATH+file)])

    return {
        "id": "question",
        "message": f"**[Turno: {str(position)}] {str(message.author.display_name)}** tu pregunta ha sido creada exitosamente!"
    }


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

def handle_message(message, user_message:str):
    
    command = user_message.split()[0]

    print(config.ROOT_PATH, config.QUESTIONS_PATH)
    
    if command not in command_list:
        return f"El comando '{command}' no existe. Para conocer los comandos utilice >ayuda"

    return command_list[command](message)