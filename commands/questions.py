import dict_manager
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
    
    with open(f"{os.path.join(dict_manager.get_questions_folder(message.guild), str(message.created_at))}.json", "w") as file:
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