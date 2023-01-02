from dotenv import load_dotenv
import command_manager
import dict_manager
import discord
import config
import shutil
import os

# We load the .env file that is located in root path
load_dotenv()

message_privacy = config.message_privacy

async def get_guild_roles_list(message):
    '''
    This function gets a message and returns the roles in the guild
    as a list.
    '''
    return await message.guild.roles
    
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
            dict_manager.folder_system_generator(os.path.join(config.DATA_PATH, str(server.id)), config.GUILD_FOLDERS_SYSTEM)
        dict_manager.create_guild_conf_file(server)
    
    # When a message is sent we process it    
    @client.event
    async def on_message(message):
        
        # If the message was sent by the bot it is ignored
        if message.author == client.user:
            return
        
        # And the same idea when the message hasn't the command key
        if not str(message.content).startswith(">"):
            return
        
        username = str(message.author.display_name)
        user_message = str(message.content[1:])
        channel =  str(message.channel)

        # Calls the function that proccess the response in base to the command initiated
        response = command_manager.read(message)
        
        await send_message(message, response["message"], is_private=message_privacy[response["id"]])

    @client.event
    async def on_guild_remove(server):
        shutil.rmtree(os.path.join(config.DATA_PATH, str(server.id)))

    client.run(os.getenv('TOKEN'))