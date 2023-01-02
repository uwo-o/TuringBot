import config

def get_not_found_command(structure, message_words_list):

    key = message_words_list[0][1:] if message_words_list[0].startswith(">") else message_words_list[0]
        
    if key not in structure:
        return key

    return get_not_found_command(structure[key], message_words_list[1:])

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
`[Ejemplo] >pregunta Es esto realmente un ejemplo?`
"""
}

def not_understood(message):
    return {"id": "help",
        "message": f"Hola! **{message.author.display_name}** creo que entendiste mal :c\nDonde escribiste **comando** debe ir al comando que quieras que ejecute :D\nPuedes ver un listado con el usando el comando: **ayuda**."
}

def not_exist(message):

    command = get_not_found_command(config.COMMANDS, str(message.content).split())

    return {
        "id": "help",
        "message": f"Hola! **{message.author.display_name}**, creo que te has equivocado :c\nLamentablemente no reconozco el comando **{command}**.\nPuedes revisar la lista de todos los comandos con sus respectivas instrucciones con el siguiente commando: **ayuda**."
    }