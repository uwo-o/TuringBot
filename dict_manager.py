import config
import json
import os

def get_questions_folder(server):
    '''
    This function gets a server and return the path of their questions folder
    '''
    return os.path.join(get_guild_folder(server), "questions")

def get_guild_folder(server):
    '''
    This function gets a server and return the path of their folder
    '''
    return os.path.join(config.DATA_PATH, str(server.id))

def create_guild_conf_file(server):
    with open(os.path.join(get_guild_folder(server),"guild.json"), "w") as config_file:
        json.dump({
            "id": str(server.id),
            "guild_name": str(server.name),
            "owner_id": str(server.owner_id),
            "owner": str(server.owner),
            "admins_rol": [],
            "assistans_rol": [],
            "users_rol": [],
            "questions_channel": config.QUESTIONS_CHANNEL
        }, config_file)

def get_guild_conf(message):
    return json.load(open(os.path.join(get_guild_folder(message.guild),"guild.json")))

def folder_system_generator(root, folders):
    '''
    This function gets a root directory as a start point and a tree of lists of lists and strings where
    each string is the folder name and the next value in the list is another list that has the children.
    This way we can create a standard form to create every folder system.

    root --|---> child1 ---> []
           |---> child2 --|--> grandchild1 --> []
                          |--> grandchild1 --> []
    '''

    # We create the actual root
    os.mkdir(root)

    if not folders:
        return 0

    for name, children in folders:
        folder_system_generator(os.path.join(root, name), children)