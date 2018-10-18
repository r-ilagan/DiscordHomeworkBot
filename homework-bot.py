# version 0.1 of homework-bot

import discord
import commands

client = discord.Client()
token = open("token.txt", "r").read()


@client.event
async def on_ready():
    print(f"Logged in as {client.user} ")

@client.event
async def on_message(message):
    channel = message.channel

    # prints commands
    if "!help" == message.content:
        await channel.send(commands.print_help())



# runs the bot
client.run(token)