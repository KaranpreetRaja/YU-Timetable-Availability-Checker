import os
import discord
import re
from dotenv import load_dotenv
from discord.ext import commands
import pickle

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_message(message):
    print("Message recieved by bot")
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send("Hello!")

    if message.content.startswith('!addWaitlist'):
        pattern = r'!command\s+(.+)'
        match = re.search(pattern, message.content)

        if match:
            course = match.group(1)
            user = message.author.id
            print(f"Course: {course} User: {user}")


client.run(token)
        

    
    


