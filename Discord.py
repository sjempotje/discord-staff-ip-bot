import discord
import os
import random
from discord.ext import commands

PREFIX = "/"

bot = commands.Bot(command_prefix=PREFIX)

TOKEN = 'Enter token in here!'
SERVER = "Your server name here"
IP = "ip of the server"

##bot made by ItsJeBoyGoogle

print("Bot Connected")
print("Thank you for using my bot :D")


@bot.command()
async def staff(ctx):
    embed=discord.Embed(title=SERVER +" " + "Staff team", description="Here is the " + SERVER + " staff team", color=0x39aa31)
    embed.add_field(name="Owner", value="Name1", inline=True)
    embed.add_field(name="Co-Owner", value="Name1, Name2", inline=False)
    embed.add_field(name="Admin", value="Name, Name2, Name3", inline=True)
    embed.set_footer(text="Made by: ItsJeBoyGoogle")
    await ctx.send(embed=embed)
    
@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return
    
    msg_content = message.content.lower()
        
    ip = ['ip', 'IP']

    if any(word in msg_content for word in ip):
        await message.channel.send(IP)   
    await bot.process_commands(message)

bot.run(TOKEN)
