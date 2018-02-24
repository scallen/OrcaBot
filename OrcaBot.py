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
    
####[p]dnd has links to the readme, phb, roll20 campaign
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
    embed.add_field(name="-----", value="[Combat Actions (Illustrated)](https://crobi.github.io/dnd5e-quickref/preview/quickref.html)", inline=False)
    embed.set_footer(text="When in doubt, check the Readme")
    await bot.say(embed=embed)

####[p]combat
@bot.group(pass_context=True)
async def combat(ctx):
    if ctx.invoked_subcommand is None:
        embed=discord.Embed(title="Combat", url="https://crobi.github.io/dnd5e-quickref/preview/quickref.html", description="During your turn you can use **movement**, make one **action**, make one **bonus** action, make an **interaction**.  A **reaction** may occur during your turn or someone else's turn.", color=0xff0000)
        embed.add_field(name="Combat Steps", value="\n1) Determine Surprise\n2) Establish Positions\n3) Roll Initiative\n4) Take Turns\n5) Repeat 4 Until Combat is Concluded!", inline=False)
        embed.add_field(name="-----", value="[Combat Chart (Simple)!](https://i.imgur.com/PngILDk.jpg)", inline=False)
        embed.add_field(name="-----", value="[Combat Explanation (Complex)](https://roll20.net/compendium/dnd5e/Combat#content)", inline=False)
        embed.add_field(name="-----", value="[Combat Actions (Illustrated)](https://crobi.github.io/dnd5e-quickref/preview/quickref.html)", inline=False)
        await bot.say(embed=embed)

##[p]combat action
@combat.command(pass_context=True)
async def action(ctx):
        embed=discord.Embed(title="Combat Actions", url="https://crobi.github.io/dnd5e-quickref/preview/quickref.html", description="During your turn you may make ONE **action**:", color=0xff0000)
        embed.add_field(name="Attack", value="Melee or ranged attack", inline=False)
        embed.add_field(name="Cast a Spell", value="Assuming cast time of 1 action", inline=False)
        embed.add_field(name="Grapple", value="Attempt to latch onto a target", inline=False)
        embed.add_field(name="Shove", value="Attempt to push a target back one space", inline=False)
        embed.add_field(name="Dash", value="Double your movement speed", inline=False)
        embed.add_field(name="Disengage", value="Move without provoking opportunity attacks", inline=False)
        embed.add_field(name="Dodge", value="Attacks against you have disadvantage and you have advantage on dex saves", inline=False)
        embed.add_field(name="Escape", value="Attempt to escape a grapple using your Athletics or Acrobatics against their Athletics", inline=False)
        embed.add_field(name="Help", value="Grant an ally advantage", inline=False)
        embed.add_field(name="Hide", value="Make a Stealth check to attempt to become Hidden", inline=False)
        embed.add_field(name="Search", value="Attempt to find something", inline=False)
        embed.add_field(name="Use Class Feature", value="Some Class features use an action", inline=False)
        embed.add_field(name="Use Race Feature", value="Some Race features use an action", inline=False)
        embed.add_field(name="Improvise!", value="Any action not on the list", inline=False)
        embed.add_field(name="-----", value="[Combat Chart (Simple)!](https://i.imgur.com/PngILDk.jpg)", inline=False)
        embed.add_field(name="-----", value="[Combat Explanation (Complex)](https://roll20.net/compendium/dnd5e/Combat#content)", inline=False)
        embed.add_field(name="-----", value="[Combat Actions (Illustrated)](https://crobi.github.io/dnd5e-quickref/preview/quickref.html)", inline=False)
        await bot.say(embed=embed)

##[p]combat movement
@combat.command(pass_context=True)
async def movement(ctx):
        embed=discord.Embed(title="Combat Movement", url="https://crobi.github.io/dnd5e-quickref/preview/quickref.html", description="During your turn you may move your character as far as your **movement** speed allows (usually 30 feet / 6 squares).  \n\nYou may use all your movement in one go, or you may break it up between an action.  E.G. Move 10 feet north, then attack, then move 20 feet east", color=0xff0000)
        embed.add_field(name="-----", value="[Combat Chart (Simple)!](https://i.imgur.com/PngILDk.jpg)", inline=False)
        embed.add_field(name="-----", value="[Combat Explanation (Complex)](https://roll20.net/compendium/dnd5e/Combat#content)", inline=False)
        embed.add_field(name="-----", value="[Combat Actions (Illustrated)](https://crobi.github.io/dnd5e-quickref/preview/quickref.html)", inline=False)
        await bot.say(embed=embed)
        
##[p]combat interaction
@combat.command(pass_context=True)
async def interaction(ctx):
        embed=discord.Embed(title="Combat Interaction", url="https://crobi.github.io/dnd5e-quickref/preview/quickref.html", description="During your turn you may do an **interaction**:\n\nDraw or sheathe a weapon\nOpen or close a door\nWithdraw an item from your pack\nPick up a dropped or unattended item\nHand an item to another player\nThrow a lever or switch\nTurn a key in a lock\nPull the hood of your cloak up\nOther small actions", color=0xff0000)
        embed.add_field(name="-----", value="[Combat Chart (Simple)!](https://i.imgur.com/PngILDk.jpg)", inline=False)
        embed.add_field(name="-----", value="[Combat Explanation (Complex)](https://roll20.net/compendium/dnd5e/Combat#content)", inline=False)
        embed.add_field(name="-----", value="[Combat Actions (Illustrated)](https://crobi.github.io/dnd5e-quickref/preview/quickref.html)", inline=False)
        await bot.say(embed=embed)
        
##[p]combat reaction
@combat.command(pass_context=True)
async def reaction(ctx):
        embed=discord.Embed(title="Combat Reaction", url="https://crobi.github.io/dnd5e-quickref/preview/quickref.html", description="You only get ONE **reaction** per turn, however your reaction can be used during another creature's turn.  Your reaction can be used for an attack of opportunity or for various class features & spells that require a casting time of one reaction", color=0xff0000)
        embed.add_field(name="-----", value="[Combat Chart (Simple)!](https://i.imgur.com/PngILDk.jpg)", inline=False)
        embed.add_field(name="-----", value="[Combat Explanation (Complex)](https://roll20.net/compendium/dnd5e/Combat#content)", inline=False)
        embed.add_field(name="-----", value="[Combat Actions (Illustrated)](https://crobi.github.io/dnd5e-quickref/preview/quickref.html)", inline=False)
        await bot.say(embed=embed)
        
##[p]combat bonus
@combat.command(pass_context=True)
async def bonus(ctx):
        embed=discord.Embed(title="Combat Bonus Action", url="https://crobi.github.io/dnd5e-quickref/preview/quickref.html", description="Many Classes and Races feature **bonus** actions, however you only get to use ONE **bonus** action per turn", color=0xff0000)
        embed.add_field(name="Offhand Attack", value="Used while fighting with two weapons", inline=False)
        embed.add_field(name="Cast a Spell", value="Cast time of 1 bonus action", inline=False)
        embed.add_field(name="Use Class Feature", value="Some Class features use an bonus action", inline=False)
        embed.add_field(name="Use Race Feature", value="Some Race features use an bonus action", inline=False)
        embed.add_field(name="-----", value="[Combat Chart (Simple)!](https://i.imgur.com/PngILDk.jpg)", inline=False)
        embed.add_field(name="-----", value="[Combat Explanation (Complex)](https://roll20.net/compendium/dnd5e/Combat#content)", inline=False)
        embed.add_field(name="-----", value="[Combat Actions (Illustrated)](https://crobi.github.io/dnd5e-quickref/preview/quickref.html)", inline=False)
        await bot.say(embed=embed)

####Languages
@bot.group(pass_context=True)
async def languages(ctx):
    if ctx.invoked_subcommand is None:
        embed=discord.Embed(title="LANGUAGES", url="https://drive.google.com/file/d/0ByQPYPddGJI2RmppdzZWRnF5RHc/edit?disco=AAAABqE3c70", description=":lips:", color=0xCCCCCC)
        embed.add_field(name="Common Languages", value="```\nCommon\nDwarvish\nElvish\nGiant\nGnomish\nGoblin\nHalfing\nOrc```", inline=False)
        embed.add_field(name="Exotic Languages", value="```\nAbyssal\nCelestial\nDraconic\nDeep Speech\nInfernal\nPrimordial\nSylvan\nUndercommon```", inline=False)
        await bot.say(embed=embed)
    
##Classes
###Use !CLASSNAME to get an embed with links to class info.  
####Info on subcommands can be found here: https://twentysix26.github.io/Red-Docs/red_guide_subcommands/
#####Basically the main command is @bot.group() async def COMMAND and the subcommands are @COMMAND.command() async def SUBCOMMAND

#Artificer stuff goes here.
@bot.group(pass_context=True)
async def artificer(ctx):
    if ctx.invoked_subcommand is None:
        embed=discord.Embed(title="ARTIFICIER", url="https://docs.google.com/document/d/1ZpodR2KdgA-BPQdYwoeiewuONXkjLt3vMwlK6JHzB_o/edit#bookmark=id.v1a3tmxksgir", description=":tools:", color=0xCCCCCC)
        embed.set_thumbnail(url="http://www.dandwiki.com/w/images/thumb/5/5a/Steamborg_Gunslinger.jpeg/390px-Steamborg_Gunslinger.jpeg")
        embed.add_field(name="-----", value="[Here's a link to the Artificer Abilities!](https://drive.google.com/open?id=1wt-uTcc0Z645nmxJzNj-SNoqAiRM3Cix)", inline=False)
        await bot.say(embed=embed)

#Barbarian stuff goes here. 
@bot.group(pass_context=True)
async def barbarian(ctx):
    if ctx.invoked_subcommand is None:
        embed=discord.Embed(title="BARBARIAN", url="https://docs.google.com/document/d/1ZpodR2KdgA-BPQdYwoeiewuONXkjLt3vMwlK6JHzB_o/edit#bookmark=id.5q5rydukqb82", description=":fire: :rage: :fire:", color=0xff0000)
        embed.set_thumbnail(url="https://i.warosu.org/data/tg/img/0375/36/1421886982963.jpg")
        embed.add_field(name="-----", value="[Here's a link to the Barbarian PHB!](https://drive.google.com/file/d/0ByQPYPddGJI2RmppdzZWRnF5RHc/edit?disco=AAAABqEtInc)", inline=False)
        embed.add_field(name="-----", value="[Here's a list of Barbarian Abilities!](https://roll20.net/compendium/dnd5e/Barbarian#content)", inline=False)
        await bot.say(embed=embed)

#Bard stuff goes here.
@bot.group(pass_context=True)
async def bard(ctx):
    if ctx.invoked_subcommand is None:
        embed=discord.Embed(title="BARD", url="https://docs.google.com/document/d/1ZpodR2KdgA-BPQdYwoeiewuONXkjLt3vMwlK6JHzB_o/edit#bookmark=id.h49uu4x6bsxp", description="\m/:kissing:\m/", color=0xff00ff)
        embed.set_thumbnail(url="https://tribality.com/wp-content/uploads/2015/02/bard-bagpipes-240x300.jpg")
        embed.add_field(name="-----", value="[Here's a link to the Bard PHB!](https://drive.google.com/file/d/0ByQPYPddGJI2RmppdzZWRnF5RHc/edit?disco=AAAABqEtInM)", inline=False)
        embed.add_field(name="-----", value="[Here's a list of Bard Spells!](https://roll20.net/compendium/dnd5e/Bard%20Spells%20by%20Level#content)", inline=False)
        await bot.say(embed=embed)
        
#Cleric stuff goes here.
@bot.group(pass_context=True)
async def cleric(ctx):
    if ctx.invoked_subcommand is None:
        embed=discord.Embed(title="CLERIC", url="https://docs.google.com/document/d/1ZpodR2KdgA-BPQdYwoeiewuONXkjLt3vMwlK6JHzB_o/edit#bookmark=id.azxgqgx7e8pp", description=":pray:", color=0xffffff)
        embed.set_thumbnail(url="https://i1.wp.com/nerdarchy.com/wp-content/uploads/2015/11/badcleric.png?resize=238%2C300&ssl=1")
        embed.add_field(name="-----", value="[Here's a link to the Cleric PHB!](https://drive.google.com/file/d/0ByQPYPddGJI2RmppdzZWRnF5RHc/edit?disco=AAAABqEfxZ4)", inline=False)
        embed.add_field(name="-----", value="[Here's a list of Cleric Spells!](https://roll20.net/compendium/dnd5e/Cleric%20Spells%20by%20Level#content)", inline=False)
        await bot.say(embed=embed)
        
#Druid stuff goes here.
@bot.group(pass_context=True)
async def druid(ctx):
    if ctx.invoked_subcommand is None:
        embed=discord.Embed(title="DRUID", url="https://docs.google.com/document/d/1ZpodR2KdgA-BPQdYwoeiewuONXkjLt3vMwlK6JHzB_o/edit#bookmark=id.ns279cfk403q", description=":evergreen_tree:", color=0x93C47D)
        embed.set_thumbnail(url="https://i2.wp.com/nerdarchy.com/wp-content/uploads/2015/11/twisted_forest_druid_by_ubermonster-d6imryh.jpg?resize=225%2C300&ssl=1")
        embed.add_field(name="-----", value="[Here's a link to the Druid PHB!](https://drive.google.com/file/d/0ByQPYPddGJI2RmppdzZWRnF5RHc/edit?disco=AAAABqEfxb0)", inline=False)
        embed.add_field(name="-----", value="[Here's a list of Druid Spells!](https://roll20.net/compendium/dnd5e/Druid%20Spells%20by%20Level#content)", inline=False)
        await bot.say(embed=embed)
        
#Fighter stuff goes here.
@bot.group(pass_context=True)
async def fighter(ctx):
    if ctx.invoked_subcommand is None:
        embed=discord.Embed(title="FIGHTER", url="https://docs.google.com/document/d/1ZpodR2KdgA-BPQdYwoeiewuONXkjLt3vMwlK6JHzB_o/edit#bookmark=id.lc1g2x3jo7al", description=":muscle::man_in_tuxedo::punch:", color=0xFF9900)
        embed.set_thumbnail(url="https://i0.wp.com/nerdarchy.com/wp-content/uploads/2016/08/dwarf-fighter.jpg?fit=900%2C758&ssl=1")
        embed.add_field(name="-----", value="[Here's a link to the Fighter PHB!](https://drive.google.com/file/d/0ByQPYPddGJI2RmppdzZWRnF5RHc/edit?disco=AAAABqE3c7I)", inline=False)
        embed.add_field(name="-----", value="[Here's a list of Fighter Abilites!](https://roll20.net/compendium/dnd5e/Fighter#content)", inline=False)
        await bot.say(embed=embed)
        
#Lumberjack stuff goes here.
@bot.group(pass_context=True)
async def lumberjack(ctx):
    if ctx.invoked_subcommand is None:
        embed=discord.Embed(title="LUMBERJACK", url="https://docs.google.com/document/d/1ZpodR2KdgA-BPQdYwoeiewuONXkjLt3vMwlK6JHzB_o/edit#bookmark=id.j8e62xi5b8cu", description=":evergreen_tree::hammer:", color=0xB6D7A8)
        embed.set_thumbnail(url="http://magic.wizards.com/sites/mtg/files/image_legacy_migration/images/magic/daily/arcana/953_orcishlumberjack.jpg")
        embed.add_field(name="-----", value="[Here's a list of Lumberjack Abilites!](https://drive.google.com/file/d/1CZUa9FzNthWtPwi_n4i8G4OO9E0g6rbY/view)", inline=False)
        await bot.say(embed=embed)

#Monk stuff goes here.
@bot.group(pass_context=True)
async def monk(ctx):
    if ctx.invoked_subcommand is None:
        embed=discord.Embed(title="MONK", url="https://docs.google.com/document/d/1ZpodR2KdgA-BPQdYwoeiewuONXkjLt3vMwlK6JHzB_o/edit#bookmark=id.ntwkh2zi190w", description=":eye:", color=0xFFFF00)
        embed.set_thumbnail(url="http://www.enworld.org/forum/attachment.php?attachmentid=70455&d=1442794402")
        embed.add_field(name="-----", value="[Here's a link to the Monk PHB!](https://drive.google.com/file/d/0ByQPYPddGJI2RmppdzZWRnF5RHc/edit?disco=AAAABqE3c7s)", inline=False)
        embed.add_field(name="-----", value="[Here's a list of Monk Abilites!](https://roll20.net/compendium/dnd5e/Monk#content)", inline=False)
        await bot.say(embed=embed)
        
#Ranger stuff goes here.
@bot.group(pass_context=True)
async def ranger(ctx):
    if ctx.invoked_subcommand is None:
        embed=discord.Embed(title="RANGER", url="https://docs.google.com/document/d/1ZpodR2KdgA-BPQdYwoeiewuONXkjLt3vMwlK6JHzB_o/edit#bookmark=id.9z317zbgb7do", description=":bow_and_arrow:", color=0x00FF00)
        embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/dnd4/images/5/5a/Elf_ranger.jpg/revision/latest?cb=20130708222756")
        embed.add_field(name="-----", value="[Here's a link to the Revised Ranger!](https://drive.google.com/file/d/14HvaV_D_jOv3Vn5B8O3BBIxNYUiAODw1/view)", inline=False)
        await bot.say(embed=embed)
        
#Rogue stuff goes here.
@bot.group(pass_context=True)
async def rogue(ctx):
    if ctx.invoked_subcommand is None:
        embed=discord.Embed(title="ROGUE", url="https://docs.google.com/document/d/1ZpodR2KdgA-BPQdYwoeiewuONXkjLt3vMwlK6JHzB_o/edit#bookmark=id.g2jbcljwqu9n", description="spy:", color=0x000000)
        embed.set_thumbnail(url="http://www.enworld.org/forum/attachment.php?attachmentid=86366&d=1500933102")
        embed.add_field(name="-----", value="[Here's a link to the Rogue PHB!](https://drive.google.com/file/d/0ByQPYPddGJI2RmppdzZWRnF5RHc/edit?disco=AAAABqE3c7c)", inline=False)
        embed.add_field(name="-----", value="[Here's a list of Rogue Abilites!](https://roll20.net/compendium/dnd5e/Rogue#content)", inline=False)
        await bot.say(embed=embed)
        

        
        
##starts Orcabot
bot.run(OrcaConfig.token)
