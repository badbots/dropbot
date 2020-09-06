import discord
import os
from dotenv import load_dotenv
from circle_drawer import draw_circle
load_dotenv()

TOKEN = os.getenv('TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('🪂'):
        image_file = draw_circle('maps/map.png', 'maps/mask.bmp')
        await message.channel.send(file=image_file)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)