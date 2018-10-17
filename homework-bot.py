
import discord


client = discord.Client()
token = open("token.txt", "r").read()




# runs the bot
client.run(token)