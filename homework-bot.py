# version 0.1 of homework-bot

import discord
import instruct

client = discord.Client()
token = open("token.txt", "r").read()



@client.event
async def on_ready():
    print(f"Logged in as {client.user} ")

@client.event
async def on_message(message):
    channel = message.channel

    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.author.bot:
        return
    # prints commands
    if "!help" == message.content:
        await channel.send(instruct.print_help())
    elif message.content.startswith('!ass'):
        #homework_channel = client.get_channel(491093305883623434)
        #await homework_channel.send("plop")
        await channel.send(instruct.print_assignment(message.content))
        # if it returned no hmwk, then delete after a couple seconds


# runs the bot
client.run(token)