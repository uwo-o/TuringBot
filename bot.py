from dotenv import load_dotenv
import responses
import discord
import os

load_dotenv()

async def send_message(message, user_message, is_private):

    try:
        response = responses.handle_message(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run():
    
    client = discord.Client()

    

    client.run(os.environ('TOKEN'))