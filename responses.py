import config
import json
import os

def new_ask(message):
    '''
    This function generate a JSON file to storage the data for each question,
    it is only to prevent lost questions if some problem appear
    '''

    questions_channel = config.QUESTIONS_CHANNEL

    # If the message channel is not the designe to questions, returns error.
    if str(message.channel) != questions_channel:
        return {
            "id": "question",
            "message": f"Solo es posible crear preguntas dentro del canal: **{questions_channel}**"
            }

    # If the question doesn't contain text, returns error.
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

    # It counts how many questions there are to set a position in the line.
    position = len([file for file in os.listdir(config.QUESTIONS_PATH) if os.path.isfile(config.QUESTIONS_PATH+file)])

    # Feedback
    return {
        "id": "question",
        "message": f"**[Turno: {str(position)}] {str(message.author.display_name)}** tu pregunta ha sido creada exitosamente!"
    }

def help(message):
    return {
        "id": "help",
        "message": f"""Hola! **{message.author.display_name}** soy **TuringBot**, me encargo de ayudar a administrar el lugar :D
Puedes interactuar conmigo usando los comandos, estos al ser llamados deben empezar con el simbolo: '>'.

De la foma:
`>comando`

**Esta es la lista de los comandos:**

**Pregunta:**
`>pregunta PREGUNTA`. Con este comando puedes crear preguntas dentro del canal designado.
Se creara una lista de espera, para que los y las ayudantes puedan responder a estas en orden de llegada.
Cuando su pregunta sea respondida yo me encargare de avisate :D
`Ejemplo: >pregunta Es esto realmente un ejemplo?`
"""
}


'''
This dictionary has the avalaibles commands as key and their
respective function as value.
'''
command_list = {
    "pregunta": new_ask,
    "ayuda": help
}

def handle_message(message, user_message:str):
    
    command = user_message.split()[0]
    
    if command not in command_list:
        return {
            "id": "help",
            "message": f"Hola! **{message.author.display_name}** creo que te has equivocado :c\nLamentablemente no reconozco el comando **{command}**.\nPuedes revisar la lista de todos los comandos con sus respectivas instrucciones con el siguiente commando: **ayuda**."
        }

    return command_list[command](message)