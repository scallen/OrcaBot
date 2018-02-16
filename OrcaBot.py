#OrcaBot by Scallen

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import OrcaConfig

bot = commands.Bot(command_prefix = '!')

#Displays Logging in messages
@bot.event
async def on_ready():
    print('Logging in to Discord')
    print("My name is " + bot.user.name)
    print("With the ID: " + bot.user.id)

#!info command displays users name, status, and when it joined the server
@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    """displays a users info"""
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what we know:", color=0x040c30)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="status", value=user.status, inline=True)
    embed.add_field(name="Joined", value=user.joined_at, inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)
    
#!dnd has links to the readme, phb, roll20 campaign
#Old Format: #embed.add_field(name="Readme", value="[Click on me!](LINK)", inline=False)
@bot.command(pass_context=True)
async def dnd(ctx):
    """has a collection of links to help out our roll20 campaign"""
    embed=discord.Embed(title="DND Links", url="https://docs.google.com/document/d/1ZpodR2KdgA-BPQdYwoeiewuONXkjLt3vMwlK6JHzB_o/edit", description="The Readme is really useful!", color=0x80ff80)
    embed.set_thumbnail(url="https://www.guerrillatees.com/media/thumbs/run-dnd-thumb-1.jpg")
    embed.add_field(name="-----", value="[Readme!](https://docs.google.com/document/d/1ZpodR2KdgA-BPQdYwoeiewuONXkjLt3vMwlK6JHzB_o/edit)", inline=False)
    embed.add_field(name="-----", value="[Players Hand Book!](https://drive.google.com/file/d/0ByQPYPddGJI2RmppdzZWRnF5RHc/view)", inline=False)
    embed.add_field(name="-----", value="[Roll20 Campaign!](https://app.roll20.net/campaigns/details/422318/the-unknown-frontier)", inline=False)
    embed.add_field(name="-----", value="[Combat Chart (Simple)!](https://i.imgur.com/PngILDk.jpg)", inline=False)
    embed.add_field(name="-----", value="[Combat Explanation (Complex)](https://roll20.net/compendium/dnd5e/Combat#content)", inline=False)
    embed.set_footer(text="When in doubt, check the Readme")
    await bot.say(embed=embed)
    
#Bard stuff goes here.  Info on subcommands can be found here: https://twentysix26.github.io/Red-Docs/red_guide_subcommands/
#Basically the main command is @bot.group() async def COMMAND and the subcommands are @COMMAND.command() async def SUBCOMMAND
@bot.group(pass_context=True)
async def bard(ctx):
    if ctx.invoked_subcommand is None:
        embed=discord.Embed(title="BARD", url="https://docs.google.com/document/d/1ZpodR2KdgA-BPQdYwoeiewuONXkjLt3vMwlK6JHzB_o/edit#bookmark=id.h49uu4x6bsxp", description="\m/:kissing:\m/", color=0xff00ff)
        embed.set_thumbnail(url="https://tribality.com/wp-content/uploads/2015/02/bard-bagpipes-240x300.jpg")
        embed.add_field(name="-----", value="[Here's a link to the Bard PHB!](https://drive.google.com/file/d/0ByQPYPddGJI2RmppdzZWRnF5RHc/edit?disco=AAAABqEtInM)", inline=False)
        embed.add_field(name="-----", value="[Here's a list of Bard Spells!](https://roll20.net/compendium/dnd5e/Bard%20Spells%20by%20Level#content)", inline=False)
        await bot.say(embed=embed)
#Subcommand formats in case some are added later
#@bard.command()
#async def SUBCOMMAND():

bot.run(OrcaConfig.token)
