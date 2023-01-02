from commands import configuration, help, questions
import os

# Channels configuration
QUESTIONS_CHANNEL = "turing-bot"

# Path constants
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(ROOT_PATH, "data")

GUILD_FOLDERS_SYSTEM = [
    ["questions", 
        [
            ["answered", []]
        ]
    ]
]

# If the reply type is sent privately or in the same channel
message_privacy = {
    "question": False,
    "help": False,
    "config": False
}

# The command tree, the tuples follows the next order: (ADMIN PRIVILEGES, ASSISTAND PRIVILEGES, FUNCTION)
COMMANDS = {
    "ayuda": (0, 0, help.help),
    "pregunta": (0, 0, questions.new_ask),
    "config": {
        "canales": {
            "cambiar_preguntas": None, #To implement
            "default_preguntas": None #To implement
        },
        "roles": {
            "ver": (1, 0, configuration.get_roles),
            "seleccionar": {
                "admin": None, #To implement
                "ayudantes": None, #To implement
                "usuarios": None, #To implement
            },
            "borrar": {
                "admin": None, #To implement
                "ayudantes": None, #To implement
                "usuarios": None, #To implement
            }
        }
    }
}

NOT_FOUND_COMMAND = (0, 0, help.not_exist)