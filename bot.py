from dotenv import load_dotenv
from discord.ext import commands
import discord
import responses
import os

# We load the .env file that is located in root path
load_dotenv()


async def send_message(message, user_message:str, is_private:bool):
    '''
    This function send a message to the user that runs a command
    The behavior is different, it has two options, private message
    or a message in the same channel that the command was called
    '''
    
    try:
        
        # Calls the function that proccess the response in base to the commant initiated
        response = responses.handle_message(user_message)
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
    
    # When a message is sent we process it    
    @client.event
    async def on_message(message):
        
        # If the message was sent by the bot it is ignored
        if message.author == client.user:
            return
        
        # And the same idea when the message hasn't the command key
        if str(message.content[0]) != ">":
            return
        
        username = str(message.author)
        user_message = str(message.content[1:])
        channel =  str(message.channel)
        
        await send_message(message, user_message, is_private=False)

    client.run(os.getenv('TOKEN'))