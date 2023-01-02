import dict_manager
import config

def command_searcher(structure, message_words_list):
    '''Recursive function that joins in the commands dict and return the selected function'''

    if not len(message_words_list):
        return config.NOT_FOUND_COMMAND

    key = message_words_list[0][1:] if message_words_list[0].startswith(">") else message_words_list[0]

    if key not in structure:
        return config.NOT_FOUND_COMMAND

    if isinstance(structure[key], tuple):
        return structure[key]

    return command_searcher(structure[key], message_words_list[1:])


def read(message):
    '''This function gets a user message and process it'''

    message_words_list = str(message.content).split()

    # Getting the user privileges
    is_admin = 1 if (rol.name in dict_manager.get_guild_conf(message)["admins_rol"] for rol in message.author.roles) else 0
    is_assistant = 1 if (rol.name in dict_manager.get_guild_conf(message)["assistans_rol"] for rol in message.author.roles) else 0

    fun_tuple = command_searcher(config.COMMANDS, message_words_list)

    # The base function to execute, that will change for the selected function
    admin, assistant, fun = config.NOT_FOUND_COMMAND

    if fun_tuple:
        admin, assistant, fun = fun_tuple

    if is_admin < admin or is_assistant < assistant:
        return

    return fun(message)