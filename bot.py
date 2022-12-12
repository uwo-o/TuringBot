from dotenv import load_dotenv
import discord
import responses
import config
import shutil
import json
import os

# We load the .env file that is located in root path
load_dotenv()

message_privacy = config.message_privacy

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
    

async def send_message(message, response:str, is_private:bool):
    '''
    This function send a message to the user that runs a command
    The behavior is different, it has two options, private message
    or a message in the same channel that the command was called
    '''
    
    try:
        await message.author.send(response) if is_private else await message.channel.send(response)
     
    except Exception as e:
        print(e)

def run():
    '''
    This function turn on the bot, call the API to authenticate, and start to work
    '''
    client = discord.Client(intents=discord.Intents.all())

    # Feedback to know that all is going good
    @client.event
    async def on_ready():
        print(f'{client.user} En servicio!')

    @client.event
    async def on_guild_join(server):
        if str(server.id) not in [folder for folder in os.listdir(config.DATA_PATH) if os.path.isdir(config.DATA_PATH+folder)]:
            folder_system_generator(os.path.join(config.DATA_PATH, str(server.id)), config.GUILD_FOLDERS_SYSTEM)
        create_guild_conf_file(server)
    
    # When a message is sent we process it    
    @client.event
    async def on_message(message):
        
        # If the message was sent by the bot it is ignored
        if message.author == client.user:
            return
        
        # And the same idea when the message hasn't the command key
        if str(message.content[0]) != ">":
            return
        
        username = str(message.author.display_name)
        user_message = str(message.content[1:])
        channel =  str(message.channel)

        # Calls the function that proccess the response in base to the command initiated
        response = responses.handle_message(message, user_message)
        
        await send_message(message, response["message"], is_private=message_privacy[response["id"]])

    @client.event
    async def on_guild_remove(server):
        shutil.rmtree(os.path.join(config.DATA_PATH, str(server.id)))

    client.run(os.getenv('TOKEN'))