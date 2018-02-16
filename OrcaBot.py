#OrcaBot by Scallen

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import config

bot = commands.Bot(command_prefix = '!')

#Displays Logging in messages
@bot.event
async def on_ready():
    print('Logging in to Discord')
    print("My name is " + bot.user.name)
    print("With the ID: " + bot.user.id)
    
#!help command displays users name, status, and when it joined the server
#@bot.command(pass_context=True)
#async def help(ctx):
#    await bot.say("Hi! I'm Orca Bot and I'm here to help!  My current commands are !dnd and !info")

#!info command displays users name, status, and when it joined the server
@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    """!info displays a user's name, ID, status, and joined_at as well as displaying their avatar.  e.g. !info @thegibb"""
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what we know:", color=0x040c30)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="status", value=user.status, inline=True)
    embed.add_field(name="Joined", value=user.joined_at, inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)
    
#!dnd has links to the readme, phb, roll20 campaign
@bot.command(pass_context=True)
async def dnd(ctx):
    """!dnd has a collection of links to help out our roll20 campaign"""
    embed=discord.Embed(title="DND Links", url="https://docs.google.com/document/d/1ZpodR2KdgA-BPQdYwoeiewuONXkjLt3vMwlK6JHzB_o/edit", description="The Readme is really useful!", color=0x80ff80)
    embed.set_thumbnail(url="https://www.guerrillatees.com/media/thumbs/run-dnd-thumb-1.jpg")
    embed.add_field(name="Readme", value="[Click on me!](https://docs.google.com/document/d/1ZpodR2KdgA-BPQdYwoeiewuONXkjLt3vMwlK6JHzB_o/edit)", inline=False)
    embed.add_field(name="Players Hand Book", value="[Click on me!](https://drive.google.com/file/d/0ByQPYPddGJI2RmppdzZWRnF5RHc/view)", inline=False)
    embed.add_field(name="Roll20 Campaign", value="[Click on me!](https://app.roll20.net/campaigns/details/422318/the-unknown-frontier)", inline=False)
    embed.add_field(name="Combat Chart (Simple)", value="[Click on me!](https://i.imgur.com/PngILDk.jpg)", inline=False)
    embed.add_field(name="Combat Explanation (Complex)", value="[Click on me!](https://roll20.net/compendium/dnd5e/Combat#content)", inline=False)
    embed.set_footer(text="When in doubt, check the Readme")
    await bot.say(embed=embed)
    
#Bard stuff goes here.  Info on subcommands can be found here: https://twentysix26.github.io/Red-Docs/red_guide_subcommands/
#Basically the main command is @bot.group() async def COMMAND and the subcommands are @COMMAND.command() async def SUBCOMMAND
@bot.group(pass_context=True)
async def bard(ctx):
    if ctx.invoked_subcommand is None:
        await bot.say('Plays instruments to channel magic... or something like that')

@bard.command()
async def push(remote: str, branch: str):
    await bot.say('Pushing to {} {}'.format(remote, branch)
    
                  
                  
                  
#Displays current player names, race, and class
@bot.command(pass_context=True)
async def players(ctx, user: discord.Member):
      
                  https://s3.amazonaws.com/files.d20.io/images/47446235/0Vb9uAm7L3tLAkQi5i-_Ew/med.jpg?1518151527
    
bot.run(config.token)
