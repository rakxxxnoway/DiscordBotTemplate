## Manual for Bot | Created by Rak
#
# This is a empty discord bot project! Created for save some time with starting with a own bot.
# For usage u will need to install discord.py
# Requires Python 3.6.x or higher | I recomend Python 3.7.x or older
# Install discord.py by this command                                    pip install discord.py
# To laucnh the script, type in CMD/PoweShell/BASH =>                   python name_of_the_script.py
# Thx for using my manual!
#
## Have a good time

TOKEN = ""              # token for your discord bot, can get on => https://discord.com/developers/applications | Just log in with your discord account 
bot_prefix = "."        # prefix for your Bot commands, "." by default

## None discord.py libraries ##
import os; rm = lambda: os.system("") ## *windows - cls | linux - clear*  clearing the terminal, to call it, just type => rm() ##
import random as Random

## discord.py libraries and extra ##
import discord
from discord.ext import commands
from discord.utils import get
from discord import Game

## Global Variables ## (Just insert what ever you want in those vars)
bot = commands.Bot(command_prefix= f"{bot_prefix}")         # commands prefix
bot.remove_command("help")                                  # removing old help command, cause you will have another
BOT_NAME = ""                                               # bot name which is going to be shown in terminal
bot_status = ""                                             # bot status which is going to be shown when it's onlines
test_msg = ""                                               # test msg which appears on test command
help_embed_title = "Help"                                   # help Window Titel | Change it to whatever you want to be on help window

## Terminal designe
developer = ""                              # change it to your name
system_output = "*"                         # only for design terminal; "*" by default
discord_server_name = ""                    # change it to your Discord server name
terminal_on_start_msg = f"[*] Created by {developer}\n[*] For {discord_server_name}\n\n[*] {BOT_NAME} is now Online!" # message in Bot Terminal on star, change it to whatever you want
## End of Global Variables ##


## Functions/Methods ##
## End of Functions/Methods ##


## Intro output in Terminal and Bot Status
@bot.event
async def on_ready():
    print(terminal_on_start_msg)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(bot_status))


## Bot Commands ##
@bot.command(pass_context =True)
async def help(ds):

    embed = discord.Embed(
        colour = discord.Colour.blue()              ## changes help window color
    )
    embed.set_author(name=help_embed_title) 
    
    # embed.add_field(name="``` ```", value="", inline=inline_set) <- :: Copy this and insert into command name and info about command :: 

    inline_set = False          # Do you want your output on the same line? Set True; If you want it as a list - set False 

    ## Commands list in help box
    embed.add_field(name="```.test ```", value="Checking if bot is online", inline=inline_set) ## ``` ``` these things makes your help window looks better
    await ds.send(embed=embed)

@bot.command(pass_context =True)
async def test(ds): #ds for discord
    await ds.send(f"{test_msg}")        # Replies you with a test message

## End of Bot Commands ##


## Bot launch ##
if __name__ == "__main__":
    try:
        rm()                            # cleaning console before terminal starts
        bot.run(TOKEN)                  # bot goes online with your token
    except KeyboardInterrupt:
        # Just outputing my own "exception" for manuel exiting by hitting CTRL-C
        print(f"[{system_output}] 'CTRL-C' is detected!\n[{system_output}] Terminated!")
